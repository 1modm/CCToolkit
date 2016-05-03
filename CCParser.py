#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """

CCParser

Author: https://twitter.com/1_mod_m/

Project site: https://github.com/1modm/

Copyright (c) 2016, MM
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""


#------------------------------------------------------------------------------
# Modules
#------------------------------------------------------------------------------

import os
import sys
import hashlib
import xml.etree.ElementTree as ET # pip install elementtree
import sqlite3
from thirdparty.color.termcolor import colored

#------------------------------------------------------------------------------
# Python version check.
#------------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        show_banner()
        print ("[!] You must use Python version 2.7 or above")
        sys.exit(1)

try:
    import argparse
except ImportError:
    print 'argparse required. Install using `pip install argparse`'
    sys.exit(1)



#------------------------------------------------------------------------------
# Command line parser using argparse
#------------------------------------------------------------------------------

def cmdline_parser():
    parser = argparse.ArgumentParser(conflict_handler='resolve', add_help=True,
        description='Example: python %(prog)s doc/cc3R4.xml', version='CCParser 0.1',
        usage="python %(prog)s [OPTIONS]")

    # Mandatory
    parser.add_argument('XMLfile', action="store")
    parser.add_argument('-ask', action='store_true', default=False, dest='ask')

    return parser




#------------------------------------------------------------------------------
# CCParser
#------------------------------------------------------------------------------
class functions:

    def cc_chapter(self,idelement):
    	'''
    	Set the chapter number as in PDF files provided in http://www.commoncriteriaportal.org/
    	'''

        CCpart1_chapter = ""
        CCpart2_chapter = ""
        CCpart3_chapter = ""
        CEM_chapter = ""

        #-----------------------------------------------------------------------------------
        if (idelement == "Introduction"):  CCpart1_chapter = 1
        if (idelement == "Scope"):  CCpart1_chapter = 2
        if (idelement == "Normative references"):  CCpart1_chapter = 3
        if (idelement == "Terms and definitions"): CCpart1_chapter = 4
        if (idelement == "Symbols and abbreviated terms"):  CCpart1_chapter = 5
        if (idelement == "Overview"):  CCpart1_chapter = 6
        if (idelement == "General model"):  CCpart1_chapter = 7
        if (idelement == "Tailoring Security Requirements"):  CCpart1_chapter = 8
        if (idelement == "Protection Profiles and Packages"):  CCpart1_chapter = 9
        if (idelement == "Evaluation results"):  CCpart1_chapter = 10
        if (idelement == "Specification of Security Targets"):  CCpart1_chapter = "Annex A"
        if (idelement == "Specification of Protection Profiles"):  CCpart1_chapter = "Annex B"
        if (idelement == "Guidance for Operations"):  CCpart1_chapter = "Annex C"
        if (idelement == "PP conformance"):  CCpart1_chapter = "Annex D"
        if (idelement == "Bibliography"):  CCpart1_chapter = "Annex E"
        #-----------------------------------------------------------------------------------
        if (idelement == "Introduction"):  CCpart2_chapter = 1
        if (idelement == "Scope"):  CCpart2_chapter = 2
        if (idelement == "Normative references"):  CCpart2_chapter = 3
        if (idelement == "Terms and definitions, symbols and abbreviated terms"):  CCpart2_chapter = 4
        if (idelement == "Overview"):  CCpart2_chapter = 5
        if (idelement == "Functional requirements paradigm"):  CCpart2_chapter = 6
        if (idelement == "Security functional components"):  CCpart2_chapter = 7
        if (idelement == "Security audit"):  CCpart2_chapter = 8
        if (idelement == "Communication"):  CCpart2_chapter = 9
        if (idelement == "Cryptographic support"):  CCpart2_chapter = 10
        if (idelement == "User data protection"):  CCpart2_chapter = 11
        if (idelement == "Identification and authentication"):  CCpart2_chapter = 12
        if (idelement == "Security management"):  CCpart2_chapter = 13
        if (idelement == "Privacy"):  CCpart2_chapter = 14
        if (idelement == "Protection of the TSF"):  CCpart2_chapter = 15
        if (idelement == "Resource utilisation"):  CCpart2_chapter = 16
        if (idelement == "TOE access"):  CCpart2_chapter = 17
        if (idelement == "Trusted path/channels"):  CCpart2_chapter = 18
        if (idelement == "Security functional requirements application notes"):  CCpart2_chapter = "Annex A"
        if (idelement == "Functional classes, families, and components"):  CCpart2_chapter = "Annex B"
        #-----------------------------------------------------------------------------------
        if (idelement == "Introduction"):  CCpart3_chapter = 1
        if (idelement == "Scope"):  CCpart3_chapter = 2
        if (idelement == "Normative references"):  CCpart3_chapter = 3
        if (idelement == "Terms and definitions, symbols and abbreviated terms"): CCpart3_chapter = 4
        if (idelement == "Overview"):  CCpart3_chapter = 5
        if (idelement == "Assurance paradigm"):  CCpart3_chapter = 6
        if (idelement == "Security assurance components"):  CCpart3_chapter = 7
        if (idelement == "Evaluation assurance levels"):  CCpart3_chapter = 8

        if (idelement == "functionally tested"):  CCpart3_chapter = 8
        if (idelement == "structurally tested"):  CCpart3_chapter = 8
        if (idelement == "methodically tested and checked"):  CCpart3_chapter = 8
        if (idelement == "methodically designed, tested, and reviewed"):  CCpart3_chapter = 8
        if (idelement == "semiformally designed and tested"):  CCpart3_chapter = 8
        if (idelement == "semiformally verified design and tested"):  CCpart3_chapter = 8
        if (idelement == "formally verified design and tested"):  CCpart3_chapter = 8
        if (idelement == "Structurally composed"):  CCpart3_chapter = 8
        if (idelement == "Methodically composed"):  CCpart3_chapter = 8
        if (idelement == "Methodically composed, tested and reviewed"): CCpart3_chapter = 8
        if (idelement == "patchinfo"):  CCpart3_chapter = 8

        if (idelement == "Composed assurance packages"):  CCpart3_chapter = 9
        if (idelement == "Protection Profile evaluation"):  CCpart3_chapter = 10
        if (idelement == "Security Target evaluation"): CCpart3_chapter = 11
        if (idelement == "Development"):  CCpart3_chapter = 12
        if (idelement == "Guidance documents"):  CCpart3_chapter = 13
        if (idelement == "Life-cycle support"):  CCpart3_chapter = 14
        if (idelement == "Tests"):  CCpart3_chapter = 15
        if (idelement == "Vulnerability assessment"):  CCpart3_chapter = 16
        if (idelement == "Composition"):  CCpart3_chapter = 17
        if (idelement == "Development (ADV)"):  CCpart3_chapter = "Annex A"
        if (idelement == "Composition (ACO)"):  CCpart3_chapter = "Annex B"
        if (idelement == "Cross reference of assurance component dependencies"):  CCpart3_chapter = "Annex C"
        if (idelement == "Cross reference of PPs and assurance components"):  CCpart3_chapter = "Annex D"
        if (idelement == "Cross reference of EALs and assurance components"):  CCpart3_chapter = "Annex E"
        if (idelement == "Cross reference of CAPs and assurance components"):  CCpart3_chapter = "Annex F"

        #-----------------------------------------------------------------------------------
        if (idelement == "Introduction"):  CEM_chapter = 1
        if (idelement == "Scope"):  CEM_chapter = 2
        if (idelement == "Normative references"):  CEM_chapter = 3
        if (idelement == "Terms and definitions"):  CEM_chapter = 4
        if (idelement == "Symbols and abbreviated terms"):  CEM_chapter = 5
        if (idelement == "Overview"):  CEM_chapter = 6
        if (idelement == "Document Conventions"):  CEM_chapter = 7
        if (idelement == "Evaluation process and related tasks"):  CEM_chapter = 8
        if (idelement == "General evaluation guidance"):  CEM_chapter = "Annex A"
        if (idelement == "Vulnerability       Assessment (AVA)"):  CEM_chapter = "Annex B"


        Chapter_cc = 0
        doc = 0
        if CCpart1_chapter: 
            Chapter_cc = CCpart1_chapter
            doc = 1
        if CCpart2_chapter: 
            Chapter_cc = CCpart2_chapter
            doc = 2
        if CCpart3_chapter: 
            Chapter_cc = CCpart3_chapter
            doc = 3
        if CEM_chapter: 
            Chapter_cc = CEM_chapter
            doc = 4

        return (Chapter_cc, doc)


    def cc_chapter_order(self,keyelement):
        '''
        Set the chapter number as in PDF files provided in http://www.commoncriteriaportal.org/
        '''

        CCpart1_chapter = ""
        CCpart2_chapter = ""
        CCpart3_chapter = ""
        CEM_chapter = ""

        if (int(keyelement) == 31): CCpart1_chapter = 1
        if (int(keyelement) == 32): CCpart1_chapter = 2
        if (int(keyelement) == 33): CCpart1_chapter = 3
        if (int(keyelement) == 34): CCpart1_chapter = 4
        if (int(keyelement) == 35): CCpart1_chapter = 5
        if (int(keyelement) == 36): CCpart1_chapter = 6
        if (int(keyelement) == 37): CCpart1_chapter = 7
        if (int(keyelement) == 38): CCpart1_chapter = 8
        if (int(keyelement) == 39): CCpart1_chapter = 9
        if (int(keyelement) == 40): CCpart1_chapter = 10
        if (int(keyelement) == 41): CCpart1_chapter = 11
        if (int(keyelement) == 42): CCpart1_chapter = 12
        if (int(keyelement) == 43): CCpart1_chapter = 13
        if (int(keyelement) == 44): CCpart1_chapter = 14
        if (int(keyelement) == 45): CCpart1_chapter = 15
        #-------------------
        if (int(keyelement) == 25): CCpart2_chapter = 20
        if (int(keyelement) == 28): CCpart2_chapter = 21
        if (int(keyelement) == 27): CCpart2_chapter = 22
        if (int(keyelement) == 24): CCpart2_chapter = 23
        if (int(keyelement) == 26): CCpart2_chapter = 24
        if (int(keyelement) == 29): CCpart2_chapter = 25
        if (int(keyelement) == 48): CCpart2_chapter = 26
        if (int(keyelement) == 50): CCpart2_chapter = 27
        if (int(keyelement) == 51): CCpart2_chapter = 28
        if (int(keyelement) == 52): CCpart2_chapter = 29
        if (int(keyelement) == 53): CCpart2_chapter = 30
        if (int(keyelement) == 54): CCpart2_chapter = 31
        if (int(keyelement) == 55): CCpart2_chapter = 32
        if (int(keyelement) == 56): CCpart2_chapter = 33
        if (int(keyelement) == 57): CCpart2_chapter = 34
        if (int(keyelement) == 58): CCpart2_chapter = 35
        if (int(keyelement) == 59): CCpart2_chapter = 36
        if (int(keyelement) == 60): CCpart2_chapter = 37
        if (int(keyelement) == 23): CCpart2_chapter = 38
        if (int(keyelement) == 49): CCpart2_chapter = 39
        #-------------------
        if (int(keyelement) == 2):  CCpart3_chapter = 40
        if (int(keyelement) == 5):  CCpart3_chapter = 41
        if (int(keyelement) == 4):  CCpart3_chapter = 42
        if (int(keyelement) == 1):  CCpart3_chapter = 43
        if (int(keyelement) == 3):  CCpart3_chapter = 44
        if (int(keyelement) == 9):  CCpart3_chapter = 45
        if (int(keyelement) == 47): CCpart3_chapter = 46 
        if (int(keyelement) == 21): CCpart3_chapter = 47
        if (int(keyelement) == 69): CCpart3_chapter = 48
        if (int(keyelement) == 70): CCpart3_chapter = 49
        if (int(keyelement) == 71): CCpart3_chapter = 50
        if (int(keyelement) == 72): CCpart3_chapter = 51
        if (int(keyelement) == 73): CCpart3_chapter = 52
        if (int(keyelement) == 74): CCpart3_chapter = 53
        if (int(keyelement) == 75): CCpart3_chapter = 54
        if (int(keyelement) == 76): CCpart3_chapter = 55
        if (int(keyelement) == 77): CCpart3_chapter = 56
        if (int(keyelement) == 78): CCpart3_chapter = 57
        if (int(keyelement) == 79): CCpart3_chapter = 58
        if (int(keyelement) == 12): CCpart3_chapter = 59
        if (int(keyelement) == 65): 
            CCpart3_chapter = 60
            CEM_chapter = 60
        if (int(keyelement) == 66):
            CCpart3_chapter = 61
            CEM_chapter = 61
        if (int(keyelement) == 62):
            CCpart3_chapter = 62
            CEM_chapter = 62
        if (int(keyelement) == 63): 
            CCpart3_chapter = 63
            CEM_chapter = 63
        if (int(keyelement) == 64): 
            CCpart3_chapter = 64
            CEM_chapter = 64
        if (int(keyelement) == 67): 
            CCpart3_chapter = 65
            CEM_chapter = 65
        if (int(keyelement) == 68): 
            CCpart3_chapter = 66
            CEM_chapter = 66
        if (int(keyelement) == 61): 
            CCpart3_chapter = 67
            CEM_chapter = 67
        if (int(keyelement) == 7):  CCpart3_chapter = 68
        if (int(keyelement) == 6):  CCpart3_chapter = 69
        if (int(keyelement) == 8):  CCpart3_chapter = 70
        if (int(keyelement) == 46): CCpart3_chapter = 71 
        if (int(keyelement) == 20): CCpart3_chapter = 72
        if (int(keyelement) == 11): CCpart3_chapter = 73
        #-------------------
        if (int(keyelement) == 15): CEM_chapter = 50
        if (int(keyelement) == 18): CEM_chapter = 51
        if (int(keyelement) == 17): CEM_chapter = 52
        if (int(keyelement) == 14): CEM_chapter = 53
        if (int(keyelement) == 19): CEM_chapter = 54
        if (int(keyelement) == 16): CEM_chapter = 55
        if (int(keyelement) == 13): CEM_chapter = 56
        if (int(keyelement) == 30): CEM_chapter = 57
        if (int(keyelement) == 22): CEM_chapter = 88 
        if (int(keyelement) == 10): CEM_chapter = 89

        Chapter_cc = 0
        cc1 = 0
        cc2 = 0
        cc3 = 0
        cem = 0

        if CCpart1_chapter: 
            Chapter_cc = CCpart1_chapter
            cc1 = 1
        if CCpart2_chapter: 
            Chapter_cc = CCpart2_chapter
            cc2 = 1
        if CCpart3_chapter: 
            Chapter_cc = CCpart3_chapter
            cc3 = 1
        if CEM_chapter: 
            Chapter_cc = CEM_chapter
            cem = 1


        return (Chapter_cc, cc1, cc2, cc3, cem)


#------------------------------------------------------------------------------------

class CCParser:
    '''
    Main Class
    '''

    try:
        parser = cmdline_parser()
        # Show help if no args
        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(1)
    except NameError:
        parser.print_help()
        sys.exit(1)

    # Get args
    results = parser.parse_args()
    # No failure by default :)
    failure = False
    # Filename and XML root with ElementTree to parse
    tree = ET.parse(results.XMLfile)
    root = tree.getroot()

    print os.linesep + ((colored("[+] CCParser (Use at your own risk)", 'yellow')))


    #------------------------------------------------------------------------------
    # Variables
    #------------------------------------------------------------------------------

    n=0 # Main counter
    c1=0 # 1st level elements counter
    c2=0 # 2º level elements counter
    c3=0 # 3er level elements counter
    c4=0 # 4º level elements counter
    c5=0 # 5º level elements counter
    c6=0 # 6º level elements counter
    c7=0 # 7º level elements counter
    c8=0 # 8º level elements counter
    c9=0 # 9º level elements counter
    c10=0 # 10º level elements counter
    c11=0 # 11º level elements counter
    c12=0 # 12º level elements counter

    # Dict to save parsed data
    child1_total = {}
    child2_total = {}
    child3_total = {}
    child4_total = {}
    child5_total = {}
    child6_total = {}
    child7_total = {}
    child8_total = {}
    child9_total = {}
    child10_total = {}
    child11_total = {}
    child12_total = {}


    #------------------------------------------------------------------------------
    # DB
    #------------------------------------------------------------------------------

    # Create a database in RAM
    print ((colored("[+] Generated database in: data/ccdb.sqlite3", 'red')))

    #db = sqlite3.connect(':memory:')
    # Creates or opens a file called mydb with a SQLite3 DB
    if not os.path.exists('data'):
        os.makedirs('data')
    db = sqlite3.connect('data/ccdb.sqlite3')
    # Remove previous
    cursor = db.cursor()
    cursor.execute('''DROP TABLE IF EXISTS xref''')
    cursor.execute('''DROP TABLE IF EXISTS child1''')
    cursor.execute('''DROP TABLE IF EXISTS child2''')
    cursor.execute('''DROP TABLE IF EXISTS child3''')
    cursor.execute('''DROP TABLE IF EXISTS child4''')
    cursor.execute('''DROP TABLE IF EXISTS child5''')
    cursor.execute('''DROP TABLE IF EXISTS child6''')
    cursor.execute('''DROP TABLE IF EXISTS child7''')
    cursor.execute('''DROP TABLE IF EXISTS child8''')
    cursor.execute('''DROP TABLE IF EXISTS child9''')
    cursor.execute('''DROP TABLE IF EXISTS child10''')
    db.commit()


    #------------------------------------------------------------------------------
    # Parse the text depending on type of element, return text
    #------------------------------------------------------------------------------

    def elements_parser_all(itemxml, idstotal, chapter_child1_text):
        paratext = ""
        chapter_number = 0
        num_doc = 0
        CCVERSION = "3.1"
        CCREVISION = "4"
        CCDATE = "September 2012"

        chapter_child1, num_doc_chapter_child1 = functions().cc_chapter(chapter_child1_text)

        #### para ####
        if itemxml.tag == "para":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""
                
        #### xref ####
        if itemxml.tag == "xref":
            try:
                if (str(itemxml.get('show')) == "none"):
                    chapter_number, num_doc = functions().cc_chapter(idstotal[itemxml.get('id')][0])
                    if (chapter_number > 0):
                        paratext += " " + str(chapter_number) + ": " + str(idstotal[itemxml.get('id')][0]) + " "
                    else:
                        paratext += " " + str(idstotal[itemxml.get('id')][0]) + " "
                        #paratext += " " + xref.get('id').upper() + ":" + str(idstotal[xref.get('id')][0]) + " "
                elif (str(itemxml.get('show')) == "title"):
                    paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "

                elif (str(itemxml.get('show')) == "id"):
                    if (str(itemxml.get('id')) == str(idstotal[itemxml.get('id')][0])):
                        paratext += " " + itemxml.get('id').upper() + " "
                    else:
                        paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "
                elif (str(itemxml.get('show')) == "link"):
                    try:
                        chapter_number, num_doc = functions().cc_chapter(idstotal[itemxml.get('id')][0])
                        if (chapter_child1_text == "Overview"):
                            paratext += " " + str(chapter_number) + " "
                        elif (chapter_number in (12, 17)): # ADV ACO
                            paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "
                        elif (("interact" or "types-of") in itemxml.get('id')):
                            paratext += " " + idstotal[itemxml.get('id')][0] + " "
                        elif (str(num_doc) == str(num_doc_chapter_child1)):
                            paratext += " " + str(num_doc) + " "
                        else:
                            paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "
                    except:
                        paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "
                else:
                    try:
                        paratext += " " + str(functions().cc_chapter(idstotal[itemxml.get('id')][0])) + " "
                    except:
                        paratext += " " + itemxml.get('id').upper() + ": " + str(idstotal[itemxml.get('id')][0]) + " "
            except:
                if (itemxml.get('fakeid')):
                    paratext += " fakeid "
                else:
                    paratext += ""

            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n') 
            except:
                paratext += "" 


        #### item ####
        elif itemxml.tag == "item":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n') 
            except:
                paratext += "" 
                
        #### list ####
        elif itemxml.tag == "list":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### bold ####
        elif itemxml.tag == "bold":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += "" 

        #### italic ####
        elif itemxml.tag == "italic":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### title - table ####
        elif itemxml.tag == "title":
            paratext += " ".join(itemxml.text.split()).rstrip('\r\n')

        #### entry - table ####
        elif itemxml.tag == "entry":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += "" 
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += "" 

        #### biblioterm ####
        elif itemxml.tag == "biblioterm":
            paratext += " ".join(itemxml.text.split()).rstrip('\r\n')

        #### bibliodef ####
        elif itemxml.tag == "bibliodef":
            paratext += " ".join(itemxml.text.split()).rstrip('\r\n').replace("_CCVERSION_", CCVERSION).replace("_CCREVISION_", CCREVISION).replace("_CCDATE_", CCDATE)
            
        #### url ####
        elif itemxml.tag == "url":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += "" 
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += "" 

        #### eal-component ####
        elif itemxml.tag == "eal-component":
            paratext += itemxml.get('acomponent').upper() + ": " + str(idstotal[itemxml.get('acomponent')][0]) + " "

        #### cap-component ####
        elif itemxml.tag == "cap-component":
            paratext += itemxml.get('acomponent').upper() + ": " + str(idstotal[itemxml.get('acomponent')][0]) + " "

        #### a-family ####
        elif itemxml.tag == "a-family":
            paratext += itemxml.get('name')+ " (" + str(idstotal[itemxml.get('id')][0]) + ")"

        #### ae-developer ####
        elif itemxml.tag == "ae-developer":
            paratext += itemxml.get('id').upper() + "   " + " ".join(itemxml.text.split()).rstrip('\r\n')

        #### ae-content ####
        elif itemxml.tag == "ae-content":
            paratext += itemxml.get('id').upper() + "   " + " ".join(itemxml.text.split()).rstrip('\r\n')

        #### ae-evaluator ####
        elif itemxml.tag == "ae-evaluator":
            paratext += itemxml.get('id').upper() + "   " + " ".join(itemxml.text.split()).rstrip('\r\n')

        #### ae-dc-element ####
        elif itemxml.tag == "ae-dc-element":
            paratext += itemxml.get('id').upper() + " "

        #### glossentry ####
        elif itemxml.tag == "glossentry":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
                #paratext += " None bold "
            except:
                paratext += ""

        #### glossterm ####
        elif itemxml.tag == "glossterm":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### glossdef ####
        elif itemxml.tag == "glossdef":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### glossnote ####
        elif itemxml.tag == "glossnote":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### glossalt ####
        elif itemxml.tag == "glossalt":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### glosssource ####
        elif itemxml.tag == "glosssource":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""
                
        #### acronym ####
        elif itemxml.tag == "acronym":
            paratext += itemxml.get('id').upper()

        #### acronymterm ####
        elif itemxml.tag == "acronymterm":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### acronymdef ####
        elif itemxml.tag == "acronymdef":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### f-element ####
        elif itemxml.tag == "f-element":
            try:
                paratext += itemxml.get('id').upper()
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""
            try:
                paratext += " assignmentitemSUBSTITUTE "
                paratext += " ".join(itemxml.tail.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### f-assignmentitem ####
        elif itemxml.tag == "fe-assignmentitem":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### fe-assignment ####
        elif itemxml.tag == "fe-assignment":
            try:
                paratext += " ".join(itemxml.text.split()).rstrip('\r\n')
            except:
                paratext += ""

        #### a-component ####
        elif itemxml.tag == "a-component":
            try:
                paratext += itemxml.get('id').upper()
            except:
                paratext += ""


        formatedparatext = paratext.rstrip('\r\n').replace("Subclause", "Section").replace("subclause", "section").replace("Clause", "Chapter").replace("clause", "chapter")

        return formatedparatext

    
    # -------------------------------------------------------------------------------------
    # Dict that contains all xref elements in order to replace in the final text
    # by the title or id referenced.
    # -------------------------------------------------------------------------------------

    ids_total = {}
    id_list = [element.get('id') for element in root.findall(".//*[@id]")]

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE xref(id INTEGER PRIMARY KEY, type TEXT, name TEXT, title TEXT, idxref TEXT)
    ''')

    for idl in root.findall(".//*[@id]"):
        if idl.tag != "xref":
            ids_total.setdefault(idl.get('id'), [])
            if (idl.get('title')):
                ids_total[idl.get('id')].append(idl.get('title'))
                cursor.execute('''INSERT INTO xref(type, name, title, idxref)
                  VALUES(?,?,?,?)''', (idl.tag,idl.get('title'), "", idl.get('id')))
            if (idl.get('name')):
                ids_total[idl.get('id')].append(idl.get('name'))
                cursor.execute('''INSERT INTO xref(type, name, title, idxref)
                  VALUES(?,?,?,?)''', (idl.tag,"", idl.get('name'), idl.get('id')))
            else:
                if not (ids_total[idl.get('id')]):
                    ids_total[idl.get('id')].append(idl.get('id'))
                    cursor.execute('''INSERT INTO xref(type, name, title, idxref)
                  VALUES(?,?,?,?)''', (idl.tag,"", "", idl.get('id')))

    db.commit()

    # -------------------------------------------------------------------------------------
    # XML path of all elements in order to get all the information needed into dicts
    # -------------------------------------------------------------------------------------

    print ((colored("[+] Parsing file "+results.XMLfile, 'white')))

    for element in root:
        n += 1
        c1 += 1
        child1_total.setdefault(str(c1), [])
        child1_total[str(c1)].append(element.tag)
        child1_total[str(c1)].append(element.attrib)
        if (element.get('title')):
            chapter_child1_title = element.get('title')
        if (element.get('name')):
            chapter_child1_title = element.get('name')

        for child1_tags in element.findall('./'):
            c2 += 1
            child2_total.setdefault(str(c2), []) # ID
            child2_total[str(c2)].append(child1_tags.tag) # Tag
            child2_total[str(c2)].append(c1) # Parent
            child2_total[str(c2)].append(child1_tags.attrib) # Attributes
            paratext=elements_parser_all(child1_tags, ids_total, chapter_child1_title) # Text
            child2_total[str(c2)].append(paratext) # Test

            for child2_tags in child1_tags.findall('./'):
                c3 += 1
                child3_total.setdefault(str(c3), [])
                child3_total[str(c3)].append(child2_tags.tag)
                child3_total[str(c3)].append(c2)
                child3_total[str(c3)].append(child2_tags.attrib)
                paratext=elements_parser_all(child2_tags, ids_total, chapter_child1_title) 
                child3_total[str(c3)].append(paratext)

                for child3_tags in child2_tags.findall('./'):
                    c4 += 1
                    child4_total.setdefault(str(c4), [])
                    child4_total[str(c4)].append(child3_tags.tag)
                    child4_total[str(c4)].append(c3)
                    child4_total[str(c4)].append(child3_tags.attrib)
                    paratext=elements_parser_all(child3_tags, ids_total, chapter_child1_title) 
                    child4_total[str(c4)].append(paratext)

                    for child4_tags in child3_tags.findall('./'):
                        c5 += 1
                        child5_total.setdefault(str(c5), [])
                        child5_total[str(c5)].append(child4_tags.tag)
                        child5_total[str(c5)].append(c4)
                        child5_total[str(c5)].append(child4_tags.attrib)
                        paratext=elements_parser_all(child4_tags, ids_total, chapter_child1_title) 
                        child5_total[str(c5)].append(paratext)

                        for child5_tags in child4_tags.findall('./'):
                            c6 += 1
                            child6_total.setdefault(str(c6), [])
                            child6_total[str(c6)].append(child5_tags.tag)
                            child6_total[str(c6)].append(c5)
                            child6_total[str(c6)].append(child5_tags.attrib)
                            paratext=elements_parser_all(child5_tags, ids_total, chapter_child1_title) 
                            child6_total[str(c6)].append(paratext)

                            for child6_tags in child5_tags.findall('./'):
                                c7 += 1
                                child7_total.setdefault(str(c7), [])
                                child7_total[str(c7)].append(child6_tags.tag)
                                child7_total[str(c7)].append(c6)
                                child7_total[str(c7)].append(child6_tags.attrib)
                                paratext=elements_parser_all(child6_tags, ids_total, chapter_child1_title)
                                child7_total[str(c7)].append(paratext)

                                for child7_tags in child6_tags.findall('./'):
                                    c8 += 1
                                    child8_total.setdefault(str(c8), [])
                                    child8_total[str(c8)].append(child7_tags.tag)
                                    child8_total[str(c8)].append(c7)
                                    child8_total[str(c8)].append(child7_tags.attrib)
                                    paratext=elements_parser_all(child7_tags, ids_total, chapter_child1_title) 
                                    child8_total[str(c8)].append(paratext)

                                    for child8_tags in child7_tags.findall('./'):
                                        c9 += 1
                                        child9_total.setdefault(str(c9), [])
                                        child9_total[str(c9)].append(child8_tags.tag)
                                        child9_total[str(c9)].append(c8)
                                        child9_total[str(c9)].append(child8_tags.attrib)
                                        paratext=elements_parser_all(child8_tags, ids_total, chapter_child1_title) 
                                        child9_total[str(c9)].append(paratext)

                                        for child9_tags in child8_tags.findall('./'):
                                            c10 += 1
                                            child10_total.setdefault(str(c10), [])
                                            child10_total[str(c10)].append(child9_tags.tag)
                                            child10_total[str(c10)].append(c9)
                                            child10_total[str(c10)].append(child9_tags.attrib)
                                            paratext=elements_parser_all(child9_tags, ids_total, chapter_child1_title) 
                                            child10_total[str(c10)].append(paratext)


	#------------------------------------------------------------------------------
	# Insert information parsed into Database
	#------------------------------------------------------------------------------

    #########################################################################################
    #child1 unique elements:
    #Parent: eal
    #Parent: clause
    #Parent: cap
    #Parent: patchinfo
    #Parent: a-class
    #Parent: f-class
    #########################################################################################

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child1(id INTEGER PRIMARY KEY, element TEXT, attributetype TEXT,
                            category TEXT, type TEXT, idelement TEXT, title TEXT, name TEXT,
                            orderdoc INTEGER, cc1 INTEGER, cc2 INTEGER, cc3 INTEGER, cem INTEGER)
    ''')

    for attribute, value in child1_total.items():
        name = category = typeelement = title = idelement = key = doc = order = ""
        keyposition = '{}'.format(attribute) # position/key
        if (keyposition=="79"): continue # forward patchinfo
        i = iter(value)
        element = i.next() # element (eal, clause, cap, patchinfo, a-class, f-class)
        attributeselement = i.next() # attributes element ie: (category, type, id, title)
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            if key == "name": name = '{}'.format(valueelement)
            if key == "category": category = '{}'.format(valueelement)
            if key == "type": typeelement = '{}'.format(valueelement)
            if key == "id": idelement = '{}'.format(valueelement)
            if key == "title": title = '{}'.format(valueelement)
            if (title):
                chapter, cc1, cc2, cc3, cem = functions().cc_chapter_order(keyposition)
            elif (name):
                chapter, cc1, cc2, cc3, cem = functions().cc_chapter_order(keyposition)
        cursor.execute('''INSERT INTO child1(id, element, attributetype, category, type,
                                             idelement, title, name, orderdoc, cc1, cc2, cc3, cem)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), element, key, category,
                          typeelement, idelement, title, name, chapter, cc1, cc2, cc3, cem))
    db.commit()

    
    #########################################################################################
    #child2 unique elements:
    #|- ac-application-notes
    #|- figure: <figure entity="clause/graphics/ACO-interact-1.png" width="textwidth" height="!" title="Base component abstraction" id="aco-interact-1"/>
    #|- ma-introduction
    #|- cap-objectives
    #|- table: <table id="ap_rating">
    #|- ma-application-notes
    #|- glossentry: <glossentry id="activity">
    #|- eal-objectives
    #|- cap-component: <cap-component acomponent="ase_ccl.1"/> 
    #|- f-family: <f-family name="Security audit automatic response" id="fau_arp">
    #|- fc-introduction
    #|- ma-objectives
    #|- para: <para type="normal"> --> text
    #|- acronym: <acronym id="cem">
    #|- cap-assurance-components
    #|- biblioentry: <biblioentry id="a-cc-p1">
    #|- ac-introduction
    #|- fc-informative-notes
    #|- ac-overview
    #|- a-family: <a-family name="Composition rationale" id="aco_cor">
    #|- eal-component: <eal-component acomponent="ase_ccl.1"/> 
    #|- subclause: <subclause title="Organisation of CC Part 3" id="assurance-scope-organisation">
    #|- eal-assurance-components
    #########################################################################################

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child2(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, idelement TEXT, title TEXT, name TEXT, paratext TEXT, entity TEXT,
                            width TEXT, height TEXT, acomponent TEXT, FOREIGN KEY(parentkey) REFERENCES root(id))
    ''')

    for attribute, value in child2_total.items():
        name = typeelement = title = idelement = entity = width = height = acomponent = key = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (ac-application-notes, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'id': 'aco-definitions', 'title': 'Terms and definitions related to the ACO class'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "entity": entity = '{}'.format(value)
            if key == "width": width = '{}'.format(value)
            if key == "height": height = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "name": name = '{}'.format(value)
            if key == "acomponent": acomponent = '{}'.format(value)

        cursor.execute('''INSERT INTO child2(id, parentkey, element, attributetype, type, entity, width, 
                        height, idelement, title, name, acomponent, paratext)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element,
                        key, typeelement, entity, width, height, idelement, title, name, acomponent, text))
    db.commit()


    #########################################################################################
    #child3 unique elements:
    #|-- biblioterm: --> text
    #|-- figure: <figure entity="clause/graphics/ACO-interact-1.png" width="textwidth" height="!" title="Base component abstraction" id="aco-interact-1"/>
    #|-- af-levelling-criteria
    #|-- acronymterm: --> text
    #|-- bibliodef: --> text
    #|-- f-component: <f-component name="Security alarms" id="fau_arp.1">
    #|-- acronymdef: --> text
    #|-- af-objectives
    #|-- table: <table id="table-pp-assurance">
    #|-- glossentry: <glossentry id="action">
    #|-- xref: <xref id="alc_tat.1-2" show="link"/>
    #|-- ff-evaluator-notes
    #|-- title: --> text
    #|-- ff-behaviour
    #|-- af-overview
    #|-- bold: --> text
    #|-- para: <para type="normal"> --> text
    #|-- tgroup: <tgroup cols="7">
    #|-- biblioentry: <biblioentry id="cem-cc">
    #|-- glossdef: --> text
    #|-- glossnote: --> text
    #|-- a-component: <a-component name="Composition rationale" id="aco_cor.1">
    #|-- glossterm: --> text
    #|-- list: <list type="enumerated"> or <list type="itemized">
    #|-- af-application-notes
    #|-- ff-user-notes
    #|-- subclause: <subclause title="Guidance" id="aco_cor_1_guidance">
    #########################################################################################

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child3(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, entity TEXT, show TEXT, cols TEXT,
                            width TEXT, height TEXT, idelement TEXT, title TEXT, name TEXT,
                            FOREIGN KEY(parentkey) REFERENCES child2(id))
    ''')

    for attribute, value in child3_total.items():
        name = category = typeelement = title = idelement = key = entity = width = height = show = cols = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "entity": entity = '{}'.format(value)
            if key == "width": width = '{}'.format(value)
            if key == "height": height = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "name": name = '{}'.format(value)
            if key == "show": show = '{}'.format(value)
            if key == "cols": cols = '{}'.format(value)

        cursor.execute('''INSERT INTO child3(id, parentkey, element, attributetype, type, entity, width, 
                        height, idelement, title, name, paratext, show, cols)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element,
                        key, typeelement, entity, width, height, idelement, title, name, text, show, cols))
    db.commit()



    #########################################################################################
    #child4 unique elements:
    #|--- biblioterm: --> text
    #|--- figure: <figure entity="clause/graphics/ACO-interact-1.png" width="textwidth" height="!" title="Base component abstraction" id="aco-interact-1"/>
    #|--- msa-objectives
    #|--- bibliodef: --> text
    #|--- fco-rationale
    #|--- table: <table id="table-pp-assurance"> or <table id="TDS-summary-table" width="100%">
    #|--- aco-hierarchical: <aco-hierarchical acomponent="aco_dev.1"/>
    #|--- xref: <xref id="adv_tds.1" show="link"/>
    #|--- ae-content: <ae-content id="aco_dev.3.1c">
    #|--- title: --> text
    #|--- f-element: <f-element id="fau_arp.1.1">
    #|--- tbody
    #|--- fco-management: --> text
    #|--- fco-user-notes
    #|--- msa-input
    #|--- italic: --> text
    #|--- ae-developer: <ae-developer id="aco_cor.1.1d">
    #|--- msa-application-notes
    #|--- thead
    #|--- fco-evaluator-notes
    #|--- bold: --> text
    #|--- para: <para type="normal"> --> text
    #|--- aco-objectives
    #|--- tgroup: <tgroup cols="4">
    #|--- fco-levelling
    #|--- glossdef: --> text
    #|--- glosssource: --> text_xref
    #|--- glossnote: --> text
    #|--- aco-dependsoncomponent: <aco-dependsoncomponent acomponent="aco_dev.1"/>
    #|--- glossterm: --> text
    #|--- equation: <equation entity="clause/equations/cem2_anb-1.png"/>
    #|--- aco-application-notes
    #|--- list: <list type="enumerated"> or <list type="itemized">
    #|--- fco-hierarchical: <fco-hierarchical fcomponent="fau_saa.3"/>
    #|--- fco-audit: <fco-audit level="minimal" equal="fau_saa.1"/>
    #|--- item: <item id="pgfId-853191">
    #|--- fco-dependencies: text_<fco-dependsoncomponent fcomponent="fau_sar.1"/>
    #|--- ae-evaluator: <ae-evaluator id="aco_cor.1.1e">
    #|--- glossalt: --> text
    #|--- subclause: <subclause title="Guidance" id="aco_cor_1_guidance">
    #########################################################################################

    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child4(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                         type TEXT, paratext TEXT, entity TEXT, width TEXT, height TEXT,
                           idelement TEXT, title TEXT, name TEXT, acomponent TEXT, fcomponent TEXT,
                           level TEXT, equal TEXT, 
                          FOREIGN KEY(parentkey) REFERENCES child3(id))
    ''')

    for attribute, value in child4_total.items():
        name = category = typeelement = title = idelement = key = entity = width = height = acomponent = fcomponent = level = equal = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "entity": entity = '{}'.format(value)
            if key == "width": width = '{}'.format(value)
            if key == "height": height = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "name": name = '{}'.format(value)
            if key == "acomponent": acomponent = '{}'.format(value)
            if key == "fcomponent": fcomponent = '{}'.format(value)
            if key == "level": level = '{}'.format(value)
            if key == "equal": equal = '{}'.format(value)

        cursor.execute('''INSERT INTO child4(id, parentkey, element, attributetype, type, entity, width, 
                          height, idelement, title, name, paratext, acomponent, fcomponent, level, equal)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent),
                          element, key, typeelement, entity, width, height, idelement, title, name,
                          text, acomponent, fcomponent, level, equal))
    db.commit()


    #########################################################################################
    #child5 unique elements:
    #|---- assignment: --> text
    #|---- xref: <xref id="adv_tds.1" show="link"/>
    #|---- figure: <figure entity="clause/graphics/ACO-interact-1.png" width="textwidth" height="!" title="Base component abstraction" id="aco-interact-1"/>
    #|---- para: --> text
    #|---- title: --> text
    #|---- row
    #|---- fco-dependsoncomponent: <fco-dependsoncomponent fcomponent="fau_saa.1"/>
    #|---- list: <list type="enumerated"> or <list type="itemized">
    #|---- tbody
    #|---- fe-selection: <fe-selection exclusive="YES"> or <fe-selection exclusive="NO">
    #|---- item: <item id="pgfId-853191">
    #|---- tgroup: <tgroup cols="4">
    #|---- italic: --> text
    #|---- fe-list
    #|---- fco-or
    #|---- table: <table id="table-pp-assurance"> or <table id="TDS-summary-table" width="100%">
    #|---- fe-assignment
    #|---- thead
    #|---- subclause: <subclause title="Guidance" id="aco_cor_1_guidance">
    #|---- m-workunit
    #|---- bold: --> text
    #########################################################################################


    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child5(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, entity TEXT, width TEXT, height TEXT,
                            idelement TEXT, title TEXT, name TEXT, fcomponent TEXT, cols TEXT,
                            exclusive TEXT, FOREIGN KEY(parentkey) REFERENCES child4(id))
    ''')

    for attribute, value in child5_total.items():
        name = category = typeelement = title = idelement = key = entity = width = height = fcomponent = cols = exclusive = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "entity": entity = '{}'.format(value)
            if key == "width": width = '{}'.format(value)
            if key == "height": height = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "name": name = '{}'.format(value)
            if key == "fcomponent": fcomponent = '{}'.format(value)
            if key == "cols": cols = '{}'.format(value)
            if key == "exclusive": exclusive = '{}'.format(value)

        cursor.execute('''INSERT INTO child5(id, parentkey, element, attributetype, type, entity, width, 
                          height, idelement, title, name, paratext, fcomponent, cols, exclusive)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent),
                          element, key, typeelement, entity, width, height, idelement, title, name,
                          text, fcomponent, cols, exclusive))
    db.commit()

    #########################################################################################
    #child6 unique elements:
    #|----- fe-assignmentnotes
    #|----- row
    #|----- fe-selectionnotes
    #|----- xref: <xref id="fau_gen.1.1b" show="link"/>
    #|----- ae-dc-element: <ae-dc-element id="aco_cor.1.1c"/>
    #|----- title: --> text
    #|----- tbody
    #|----- italic: --> text
    #|----- fe-item: --> text
    #|----- fco-dependsoncomponent: <fco-dependsoncomponent fcomponent="fau_gen.1"/>
    #|----- fe-assignmentitem: --> text
    #|----- bold: --> text
    #|----- para: --> text
    #|----- tgroup: <tgroup cols="4">
    #|----- url: <url id="http://vl.zuser.org/"/>
    #|----- equation: <equation entity="clause/equations/cem2_anb-1.png"/>
    #|----- list: <list type="enumerated"> or <list type="itemized">
    #|----- item: <item id="pgfId-853191">
    #|----- fe-selectionitem: --> text
    #|----- entry: <entry rowspan="2" align="center" style="mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;text-align:center"> or <entry style="font-size:10.0pt" columnspan="3" align="center">TSF Module</entry>
    #|----- thead
    #|----- subclause: <subclause title="Guidance" id="aco_cor_1_guidance">
    #########################################################################################


    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child6(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, idelement TEXT, title TEXT, entity TEXT,
                            fcomponent TEXT, cols TEXT, show TEXT, rowspan TEXT, columnspan TEXT, align TEXT, style TEXT,
                            FOREIGN KEY(parentkey) REFERENCES child5(id))
    ''')

    for attribute, value in child6_total.items():
        name = category = typeelement = title = idelement = key = entity = rowspan = columnspan = align = style = fcomponent = cols = show = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "entity": entity = '{}'.format(value)
            if key == "rowspan": rowspan = '{}'.format(value)
            if key == "columnspan": columnspan = '{}'.format(value)
            if key == "align": align = '{}'.format(value)
            if key == "style": style = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "fcomponent": fcomponent = '{}'.format(value)
            if key == "cols": cols = '{}'.format(value)
            if key == "show": show = '{}'.format(value)

        cursor.execute('''INSERT INTO child6(id, parentkey, element, attributetype, type, entity, rowspan, columnspan,
                          align, style, idelement, title, paratext, fcomponent, cols, show)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent),
                          element, key, typeelement, entity, rowspan, columnspan, align, style, idelement, title,
                          text, fcomponent, cols, show))
    db.commit()


    #########################################################################################
    #child7 unique elements:
    #|------ xref: <xref id="fau_gen.1.1b" show="link"/>
    #|------ bold: --> text
    #|------ para: --> text
    #|------ list: <list type="enumerated"> or <list type="itemized">
    #|------ tbody
    #|------ fe-selection: <fe-selection exclusive="YES"> or <fe-selection exclusive="NO">
    #|------ item: <item id="pgfId-853191">
    #|------ italic: --> text
    #|------ entry: <entry rowspan="2" align="center" style="mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;text-align:center"> or <entry style="font-size:10.0pt" columnspan="3" align="center">TSF Module</entry>
    #|------ fe-assignment
    #|------ thead
    #|------ subclause: <subclause title="Guidance" id="aco_cor_1_guidance">
    #|------ row
    #########################################################################################


    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child7(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, idelement TEXT, title TEXT, exclusive TEXT,
                            show TEXT, rowspan TEXT, columnspan TEXT, align TEXT, style TEXT,
                            FOREIGN KEY(parentkey) REFERENCES child6(id))
    ''')

    for attribute, value in child7_total.items():
        name = category = typeelement = title = idelement = key = entity = rowspan = columnspan = align = style = fcomponent = cols = show = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "exclusive": exclusive = '{}'.format(value)
            if key == "rowspan": rowspan = '{}'.format(value)
            if key == "columnspan": columnspan = '{}'.format(value)
            if key == "align": align = '{}'.format(value)
            if key == "style": style = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "show": show = '{}'.format(value)

        cursor.execute('''INSERT INTO child7(id, parentkey, element, attributetype, type, exclusive, rowspan, columnspan,
                          align, style, idelement, title, paratext, show)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element,
                          key, typeelement, exclusive, rowspan, columnspan, align, style, idelement, title, text, show))
    db.commit()

    #########################################################################################
    #child8 unique elements:
    #|------- fe-selectionnotes
    #|------- xref: <xref id="fau_gen.1.1b" show="link"/>
    #|------- bold: --> text
    #|------- para: --> text
    #|------- list: <list type="enumerated"> or <list type="itemized">
    #|------- item: <item id="pgfId-853191">
    #|------- italic: --> text
    #|------- fe-selectionitem: --> text
    #|------- fe-assignmentnotes
    #|------- entry: <entry rowspan="2" align="center" style="mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;text-align:center"> or <entry style="font-size:10.0pt" columnspan="3" align="center">TSF Module</entry>
    #|------- fe-assignmentitem
    #|------- row
    #########################################################################################


    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child8(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                         type TEXT, paratext TEXT, idelement TEXT, title TEXT, show TEXT, rowspan TEXT,
                         columnspan TEXT, align TEXT, style TEXT, FOREIGN KEY(parentkey) REFERENCES child7(id))
    ''')

    for attribute, value in child8_total.items():
        name = category = typeelement = title = idelement = key = rowspan = columnspan = align = style = show = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "rowspan": rowspan = '{}'.format(value)
            if key == "columnspan": columnspan = '{}'.format(value)
            if key == "align": align = '{}'.format(value)
            if key == "style": style = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "show": show = '{}'.format(value)

        cursor.execute('''INSERT INTO child8(id, parentkey, element, attributetype, type, rowspan, columnspan, 
                          align, style, idelement, title, paratext, show)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element,
                          key, typeelement, rowspan, columnspan, align, style, idelement, title, text, show))
    db.commit()

    #########################################################################################
    #child9 unique elements:
    #|-------- xref: <xref id="fau_gen.1.1b" show="link"/>
    #|-------- bold: --> text
    #|-------- para: --> text
    #|-------- footnote: --> text
    #|-------- list: <list type="enumerated"> or <list type="itemized">
    #|-------- item: <item id="pgfId-853191">
    #|-------- italic: --> text
    #|-------- entry: <entry rowspan="2" align="center" style="mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;text-align:center"> or <entry style="font-size:10.0pt" columnspan="3" align="center">TSF Module</entry>
    #########################################################################################



    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child9(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, idelement TEXT, title TEXT,
                            show TEXT, rowspan TEXT, columnspan TEXT, align TEXT, style TEXT,
                            FOREIGN KEY(parentkey) REFERENCES child8(id))
    ''')

    for attribute, value in child9_total.items():
        name = category = typeelement = title = idelement = key = rowspan = columnspan = align = style = show = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "rowspan": rowspan = '{}'.format(value)
            if key == "columnspan": columnspan = '{}'.format(value)
            if key == "align": align = '{}'.format(value)
            if key == "style": style = '{}'.format(value)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "title": title = '{}'.format(value)
            if key == "show": show = '{}'.format(value)

        cursor.execute('''INSERT INTO child9(id, parentkey, element, attributetype, type, rowspan, columnspan,
                          align, style, idelement, title, paratext, show)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element,
                          key, typeelement, rowspan, columnspan, align, style, idelement, title, text, show))
    db.commit()


    #########################################################################################
    #child10 unique elements:
    #|--------- footnote: --> text
    #|--------- item: <item id="pgfId-853191">
    #|--------- xref: <xref id="fau_gen.1.1b" show="link"/>
    #|--------- bold: --> text
    #|--------- italic: --> text
    #########################################################################################


    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE child10(id INTEGER PRIMARY KEY, parentkey INTEGER, element TEXT, attributetype TEXT,
                            type TEXT, paratext TEXT, idelement TEXT, show TEXT,
                            FOREIGN KEY(parentkey) REFERENCES child9(id))
    ''')

    for attribute, value in child10_total.items():
        name = category = typeelement = title = idelement = key = rowspan = align = style = show = ""
        keyposition = '{}'.format(attribute) # position/key
        i = iter(value)
        element = i.next() # element (biblioterm, figure, para, etc.)
        parent = i.next() # id parent
        attributeselement = i.next() # attributes element ej: {'name': 'Composition vulnerability review', 'id': 'aco_vul.1'}
        text = i.next() # Text
        for attributeselement, valueelement in attributeselement.items():
            key = '{}'.format(attributeselement)
            value =  '{}'.format(valueelement)
            if key == "type": typeelement = '{}'.format(value)
            if key == "id": idelement = '{}'.format(value)
            if key == "show": show = '{}'.format(value)

        cursor.execute('''INSERT INTO child10(id, parentkey, element, attributetype, type, 
                          idelement, paratext, show)
                          VALUES(?,?,?,?,?,?,?,?)''', (int(keyposition), int(parent), element, key,
                          typeelement, idelement, text, show))
    db.commit()

    print os.linesep + ((colored("[+] DONE", 'green'))) + os.linesep

    # Press ENTER to continue
    if (results.ask):
        python2 = sys.version_info[0] == 2
        if python2:
            raw_input("Press ENTER to continue")
        else:
            input("Press ENTER to continue")
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    if CCParser.failure:
        sys.exit(1)
