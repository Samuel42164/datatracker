# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomcom', '0011_auto_20161207_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nominee',
            options={'ordering': ['-nomcom__group__acronym', 'email__address'], 'verbose_name_plural': 'Nominees'},
        ),
    ]
