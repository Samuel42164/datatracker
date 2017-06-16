# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-20 14:21
from __future__ import unicode_literals

from django.db import migrations

new_addresses = {
'104-8456@mcimail.com': 3385, # John Linn
'a.ballardie@cs.ucl.ac.uk': 8269, # Anthony J. Ballardie
'a_bogdanov@iname.ru': 104669, # Alexander Bogdanov
'abbieb@nortel.com': 105441, # Abbie Barbir
'agriffin@cpcug.org': 16360, # James A. Griffin
'ah_smith@acm.org': 113171, # Andrew Smith
'ahawrylyshen@ditechnetworks.com': 106876, # Alan Hawrylyshen
'ajohnston@ipstation.com': 106289, # Alan Johnston
'ajs.ietf@gmail.com': 107364, # Aron J. Silverton
'akarp@cs.wisc.edu': 113268, # Anatoly Karp
'akoba@orange.plala.or.jp': 107496, # Atsushi Kobayashi
'akram.muhammadazam@gmail.com': 112989, # Azam Akram
'alain.baudot@francetelecom.com': 106719, # Alain Baudot
'alan@ivmg.net': 101241, # Alan Hannan
'alec.brusilovsky@alcatel-lucent.com': 101245, # Alec Brusilovsky
'alex.zinin@alcatel-lucent.com': 103264, # Alex D. Zinin
'alex@0--0.org': 103911, # Alexander Taler
'alexander.gall@switch.ch': 113278, # Alexander Gall
'alexander.steinmitz@telekom.de': 111504, # Alexander Steinmitz
'alexey@renatasystems.org': 114969, # Alexey Degtyarev
'allyn@mci.net': 4496, # Dr. Allyn Romanow
'amarine@atlas.arc.nasa.gov': 4356, # April Marine
'amir@montilio.com': 104972, # Amir Hermelin
'ana.kukec@enterprisearchitects.com': 107863, # Ana Kukec
'anant@isi.edu': 12133, # Anant Kumar
'anders.klemets@microsoft.com': 4489, # Anders Klemets
'andreas@sbin.se': 112458, # Andreas Petersson
'andrei.gurtov@teliasonera.com': 105728, # Andrei Gurtov
'antti.t.makela@iki.fi': 110136, # Antti Makela
'anuj.sehgal@navomi.com': 111956, # Anuj Sehgal
'athomson@lgscout.com': 107945, # Allan Thomson
'atkinson@itd.nrl.navy.mil': 6059, # Randall Atkinson
'azinin@nexsi.com': 103264, # Alex D. Zinin
'b.hoeneisen@ieee.org': 109505, # Bernie Hoeneisen
'balar@microsoft.com': 8354, # Dr. Bala Rajagopalan
'barnes@xylogics.com': 4848, # Jim Barnes
'barr@math.psu.edu': 18473, # David Barr
'barryf@google.com': 109799, # Barry Friedman
'bcain99@gmail.com': 113204, # Storigen Systems
'bchandle@gmail.com': 113421, # Ben Chandler
'bcn@lulea.trab.se': 19613, # Bjorn Nordgren
'bds@cisco.com': 3511, # Dr. Bruce S. Davie
'bernd.linowski.ext@nsn.com': 108731, # Bernd Linowski
'bgreenblatt@directory-applications.com': 20184, # Bruce Greenblatt
'billk@jti.com': 10543, # William Kwan
'bjewell@coppermountain.com': 100839, # Brian R. Jewell
'blaker@deming.com': 21446, # Blake C. Ramsdell
'bmanning@rice.edu': 4030, # Bill Manning
'bob.gilligan@acm.org': 2972, # Robert E. Gilligan
'bob.lynch@overturenetworks.com': 10161, # Bob Lynch
'bob@cqos.com': 113208, # Robert Mandeville
'bossert@corp.sgi.com': 15947, # Greg Bossert
'bparise@skyportsystems.com': 111993, # Bhavani Parise
'brad@cayman.com': 2865, # J. Bradford Parker
'brian.hibbard@tekelec.com': 110146, # Brian Hibbard
'brian@aero.org': 17603, # Brian Tung
'brisco@rutgers.edu': 5103, # Thomas P. Brisco
'bruce@seawaynetworks.com': 104563, # bruce Buffam
'brunner@netlab.nec.de': 104517, # Marcus Brunner
'bryan.ford@yale.edu': 106229, # Bryan Ford
'bsimpson@ray.lloyd.com': 5755, # William A. Simpson
'buglady@fuschia.net': 100013, # Aliza R. Panitz
'byf@cert.sei.cmu.edu': 3793, # Barbara Y. Fraser
'c.j.adie@edinburgh.ac.uk': 11660, # Chris Adie
'caitlin.bestler@neterion.com': 106162, # Caitlin Bestler
'callon@wellfleet.com': 2723, # Ross Callon
'carlisle.adams@entrust.com': 15836, # Dr. Carlisle Adams
'carlo.demichelis@tilab.com': 22965, # Carlo M. Demichelis
'carrel@ipsec.org': 6703, # David Carrel
'carrel@redback.net': 6703, # David Carrel
'carsten.burmeister@eu.panasonic.com': 104240, # Carsten Burmeister
'case@cs.utk.edu': 2331, # Dr. Jeff D. Case
'cbrown@wellfleet.com': 3321, # Caralyn Brown
'ccadar2@yahoo.com': 106570, # Cristian Cadar
'cdannewitz@googlemail.com': 111147, # Christian Dannewitz
'cedaoun@yahoo.fr': 105231, # Cedric Aoun
'charles.agboh@packetizer.com': 104514, # Charles Agboh
'charles.perkins@sun.com': 5133, # Charles E. Perkins
'charliekaufman@outlook.com': 107977, # Charlie Kaufman
'chimento@torrentnet.com': 4247, # Philip Chimento
'chip@technodyne.com': 107469, # Chip Popoviciu
'christophe.kalt@gmail.com': 103821, # Christophe Kalt
'cjw@magnolia.stanford.edu': 3458, # Cathy Wittbrodt
'clifford.lynch@ucop.edu': 1913, # Dr. Clifford A. Lynch
'clive@davros.org': 21288, # Clive Feather
'clw@merit.edu': 3428, # Chris Weider
'cohen@myricom.com': 184, # Dr. Danny Cohen
'colella@nist.gov': 2738, # Richard P. Colella
'craig.schelp@oracle.com': 120896, # Craig Schelp
'cromwell@nortelnetworks.com': 102270, # David Cromwell
'csapuntz@alum.mit.edu': 113267, # Constantine Sapuntzakis
'cschmec@eng.sun.com': 20582, # Christopher A. Schmechel
'd.spinellis@senanet.com': 19820, # Diomidis Spinellis
'd20@icosahedron.org': 113286, # Jay Kint
'dab@bsdi.com': 2701, # David A. Borman
'dab@cray.com': 2701, # David A. Borman
'dahoss@earthlink.net': 8860, # Albin Warth
'dan@redback.net': 102133, # Dan Simone
'danbailey@sth.rub.de': 111415, # Daniel Bailey
'daniel@iogearbox.net': 116458, # Daniel Borkmann
'daniel@isi.edu': 10804, # Daniel M.A. Zappala
'danmcd@opensolaris.org': 109859, # Daniel McDonald
'danzig@caldera.usc.edu': 6596, # Dr. Peter B. Danzig
'dap@cnt.com': 110869, # David Peterson
'dave.garcia@stanfordalumni.org': 105567, # Dave Garcia
'dave@mail.bellcore.com': 2775, # David M. Piscitello
'david.walker@sedna-wireless.com': 23178, # Dave R. Walker
'david_chuang@cosinecom.com': 100840, # David Chuang
'david_grabelsky@commworks.com': 101539, # David Grabelsky
'david_zelig@pmc-sierra.com': 105293, # David Zelig
'davidmiles@google.com': 109177, # David Miles
'dbrownell@sun.com': 19501, # David Brownell
'dck2@mail.bellcore.com': 4763, # Deirdre C. Kostick
'ddc@lcs.mit.edu': 182, # Dr. David D. Clark
'dee@lkg.dec.com': 102391, # Donald E. Eastlake 3rd
'deleganes@yahoo.com': 113377, # Ellen Deleganes
'demizu@dd.iij4u.or.jp': 9010, # Noritoshi Demizu
'dennis@juniper.com': 2766, # Dennis Ferguson
'derhwagan@yahoo.com': 2364, # Der-Hwa Gan
'dfrancis@cisco.com': 19633, # Dale Francisco
'dgilletti@yahoo.com': 104722, # Don Gilletti
'dharkins@cisco.com': 19647, # Dan Harkins
'dhs@magna.telco.com': 13872, # Doug Schremp
'dkuenzi@724.com': 103656, # Diego Kuenzi
'dlr@daver.bungi.com': 10790, # David Rand
'dmwalln@orion.ncsc.mil': 23257, # Debby M. Wallner
'dondeti@qualcomm.com': 105234, # Lakshminath R. Dondeti
'donglg@zjgsu.edu.cn': 107151, # Ligang Dong
'doug.tygar@gmail.com': 21276, # Professor Doug Tygar
'dplore@gmail.com': 107267, # Darren Loher
'dpz@dimacs.rutgers.edu': 2503, # David Paul Zimmerman
'dross@microsoft.com': 113489, # David Ross
'drummond@ieee.org': 13333, # Walt F. Drummond III
'ds-rfc@ogud.com': 3760, # Ólafur Guðmundsson
'dskim@jejutp.or.kr': 112636, # Dae-Sun Kim
'duncan.missimer@ieee.org': 104904, # Duncan Missimer
'e-krol@uiuc.edu': 304, # Edward M. Krol
'edd@acm.org': 20577, # Edgar Der-Danieliantz
'edixon@myrealbox.com': 105192, # Eric Dixon
'eellesson@lboard.com': 10585, # Ed J. Ellesson
'elb@interruptsciences.com': 104783, # Ethan Blanton
'elbell@ntlworld.com': 101385, # Les Bell
'elevinson@accurate.com': 8098, # Dr. Ed Levinson
'email2mre-rfc4506@yahoo.com': 20436, # Mike Eisler
'engan@effnet.com': 19605, # Mathias Engan
'enke@redback.com': 8348, # Enke Chen
'epg@gateway.mitre.org': 2784, # Ella P. Gardner
'epg@merit.edu': 2366, # Elise P. Gerich
'eric.mannie@perceval.net': 18669, # Eric Mannie
'eric_zimmerer@yahoo.com': 103617, # Eric Zimmerer
'ericlklein.ipv6@gmail.com': 113403, # Eric Klein
'erik.nordmark@oracle.com': 8243, # Erik Nordmark
'erik@spybeam.org': 16916, # Erik Guttman
'estrin@isi.edu': 209, # Dr. Deborah Estrin
'eva.leppanen@saunalaht.fi': 106161, # Eva Leppanen
'eva.weilandt@temic.com': 105029, # Dr. Eva Weilandt
'fair@apple.com': 2965, # Erik E. Fair
'faisal.mir@gmail.com': 112353, # Faisal Mir
'fanzhao@google.com': 106304, # Fan Zhao
'fbaker@acc.com': 2853, # Fred Baker
'feinstein@acm.org': 105027, # Benjamin Feinstein
'fenner@arista.com': 13108, # Bill Fenner
'fgalligan@google.com': 112761, # Frank Galligan
'fink@es.net': 5112, # Bill Fink
'florent.ftrd@gmail.com': 106226, # Florent Bersani
'fowler@syndesis.com': 16503, # Dave Fowler
'francis@cactus.ntt.jp': 105085, # Paul Francis
'frank.derks@nec-philips.com': 113354, # Frank Derks
'frank@bbn.com': 2706, # Frank Kastenholz
'frank@savecore.net': 103312, # Frank Cusack
'g+ietf@qualcomm.com': 18621, # Randall Gellens
'galperin@mycfo.com': 101361, # Slava Galperin
'gamunson@gmail.com': 112476, # Gary Munson
'gaoming@mail.zjgsu.edu.cn': 112296, # Ming Gao
'gary.goncher@tek.com': 104537, # Gary Goncher
'gary.tomlinson@cacheflow.com': 22809, # Gary Tomlinson
'gary@tomlinsongroup.net': 22809, # Gary Tomlinson
'gary_hanson@adc.com': 102087, # Gary Hanson
'gduan@us.oracle.com': 101422, # Gang Duan
'geertjan.degroot@bsdi.com': 2912, # Geert Jan de Groot
'gene@alertlogic.net': 106118, # Eugene Golovinsky
'geoff-s@panix.com': 106919, # Geoffrey Sisson
'ghyslain.pelletier@epl.ericsson.se': 105047, # Ghyslain Pelletier
'gja@dnrc.bell-labs.com': 8704, # Dr. Grenville Armitage
'glenn.mcgregor@merit.edu': 4416, # Glenn McGregor
'glenn@lloyd.com': 4416, # Glenn McGregor
'gmgross@securemulticast.net': 21773, # George Gross
'gmj3871@pobox.com': 6163, # George M. Jones
'gojomo@usa.net': 101035, # Gordon Mohr
'gsadasiv@rohati.com': 105681, # Ganesh Sadasivan
'gvm@att.com': 10019, # George V. Mouradian
'gyakushev@yahoo.com': 115367, # Gregory Yakushev
'hagens@ans.net': 2372, # Robert Hagens
'hank@vm.tau.ac.il': 5000, # Hank H. Nussbacher
'harald.alvestrand@delab.sintef.no': 5778, # Harald T. Alvestrand
'harald.t.alvestrand@delab.sintef.no': 5778, # Harald T. Alvestrand
'harald.t.alvestrand@uninett.no': 5778, # Harald T. Alvestrand
'hardie@equinix.com': 110721, # Ted Hardie
'has@google.com': 112938, # Heather Schiller
'heejin.jang@gmail.com': 106489, # Hee-Jin Jang
'hemma@cp.net': 18516, # Hemma Prafullchandra
'henk@procket.com': 20261, # Henk Smit
'henk@ripe.net': 100603, # Dr. Henk A.J Uijterwaal
'henry@zoo.utoronto.ca': 101423, # Henry Spencer
'herve.debar@orange-ftgroup.com': 113249, # Herve Debar
'herzog@policyconsulting.com': 13374, # Shai Herzog
'hiashida@cisco.com': 109182, # Hiroyuki Ashida
'hidetoshi.yokota@landisgyr.com': 19709, # Hidetoshi Yokota
'hirokazu.ishimatsu@g1m.jp': 104846, # Hirokazu Ishimatsu
'ho@darpa.mil': 9645, # Hilarie Orman
'holbrook@arista.com': 104288, # Hugh Holbrook
'howes@loudcloud.com': 4502, # Tim Howes
'hprafullchandra@hytrust.com': 18516, # Hemma Prafullchandra
'huangfuqing@huawei.com': 109710, # Fortune Huang
'hugokraw@us.ibm.com': 15913, # Dr. Hugo Krawczyk
'huston@franklin.ro': 113288, # Huston Franklin
'huub@van-helvoort.eu': 109312, # Huub van Helvoort
'hvivek@cisco.com': 101626, # Silvano Gai
'icemilk77@yahoo.co.jp': 113254, # Chie Kanaide
'icheol.lee@samsung.com': 107093, # Jicheol Lee
'idickins@fore.co.uk': 17469, # Ian Dickinson
'ietf-wd@v6security.com': 102247, # William Dixon
'ietf@kalbfleisch.us': 19264, # Carl W. Kalbfleisch
'ietf@mah.priv.at': 14971, # Michael Haberler
'ietfdbh@gmail.com': 17253, # David Harrington
'imap+sort+thread@lingling.panda.com': 3346, # Mark Crispin
'irene.grosclaude@orange.com': 111158, # Irene Grosclaude
'j_mandin@yahoo.com': 107354, # Jeff Mandin
'jakob@nic.se': 105400, # Jacob Schlyter
'james@bovik.org': 100793, # James Salsman
'jan@flyingcloggies.nl': 104833, # Jan Meijer
'jcucchiara@mindspring.com': 18180, # Joan Cucchiara
'jdrandall@comcast.net': 107972, # James Randall
'jdrosen.net': 2250, # Jonathan Rosenberg
'jebooth@cisco.com': 101835, # Skip Booth
'jeffp@middlebury.edu': 102261, # Jeff Parker
'jelson@cs.ucla.edu': 103980, # Jeremy Elson
'jesse@intonet.com': 102934, # Jesse R. Vincent
'jferrai@us.ibm.com': 113424, # Jon Ferraiolo
'jfmule@apple.com': 103612, # Jean-Francois Mule
'jhaas@nexthop.com': 105046, # Jeffrey Haas
'jhawk@bbnplanet.com': 16966, # John A. Hawkinson
'jheitz@lucent.com': 103462, # Jacob Heitz
'jhodges@oblix.com': 110898, # Jeff Hodges
'jineshd@juniper.net': 113028, # University of Colorado
'jjiang@syndesis.com': 113312, # Jianping Jiang
'jjp@bscs.com': 10822, # Jon J. Penner
'jlhufferd@comcast.net': 105666, # John L. Hufferd
'joan@ironbridgenetworks.com': 18180, # Joan Cucchiara
'johanietf@gmail.com': 109064, # Johan Rydell
'john.e.drake2@boeing.com': 111354, # John Drake
'john.pawling@wang.com': 22831, # John Pawling
'john3725@world.std.com': 19586, # Dr. Jonathan Trostle
'jon.harrison@metaswitch.com': 106778, # Jon Harrison
'jonathan.green@queensu.ca': 110115, # Jon Green
'jorge.gato@vodafone.com': 104716, # Jorge Gato
'jose.rey@eu.panasonic.com': 106074, # Jose Rey
'jrd@ptt.lcs.mit.edu': 2345, # James R. Davin
'jrv@mtghouse.com': 2856, # John Vollbrecht
'jssteven@us.ibm.com': 101016, # Jeffrey S. Stevens
'jtkohl@zk3.dec.com': 4837, # Theodore Ts'o
'julianchesterfield@cantab.net': 105079, # Julian Chesterfield
'julien.bournelle@orange.com': 106682, # Julien Bournelle
'jyanacek@ctron.com': 102879, # Judy Yanacek
'jyy@cosinecom.com': 3438, # Jessica Yu
'jyy@merit.edu': 3438, # Jessica Yu
'jzwiebel@cruzio.com': 12543, # John Zwiebel
'kaj@bellcore.com': 3798, # Kaj Tesink
'kaj@cc.bellcore.com': 3798, # Kaj Tesink
'kannan@isi.edu': 2830, # Kannan Varadhan
'kannan@oar.net': 2830, # Kannan Varadhan
'kasten@ftp.com': 2706, # Frank Kastenholz
'katsnelson6@peoplepc.com': 113236, # Alexander Katsnelson
'kbe@craycom.dk': 11621, # Kjeld Borch Egevang
'kdegraaf@isd.3com.com': 16911, # Kathryn de Graaf
'kent@trl.ibm.co.jp': 103130, # Kent Tamura
'kepeng.likp@gmail.com': 111131, # Kepeng Li
'kevin.e.jordan@mercury.oss.arh.cpg.cdc.com': 4420, # Kevin E. Jordan
'kfrisa@fore.com': 2777, # Karen Frisa
'kh274@cornell.edu': 18326, # Kaynam Hedayat
'klaus.wehrle@uni-tuebingen.de': 103885, # Klaus Wehrle
'klensin@nsrc.org': 106911, # Dr. John C. Klensin
'knabe@ad.cyberhome.ne.jp': 20113, # Ken Watanabe
'knichols@ieee.org': 9833, # Dr. Kathleen M. Nichols
'kobara_conf@m.aist.go.jp': 112488, # Kazukuni Kobara
'kocke@crt.xerox.com': 104324, # Kirk Ocke
'kodonog@relay.nswc.navy.mil': 4857, # Karen O'Donoghue
'krehbehn@megisto.com': 4715, # Kenneth J. Rehbehn
'krister.svanbro@ericsson.com': 103798, # Krister Svanbro
'ksmith@ascend.com': 19416, # Kevin Smith
'kuthan@fokus.fhg.de': 113276, # Jiri Kuthan
'kzm@hls.com': 2731, # Keith McCloghrie
'ladislav@lhotka.name': 107983, # Ladislav Lhotka
'lars-erik.jonsson@ericsson.com': 103797, # Lars-Erik Jonsson
'laurent.goix@econocom-osiatis.com': 113067, # Laurent Walter Goix
'leaf.y.yeh@hotmail.com': 114014, # Leaf Yeh
'leiner@nsipo.nasa.gov': 315, # Dr. Barry M. Leiner
'llavu@bacon.gmu.edu': 20716, # Lava K. Lavu
'loureiro@neclab.eu': 108663, # Paulo Loureiro
'luc.beloeil@orange.com': 106013, # Luc Beloeil
'm.saarinen@qub.ac.uk': 118829, # Markku-Juhani O. Saarinen
'mab@crypto.com': 21317, # Dr. Matt Blaze
'mail@frankwmiller.net': 105814, # Frank w. Miller
'mak@merit.edu': 2983, # Mark Knopper
'malis@maelstrom.timeplex.com': 3844, # Andrew G. Malis
'mallen@hq.walldata.com': 10701, # Michael O. Allen
'mankin@east.isi.edu': 2515, # Allison J. Mankin
'manoel.rodrigues@att.com': 3456, # Dr. Manoel A. Rodrigues
'marc@cygnus.com': 6391, # Steven J. Lunt
'marco.carugi@nortel.com': 20871, # Marco Carugi
'marijke.kaat@surfnet.nl': 12243, # Dr. Marijke Kaat
'mark.wahl@sun.com': 19108, # Mark Wahl
'markdavis@google.com': 101920, # Mark Davis
'mathur@telebit.com': 10764, # Saroop Mathur
'matt@sergeant.org': 109034, # Matt Sergeant
'matthias-philipp@gmx.de': 112556, # Matthias Philipp
'mattias@uchicago.edu<': 121182, # Mattias Lidman
'mattjf@umd.edu': 107394, # M Fanto
'mattsquire@acm.org': 106447, # Matt Squire
'mbaugher@passedge.com': 12017, # Mark Baugher
'mbeadles@endforce.com': 21400, # Mark A. Beadles
'mcampagna@gmail.com': 110599, # Matthew Campagna
'mcbride@cisco.com': 105708, # Mike McBride
'mccanne@cs.berkeley.edu': 18316, # Steven McCanne
'mcmaster@synoptics.com': 4029, # Donna McMaster
'md.1@newtbt.com': 104210, # Michael Dolan
'meconn26@gmail.com': 118267, # Michael Conn
'merlin.hughes@betrusted.com': 106125, # Merlin Hughes
'mhadley@mitre.org': 111239, # Marc Hadley
'mhausenblas@maprtech.com': 112502, # Michael Hausenblas
'michael.daniele@syamsoftware.com': 113252, # Mike Daniele
'michael.larsen@tieto.com': 106852, # Michael Larsen
'michael.tuexen@siemens.com': 104695, # Michael Tüxen
'michaelglover262@gmail.com': 112759, # Michael Glover
'micke@sm.luth.se': 18236, # Mikael Degermark
'mike.bursell@intel.com': 112817, # Mike Bursell
'mike@belshe.com': 113150, # Mike Belshe
'mike_borella@commworks.com': 101538, # Michael Borella
'milan.patel@huawei.com': 111064, # Milan Patel
'mimu@miyabi-labo.net': 113256, # Katsuhiko Mimura
'minshall@wc.novell.com': 2740, # Greg Minshall
'miyazaki.akihiro@jp.panasonic.com': 23054, # Akihiro Miyazaki
'mlasserre@alcatel-lucent.com': 105300, # Marc Lasserre
'mo@uunet.uu.net': 4817, # Michael D. O'Dell
'mohamad.badra@zu.ac.ae': 106750, # Mohamad Badra
'mohamed.khalil@ericsson.com': 108198, # Mohamed Khalil
'motonori@media.kyoto-u.ac.jp': 9198, # Motonori Nakamura
'mpvecchi@twcable.com': 4386, # Mario P. Vecchi
'mreyes@ac.upc.edu': 106104, # Angelica Reyes
'mstjohns@comcast.net': 106741, # Michael StJohns
'mwritter@applelink.apple.com': 4785, # Dr. Mike Ritter
'mxa@mail.bellcore.com': 8761, # Dr. Masuma Ahmed
'mythicalkevin@yahoo.com': 109225, # Kevin Igoe
'naiming@siara.com': 20076, # Naiming Shen
'nair_raj@yahoo.com': 4513, # Raj Nair
'nas@fu-berlin.de': 104152, # Philipp Grau
'nathan@millpark.com': 105467, # Nathan Charlton
'nevil@caida.org': 6766, # Nevil Brownlee
'niels@macfergus.com': 113337, # Niels Ferguson
'ningso@vinci-systems.com': 109626, # So Ning
'nir.ietf@gmail.com': 106745, # Yoav Nir
'npopp@verisign.com': 102231, # Nicolas Popp
'nsb@bellcore.com': 3651, # Dr. Nathaniel S. Borenstein
'ogashiwa@wide.ad.jp': 107140, # Nobuo Ogashiwa
'ogud@tislabs.com': 3760, # Ólafur Guðmundsson
'orange@spiritone.com': 20012, # Dr. Carol Orange
'orly_n@rad.co.il': 108494, # Orly Nicklass
'oshihiro.ohba@toshiba.co.jp': 106636, # Yoshihiro Ohba
'padhye@aciri.org': 103949, # Jitendra Padhye
'padma.krishnaswamy@saic.com': 7822, # Padma Krishnaswamy
'paf@nada.kth.se': 11182, # Patrik Fältström
'pashalidis@nw.neclab.eu': 107180, # Andreas Pashalidis
'patrick.masotta.ietf@vercot.com': 113507, # Patrick Masotta
'patrick.mourot@alcatel.fr': 111332, # Patrick Mourot
'paul@alantec.com': 4711, # Paul Ziemba
'paul@bayleaf.org.uk': 21801, # Paul Overell
'paul_95014@yahoo.com': 105232, # Paul Joseph
'pauljleach@msn.com': 14634, # Paul J. Leach
'perrig@cmu.edu': 104909, # Adrian Perrig
'pete@surfaceeffect.com': 113192, # Peter Bagnall
'peter.hartmann@it-sec.com': 103655, # Peter Hartmann
'peter.monaco@nuasis.com': 113319, # Peter Monaco
'pgross@ans.net': 2791, # Phillip G. Gross
'phil.m.williams@bt.com': 112831, # Philip M. Williams
'philippe.niger@orange.com': 109360, # Philippe Niger
'philrz@yahoo.com': 104857, # Phillip Rzewski
'pirey@relay.nswc.navy.mil': 10154, # Phil Irey
'pstimme@nsa.gov': 112679, # Paul Timmel
'publications@gigabeam.com': 107569, # Alan Corry
'rabie@nortel.com': 106384, # Sameh Rabie
'raj@eng.sun.com': 10754, # Raj Srinivasan
'rajesh.balay@cosinecom.com': 22820, # Rajesh I. Balay
'randy@mv.unisys.com': 18621, # Randall Gellens
'randy@nsrc.org': 5234, # Randy Bush
'rayhan@ee.ryerson.ca': 103788, # Abdallah Rayhan
'rbergma@dpc.com': 21837, # Ron Bergman
'rcoltun@ni.umd.edu': 2340, # Rob Coltun
'rcoltun@rainbow-bridge.com': 2340, # Rob Coltun
'rcoltun@siara.com': 2340, # Rob Coltun
'rcq@boxnarrow.com': 19097, # Bob Quinn
'rdantu@netrake.com': 102323, # Ram Dantu
'rdasilva@va.rr.com': 101526, # Ron da Silva
'remoore@ralvm6.vnet.ibm.com': 18205, # Dr. Robert C. Moore
'rfc4217@ford-hutchinson.com': 21156, # Paul Ford-Hutchinson
'rfox@synoptics.com': 2360, # Richard Fox
'rherriot@pahv.xerox.com': 15033, # Robert G. Herriot
'rhys.smith@jisc.ac.uk': 112289, # Rhys Smith
'richard.tse@microsemi.com': 114353, # Richard Tse
'richardstastny@gmail.com': 105862, # Richard Stastny
'rjc@cc.gatech.edu': 9549, # Russ Clark
'rkoodli@starentnetworks.com[': 101214, # Rajeev Koodli
'rlsmith@nb.ppd.ti.com': 14566, # Ronald L. Smith
'rlstewart@eng.xyplex.com': 2905, # Bob Stewart
'rmegginson0224@aol.com': 104943, # Rich Megginson
'robert.sparks@tekelec.com': 103961, # Robert Sparks
'robert.steinberger@fnc.fujitsu.com': 101196, # Robert A. Steinberger
'robs@join.com': 15883, # Rick L. Stevens
'rogeralexander@eaton.com': 109895, # Roger Alexander
'rohan@airespace.com': 104491, # Rohan Mahy
'rolf.hakenberg@eu.panasonic.com': 104239, # Rolf Hakenberg
'ronf@bluecoat.com': 8677, # Ron Frederick
'rsa-labs@rsa.com': 19822, # Ronald L. Rivest
'rsanjay@nortelnetworks.com': 104815, # Sira P. Rao
'rscott@us.axway.com': 2140, # Richard C. Scott
'rsofia@zmail.pt': 113355, # Rute Sofia
'rstory@ipsp.revelstone.com': 112321, # Robert Story
'rtroll@corp.home.net': 22867, # Ryan Troll
'rubbersoul3@yahoo.com': 113237, # Stuart M. Green
'russ.white@vce.com': 104645, # Russ White
'russerts@hotmail.com': 15057, # Steven Russert
'rwoundy@broadband.att.com': 2690, # Richard Woundy
'rwshirey4949@verizon.net': 113389, # Robert W. Shirey
's-dorner@uiuc.edu': 16250, # Steve Dorner
'sabaset@us.ibm.com': 107389, # Salman Baset
'saperia@enet.dec.com': 2809, # Jon Saperia
'saperia@mediaone.net': 2809, # Jon Saperia
'saperia@tay.dec.com': 2809, # Jon Saperia
'saperia@zko.dec.com': 2809, # Jon Saperia
'sar@iwl.com': 9791, # Shawn A. Routhier
'sassan.ahmadi@ieee.org': 106434, # Sassan Ahmadi
'saverio.niccolini@.neclab.eu': 106463, # Saverio Niccolini
'sbardalai@gmail.com': 108895, # Snigdho Bardalai
'sblakewilson@safenet-inc.com': 104696, # Simon Blake-Wilson
'sc@corp.sgi.com': 17266, # Simon P. Cooper
'schmitzjo@aol.com': 18498, # Dr. Joachim Schmitz
'sdas@ececs.uc.edu': 113195, # Samir R. Das
'sdawson@eecs.umich.edu': 20580, # Mark Allman
'sds@hill.com': 13516, # Steven D. Shepard
'sdshew@nortel.com': 4481, # Stephen Shew
'seanol@microsoft.com': 104771, # Sean Olson
'selvam@trideaworks.com': 102592, # Selvam Rengasami
'sharkey@zoic.org': 106030, # Nick Moore
'shep@alum.mit.edu': 20923, # Dr. Timothy J. Shepard
'siddharthietf@gmail.com': 109500, # Siddharth Bajaj
'silvano@ip6.com': 101626, # Silvano Gai
'sjero@purdue.edu': 114063, # Samuel Jero
'sjs@network.com': 2811, # Steve Senum
'skhurana@motorola.com': 104599, # Sumit Khurana
'smansour@ebay.com': 22880, # Steve Mansour
'smccann@blackberry.com': 110719, # Stephen McCann
'snix@metaplex.com': 10713, # Shannon D. Nix
'sra@epilogue.com': 104212, # Rob Austein
'sri@qsun.att.com': 8225, # Dr. Srinivas R. Sataluri
'srivatsa.srinivasan@gmail.com': 108467, # Srivatsa Srinivasan
'sshaffer@bridgeport-networks.com': 105921, # Scott Shaffer
'stan@netsmiths.com': 8934, # Stanley P. Hanks
'stefanforsgren@alvishagglunds.se': 105266, # Stefan Forsgren
'stephan.teiwes@it-sec.com': 103654, # Stephen Teiwes
'stephen@mchenry.net': 105044, # Stephen McHenry
'steqve@shore.net': 104230, # SteQven Christey
'stev@ftp.com': 9122, # Stev Knowles
'steve.gonczi@networkengines.com': 102188, # Steve Gonczi
'steve.hanna@infineon.com': 15448, # Stephen R. Hanna
'steve@sm.luth.se': 4966, # Stephen Pink
'stevea@lachman.com': 3850, # Steve Alexander
'stevef@nasuni.com': 107116, # Stephen Fridella
'stevej@netmanage.com': 15074, # Steven J. Jackowski
'stjohns@darpa.mil': 106741, # Michael StJohns
'stokese@us.ibm.com': 21456, # Ellen Stokes
'sundell@nortelnetworks.com': 19643, # Kenneth Sundell
'sung1.lee@samsung.com': 106487, # Sung-Hyuck Lee
'susan.joseph@vdtg.com': 113369, # Susan Joseph
'suyong@ist.osaka-u.ac.jp': 114932, # Suyong Eum
'swol@andrew.cmu.edu': 2689, # Steven Waldbusser
'szander@swin.edu.au': 104609, # Sebastian Zander
'szilles@mv.us.adobe.com': 9668, # Steve N. Zilles
'tacox@mail.bellcore.com': 3345, # Tracy A. Brown
'tata_kalyan@yahoo.com': 106326, # Kalyan Tata
'tbdean@qinetiq.com': 15520, # Tim Dean
'tedgavin@newsguy.com': 103935, # Edward Gavin
'terzis@cs.jhu.edu': 20892, # Andreas Terzis
'tgeorge_tx@verizon.net': 104129, # Tom George
'thomas.froment@tech-invite.com': 107475, # Thomas Froment
'thomas.johannsen@ifn.et.tu-dresden.de': 8758, # Thomas Johannsen
'thomas.nadeau@huawei.com': 104197, # Thomas Nadeau
'thomwu@cisco.com': 23231, # Thomas Wu
'timbl@info.cern.ch': 6861, # Tim Berners-Lee
'timm@rainwillow.com': 102640, # Tim J. Melanchuk
'tli@tropos.com': 4475, # Dr. Tony Li
'tmtalpey@gmail.com': 8209, # Tom Talpey
'tom.hastings@alum.mit.edu': 14890, # Thomas N. Hastings
'tom.worster@motorola.com': 100623, # Tom Worster
'ton.verschuren@surfnet.nl': 8122, # Dr. Ton Verschuren
'toni.paila@gmail.com': 105787, # Toni Paila
'tony+msgtrk@maillennium.att.com': 6771, # Tony Hansen
'topolcic@cnri.reston.va.us': 2828, # Claudio M. Topolcic
'tzetatsao@eaton.com': 111179, # Tzeta Tsao
'uhhyung@kaist.ac.kr': 5295, # Uhhyung Choi
'ulrich.drafz@telekom.de': 108873, # Ulrich Drafz
'urimobile@optonline.net': 8774, # Uri Blumenthal
'v.goyal@ieee.org': 17589, # Vivek Goyal
'vaf@stanford.edu': 2362, # Vince Fuller
'vaf@valinor.stanford.edu': 2362, # Vince Fuller
'vesa.torvinen@turkuamk.fi': 105361, # Vesa Torvinen
'viega@list.org': 107111, # John Viega
'vishwas@sinett.com': 105627, # Vishwas Manral
'vrangan@brocade.com': 5746, # Venkat D. Rangan
'vsriniva@cosinecom.com': 19073, # Dr. Vijay Srinivasan
'waldbusser@andrew.cmu.edu': 2689, # Steven Waldbusser
'waldbusser@cmu.edu': 2689, # Steven Waldbusser
'waldbusser@ins.com': 2689, # Steven Waldbusser
'waldemar@wdmsys.com': 105191, # Waldemar Augustyn
'walter.wimer@cmu.edu': 2835, # Walter Wimer
'walterweiss@attbi.com': 100760, # Walter Weiss
'wclark@cisco.com': 10720, # Wayne C. Clark
'wel@bellcore.com': 19079, # Will E. Leland
'wfms@ottix.net': 107646, # William F. Maton
'willy@haproxy.com': 113096, # Willy Tarreau
'wk04464@worldlink.com': 2775, # David M. Piscitello
'wnicolls@forsythesolutions.com': 102991, # Weston Nicolls
'wray@tuxedo.enet.dec.com': 9240, # John Wray
'wsawyer@ieee.org': 8267, # Wilson Sawyer
'xipeng@gblx.net': 103866, # X Xiao
'yangwooko@gmail.com': 107280, # YangWoo Ko
'ybernet@msn.com': 20296, # Yoram Bernet
'yeongw@psilink.com': 4155, # Wengyik Yeong
'yidarlo@yahoo.com': 102351, # Jeffrey Lo
'ying.zhang13@hp.com': 108726, # Ying Zhang
'yoshida@peta.arch.ecl.net': 20814, # Toshiaki Yoshida
'young@netntv.co.kr': 19477, # Yuen Lim
'yulindong@gmail.com': 113223, # Yulin Dong
'zbig@eicon.qc.ca': 6860, # Zbigniew Kielczewski
'zhiwlin@nyct.com': 104865, # Zhi Lin
'zhouweiisu@gmail.com': 114358, # Wei Zhou
'zsatou@t-ns.co.jp': 104489, # T Satoh
}


def forward(apps,schema_editor):

    Email=apps.get_model('person','Email')

    # Sanity check
    for addr in new_addresses.keys():
        if Email.objects.filter(address__iexact=addr).exists():
            raise Exception("%s already exists in the Email table"%addr)

    for addr in new_addresses.keys():
        Email.objects.create(address=addr,person_id=new_addresses[addr],active=False,primary=False)

def reverse(apps,schema_editor):
    Email=apps.get_model('person','Email')
    #Person=apps.get_model('person','Person')
    #print "new_addresses = {"
    #for addr in sorted(new_addresses.keys()):
    #    print "'%s': %s, # %s"%(addr,new_addresses[addr],Person.objects.get(pk=new_addresses[addr]).name) 
    #print "}"
    Email.objects.filter(address__in=new_addresses.keys()).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('person', '0015_clean_primary'),
    ]

    operations = [
        migrations.RunPython(forward,reverse)
    ]
