# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 11:59
from __future__ import unicode_literals

import datetime
import sys
from tqdm import tqdm

from django.db import migrations

import debug                            # pyflakes:ignore

rev_fix_desc = [
    "Uploaded new revision",
    "Request for posting confirmation",
    "New version approved",
    "Posted submission manually",
]

time_fix_desc = rev_fix_desc + [
    "New version available",
]

untouchable_type = ['new_revision', ]
untouchable_desc = [
    "IANA Action state changed",
    "IANA Review state changed",
    "RFC Editor state changed",
]

name_shown = False

def ename(event):
    return u"event #%d %s %s by %s at %s" % (event.pk, event.doc.name, event.get_type_display().lower(), event.by.name, event.time)

def change_rev(e, r):
    global name_shown
    if not name_shown:
        #debug.say("")
        #debug.show('e.doc.name')
        name_shown = True
    #debug.say('Changing rev %s -> %s for %s' % (e.rev, r.rev, ename(e)))
    e.rev = r.rev
    e.save()

def forwards(apps, schema_editor):
    global name_shown
    DocEvent = apps.get_model('doc', 'DocEvent')
    events = DocEvent.objects.filter(time__gt='2016-09-10', time__lt='2016-10-04', doc__type='draft').order_by('id')
    #debug.say('')
    #debug.show('events.count()')
    docs = set()
    for e in events:
        docs.add(e.doc)
    sys.stdout.write('\n')
    for doc in tqdm(docs):
        name_shown = False
        if events.filter(doc=doc, type='new_revision').exists():
            # first scan from past towards present and fix up time:
            docevents = DocEvent.objects.filter(doc=doc).order_by('id')
            prev = docevents.first()
            for event in docevents:
                # review_request-related events may have out-of-order times
                # because of import of historical data:
                if event.time < prev.time and not 'review_request' in event.type:
                    for desc_start in time_fix_desc:
                        if event.desc.startswith(desc_start):
                            if not name_shown:
                                #debug.say("")
                                #debug.show('doc.name')
                                name_shown = True
                            #debug.say("Fixing up time -> %s for %s" % (prev.time, ename(event)))
                            event.time = prev.time
                            event.save()
                            break
                    else:
                        if event.type in untouchable_type:
                            break
                        for desc_start in untouchable_desc:
                            if event.desc.startswith(desc_start):
                                break
                        else:
                            #debug.say("** Out of order time for event %s" % (ename(event),))
                            pass
                prev = event
            #
            # then scan from present towards past and fix up revision:
            docevents = DocEvent.objects.filter(doc=doc).order_by('-id')
            seen = None
            for event in docevents:
                if event.type == 'new_revision':
                    if seen and event.rev == seen.rev:
                        if (seen.time - event.time) < datetime.timedelta(seconds=60):
                            #debug.say("Two new_revision events with the same rev: %s on %s and %s. Deleting the first." % (event.rev, seen.time, event.time))
                            event.delete()
                        else:
                            #debug.say("** Two new_revision events with the same rev: %s on %s and %s. Differnt time, not deleting." % (event.rev, seen.time, event.time))
                            pass
                    else:
                        seen = event
                else:
                    pass
                for desc_start in rev_fix_desc:
                    if event.desc.startswith(desc_start) and seen and event.rev != seen.rev:
                        if (seen.time-event.time) < datetime.timedelta(hours=2): # 2 hours is a bit arbitrary
                            change_rev(event, seen)
                            break
                        elif name_shown:
                            #debug.say('Skipping change %s -> %s (at %s) for %s ' % (event.rev, seen.rev, seen.time, ename(event), ))
                            pass
                        else:
                            pass

def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0017_auto_20161207_1046'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
