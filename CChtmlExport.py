#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """

CChtmlExport

Author: https://twitter.com/1_mod_m/

Project site: https://github.com/1modm

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
from datetime import datetime
import sqlite3
import shutil
from thirdparty.color.termcolor import colored

#------------------------------------------------------------------------------
# Plugins
#------------------------------------------------------------------------------
from lib.htmloutput import htmlaudit, htmlend, htmllast, create_html_file,\
                           create_blank_html_file, htmldatadashboard,\
                           htmldatadashboardjs, htmldashboardend
from lib.txtoutput import create_txt_file
from lib.output import print_results, print_titles, print_results_list, print_results_item,\
                         print_results_list_end, print_titles_subclase, print_results_figure,\
                         print_results_table, print_results_table_end, print_results_rowth, print_results_rowtd,\
                         print_results_tr, print_results_tr_end, print_results_aclass, print_titles_aclass,\
                         print_results_list_aclass, print_results_item_aclass, print_results_list_end_aclass,\
                         print_results_list_aclass_child6, print_results_item_aclass_child6, print_results_list_end_aclass_child6,\
                         print_results_list_aclass_child7, print_results_item_aclass_child7, print_results_list_end_aclass_child7,\
                         print_results_aclass_child4, print_results_aclass_child5

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
        description='Example: python %(prog)s data/ccdb.sqlite3', version='CChtmlExport 0.1',
        usage="python %(prog)s [OPTIONS]")

    # Mandatory
    parser.add_argument('database', action="store")
    parser.add_argument('-ask', action='store_true', default=False, dest='ask')
    
    return parser



###############################################################################
#------------------------------------------------------------------------------
# Class DatabaseManager
#------------------------------------------------------------------------------
###############################################################################

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()


###############################################################################
#------------------------------------------------------------------------------
# Class Iterate
#------------------------------------------------------------------------------
###############################################################################

class Iterate(object):

    def search(self, row, filenamedb, cc1, cc2, cc3, cem, outputdirectory):

        ParseChildSearch = ParseChild()

        dbmgr1 = DatabaseManager(filenamedb)
        dbmgr2 = DatabaseManager(filenamedb)
        dbmgr3 = DatabaseManager(filenamedb)
        dbmgr4 = DatabaseManager(filenamedb)
        dbmgr5 = DatabaseManager(filenamedb)
        dbmgr6 = DatabaseManager(filenamedb)
        dbmgr7 = DatabaseManager(filenamedb)
        dbmgr8 = DatabaseManager(filenamedb)
        dbmgr9 = DatabaseManager(filenamedb)
        dbmgr10 = DatabaseManager(filenamedb)
        dbmgrbiblioentry = DatabaseManager(filenamedb)
        dbmgrpara1 = DatabaseManager(filenamedb)
        dbmgrpara2 = DatabaseManager(filenamedb)
        dbmgrpara3 = DatabaseManager(filenamedb)
        dbmgrpara4 = DatabaseManager(filenamedb)
        dbmgritem = DatabaseManager(filenamedb)
        dbmgrlist= DatabaseManager(filenamedb)

        child2_query = 'SELECT id, parentkey, idelement, title, name, paratext, element, entity, width, height FROM child2 WHERE parentkey = '+str(row[0]) +' ORDER BY id'
        for row2 in dbmgr2.query(child2_query):
            ParseChildSearch.child2_to_html(row[3], dbmgrbiblioentry, dbmgrpara1, row2, cc1, cc2, cc3, cem, outputdirectory)

            child3_query = 'SELECT id, parentkey, idelement, title, name, paratext, element, entity, width, height FROM child3 WHERE parentkey = '+str(row2[0])+' ORDER BY id'
            for row3 in dbmgr3.query(child3_query):
                ParseChildSearch.child3_to_html(row[3], row2[6], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row3,cc1, cc2, cc3, cem, outputdirectory)

                child4_query = 'SELECT id, parentkey, idelement, title, name, paratext, element, entity, width, height FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
                for row4 in dbmgr4.query(child4_query):
                    ParseChildSearch.child4_to_html(row[3], row2[6], row3[6], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row4, cc1, cc2, cc3, cem, outputdirectory)

                    child5_query = 'SELECT id, parentkey, idelement, title, name, paratext, element, entity, width, height FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
                    for row5 in dbmgr5.query(child5_query):
                        ParseChildSearch.child5_to_html(row[3], row2[6], row3[6], row4[6], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row5, cc1, cc2, cc3, cem, outputdirectory)

                        child6_query = 'SELECT id, parentkey, idelement, title, paratext, element, entity FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
                        for row6 in dbmgr6.query(child6_query):
                            ParseChildSearch.child6_to_html(row[3], row2[6], row3[6], row4[6], row5[5], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row6, cc1, cc2, cc3, cem, outputdirectory)

                            child7_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(row6[0])+' ORDER BY id'
                            for row7 in dbmgr7.query(child7_query):
                                ParseChildSearch.child7_to_html(row[3], row2[6], row3[6], row4[6], row5[5], row6[5], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row7, cc1, cc2, cc3, cem, outputdirectory)

                                child8_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(row7[0])+' ORDER BY id'
                                for row8 in dbmgr8.query(child8_query):
                                    ParseChildSearch.child8_to_html(row[3], row2[6], row3[6], row4[6], row5[5], row6[5], row7[5], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row8, cc1, cc2, cc3, cem, outputdirectory)
                                    
                                    child9_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(row8[0])+' ORDER BY id'
                                    for row9 in dbmgr9.query(child9_query):
                                        ParseChildSearch.child9_to_html(row[3], row2[6], row3[6], row4[6], row5[5], row6[5], row7[5], row8[5],dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row9, cc1, cc2, cc3, cem, outputdirectory)

                                        child10_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(row9[0])+' ORDER BY id'
                                        for row10 in dbmgr10.query(child10_query):
                                            ParseChildSearch.child10_to_html(row[3], row2[6], row3[6], row4[6], row5[5], row6[5], row7[5], row8[5], row9[4], dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row10, cc1, cc2, cc3, cem, outputdirectory)
                

###############################################################################
#------------------------------------------------------------------------------
# Class ParseChild
#------------------------------------------------------------------------------
###############################################################################

class ParseChild(object):

    def child1_to_html(self, rowquery, cc1, cc2, cc3, cem, outputdirectory):

        if (rowquery[1]):
            child1_title = str(rowquery[1])
        elif (rowquery[2]):
            child1_title = str(rowquery[2])
        else: 
            child1_title = str(rowquery[3])

        if ((rowquery[0]) == 69):
            child1_title = "Evaluation assurance level 1 (EAL1) - " + child1_title
        elif ((rowquery[0]) == 70):
            child1_title = "Evaluation assurance level 2 (EAL2) - " + child1_title
        elif ((rowquery[0]) == 71):
            child1_title = "Evaluation assurance level 3 (EAL3) - " + child1_title
        elif ((rowquery[0]) == 72):
            child1_title = "Evaluation assurance level 4 (EAL4) - " + child1_title
        elif ((rowquery[0]) == 73):
            child1_title = "Evaluation assurance level 5 (EAL5) - " + child1_title
        elif ((rowquery[0]) == 74):
            child1_title = "Evaluation assurance level 6 (EAL6) - " + child1_title
        elif ((rowquery[0]) == 75):
            child1_title = "Evaluation assurance level 7 (EAL7) - " + child1_title
        elif ((rowquery[0]) == 76):
            child1_title = "Composition assurance level A (CAP-A) - " + child1_title
        elif ((rowquery[0]) == 77):
            child1_title = "Composition assurance level B (CAP-B) - " + child1_title
        elif ((rowquery[0]) == 78):
            child1_title = "Composition assurance level C (CAP-C) - " + child1_title
        elif ((rowquery[0]) == 65):
            child1_title = "Class APE: " + child1_title
        elif ((rowquery[0]) == 66):
            child1_title = "Class ASE: " + child1_title
        elif ((rowquery[0]) == 62):
            child1_title = "Class ADV: " + child1_title
        elif ((rowquery[0]) == 63):
            child1_title = "Class AGD: " + child1_title
        elif ((rowquery[0]) == 64):
            child1_title = "Class ALC: " + child1_title
        elif ((rowquery[0]) == 67):
            child1_title = "Class ATE: " + child1_title
        elif ((rowquery[0]) == 68):
            child1_title = "Class AVA: " + child1_title
        elif ((rowquery[0]) == 61):
            child1_title = "Class ACO: " + child1_title
        elif ((rowquery[0]) == 7):
            child1_title = "ANNEX A: " + child1_title
        elif ((rowquery[0]) == 6):
            child1_title = "ANNEX B: " + child1_title
        elif ((rowquery[0]) == 50):
            child1_title = "CLASS FAU: " + child1_title
        elif ((rowquery[0]) == 51):
            child1_title = "CLASS FCO: " + child1_title
        elif ((rowquery[0]) == 52):
            child1_title = "CLASS FCS: " + child1_title
        elif ((rowquery[0]) == 53):
            child1_title = "CLASS FDP: " + child1_title
        elif ((rowquery[0]) == 54):
            child1_title = "CLASS FIA: " + child1_title
        elif ((rowquery[0]) == 55):
            child1_title = "CLASS FMT: " + child1_title
        elif ((rowquery[0]) == 56):
            child1_title = "CLASS FPR: " + child1_title
        elif ((rowquery[0]) == 57):
            child1_title = "CLASS FPT: " + child1_title
        elif ((rowquery[0]) == 58):
            child1_title = "CLASS FRU: " + child1_title
        elif ((rowquery[0]) == 59):
            child1_title = "CLASS FTA: " + child1_title
        elif ((rowquery[0]) == 60):
            child1_title = "CLASS FTP: " + child1_title
        elif ((rowquery[0]) == 22):
            child1_title = "ANNEX A: " + child1_title
        elif ((rowquery[0]) == 10):
            child1_title = "ANNEX B: " + child1_title

        print_titles(child1_title, "href", cc1, cc2, cc3, cem, outputdirectory)

                 
        return (child1_title)

    #------------------------------------------------------------------------------

    def child2_to_html(self, element1, dbmgrbiblioentry, dbmgrpara1, row2, cc1, cc2, cc3, cem, outputdirectory):

        if ((row2[6]) == "biblioentry"): # element
            child2_biblioentry_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child3 WHERE parentkey = '+str(row2[0])+' ORDER BY id'
            for row_biblioentry in dbmgrbiblioentry.query(child2_biblioentry_query):
                if ((row_biblioentry[6]) == "biblioterm"): # element
                    child2_biblioentry_text = (row_biblioentry[5]).encode('utf-8') # item
                    print_results(child2_biblioentry_text, cc1, cc2, cc3, cem, outputdirectory)
                if ((row_biblioentry[6]) == "bibliodef"): # element
                    child2_biblioentry_text = (row_biblioentry[5]).encode('utf-8') # item
                    print_results(child2_biblioentry_text, cc1, cc2, cc3, cem, outputdirectory)
                    
        elif ((row2[6]) == "item"): # element
            child2_text = ""
        elif ((row2[6]) == "xref"): # element
            child2_text = ""
        elif ((row2[6]) == "acronym"): # element
            child2_text = ""

        elif ((row2[6]) == "eal-component"): # element
            child2_text = (row2[5]).encode('utf-8') # acomponent
            print_results_item(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "cap-component"): # element
            child2_text = (row2[5]).encode('utf-8') # acomponent
            print_results_item(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "glossentry"): # element
            if ((row2[5]).encode('utf-8') != ""):
                child2_text = "<b> " + (row2[5]).encode('utf-8') + ": </b> "
                print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "glossterm"): # element
            child2_text = "<b> " + (row2[5]).encode('utf-8') + ": </b> "
            print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "glossdef"): # element
            child2_text = (row2[5]).encode('utf-8') # acomponent

            child3_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child3 WHERE parentkey = '+str(row2[0])+' ORDER BY id'
            for para_row_3 in dbmgrpara1.query(child3_para_query):
                if ((para_row_3[6]) == "bold"):
                    child2_text += "<b> " + (para_row_3[5]).encode('utf-8') + " </b>"
                if ((para_row_3[6]) == "italic"):
                    child2_text += "<i> " + (para_row_3[5]).encode('utf-8') + " </i>"
                if ((para_row_3[6]) == "xref"):
                    child2_text += (para_row_3[5]).encode('utf-8') # paratext

            print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "glossnote"): # element
            child2_text = (row2[5]).encode('utf-8') # acomponent
            print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "para"): # element
            child2_text = (row2[5]).encode('utf-8') # paratext
            
            child3_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child3 WHERE parentkey = '+str(row2[0])+' ORDER BY id'
            for para_row_3 in dbmgrpara1.query(child3_para_query):
                if ((para_row_3[6]) == "bold"):
                    child2_text += "<b> " + (para_row_3[5]).encode('utf-8') + " </b>"
                if ((para_row_3[6]) == "italic"):
                    child2_text += "<i> " + (para_row_3[5]).encode('utf-8') + " </i>"
                if ((para_row_3[6]) == "xref"):
                    child2_text += (para_row_3[5]).encode('utf-8') # paratext

            print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "figure"): # element
            figure_title = (row2[3]).encode('utf-8')
            figure_entity = (row2[7]).encode('utf-8')
            figure_width = (row2[8]).encode('utf-8')
            figure_height = (row2[9]).encode('utf-8')
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row2[6]) == "subclause"): # element
            child2_text = str(row2[3]) #title
            print_titles_subclase(child2_text, "href", cc1, cc2, cc3, cem, outputdirectory)
            
        elif (row2[3]):
            child2_text = str(row2[3]) #title
            print_titles(child2_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        elif (row2[4]):
            child2_text = str(row2[4]) #name
            print_titles(child2_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child2_text = str(row2[2])
            #print_results(child2_text, cc1, cc2, cc3, cem, outputdirectory)


    #------------------------------------------------------------------------------

    def child3_to_html(self, element1, element2, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row3, cc1, cc2, cc3, cem, outputdirectory):

        if ((row3[6]) == "item"): # element
            child3_text = ""

        elif ((row3[6]) == "a-component"): # element
            child3_text = "<b> Evaluation of sub-activity (" + (row3[5]).encode('utf-8') + ")</b> " 
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "glossentry"): # element
            if ((row3[5]).encode('utf-8') != ""):
                child3_text = "<b> " + (row3[5]).encode('utf-8') + ": </b> "
                print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "acronymterm"): # element
            child3_text = (row3[5]).encode('utf-8') 
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "acronymdef"): # element
            child3_text = (row3[5]).encode('utf-8') 
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "glossterm"): # element
            child3_text = "<b> " + (row3[5]).encode('utf-8') + ": </b> "
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "glossdef"): # element
            child3_text = (row3[5]).encode('utf-8') # acomponent
            child4_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for para_row_4 in dbmgrpara1.query(child4_para_query):
                if ((para_row_4[6]) == "bold"):
                    child3_text += "<b> " + (para_row_4[5]).encode('utf-8') + " </b>"
                if ((para_row_4[6]) == "italic"):
                    child3_text += "<i> " + (para_row_4[5]).encode('utf-8') + " </i>"
                if ((para_row_4[6]) == "xref"):
                    child3_text += (para_row_4[5]).encode('utf-8') # paratext

            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (((row3[6]) == "glossnote") or ((row3[6]) == "glossalt") or ((row3[6]) == "glosssource")): # element
            child3_text = (row3[5]).encode('utf-8') # acomponent
            child4_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for para_row_4 in dbmgrpara1.query(child4_para_query):
                if ((para_row_4[6]) == "bold"):
                    child3_text += "<b> " + (para_row_4[5]).encode('utf-8') + " </b>"
                if ((para_row_4[6]) == "italic"):
                    child3_text += "<i> " + (para_row_4[5]).encode('utf-8') + " </i>"
                if ((para_row_4[6]) == "xref"):
                    child3_text += (para_row_4[5]).encode('utf-8') # paratext


                    child5_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child5 WHERE parentkey = '+str(para_row_4[0])+' ORDER BY id'
                    for para_row_5 in dbmgrpara2.query(child5_para_query):
                        if ((para_row_5[5]) == "bold"):
                            child3_text += "<b> " + (para_row_5[4]).encode('utf-8') + " </b>"
                        if ((para_row_5[5]) == "italic"):
                            child3_text += "<i> " + (para_row_5[4]).encode('utf-8') + " </i>"
                        if ((para_row_5[5]) == "xref"):
                            child3_text += (para_row_5[4]).encode('utf-8') # paratext   
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)


        elif ((row3[6]) == "table"): # element
            child3_text = ""
            print_results_table(cc1, cc2, cc3, cem, outputdirectory)
            #<table border="1">

            child4_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for para_row_4 in dbmgrpara1.query(child4_para_query):
                if ((para_row_4[6]) == "title"): # element
                    child3_text += (para_row_4[5]).encode('utf-8') # paratext
                    # TITLE

                if ((para_row_4[6]) == "tgroup"): # element
                    
                    child3_table_text = ""
                    child5_item_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child5 WHERE parentkey = '+str(para_row_4[0])+' ORDER BY id'
                    for para_item_5 in dbmgritem.query(child5_item_query):
                        if ((para_item_5[5]) == "thead"): # element
                            
                            child8_extra_row = 0
                            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(para_item_5[0])+' ORDER BY id'
                            for para_item_6 in dbmgrpara2.query(child6_para_query):
                                if ((para_item_6[5]) == "row"): # element
                                    #<tr>
                                    print_results_tr(cc1, cc2, cc3, cem, outputdirectory)
                                    if (child8_extra_row == 1 ):
                                        print_results_rowth("", "1", cc1, cc2, cc3, cem, outputdirectory)
                                        child8_extra_row = 0

                                    child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element, columnspan FROM child7 WHERE parentkey = '+str(para_item_6[0])+' ORDER BY id'
                                    for para_item_7 in dbmgrpara3.query(child7_para_query):
                                        columnspan = 1

                                        if ((para_item_7[5]) == "entry"): # element

                                            child7_text_row = ""
                                            child7_text_row += (para_item_7[4]).encode('utf-8') # paratext

                                            if (child7_text_row == ""): child8_extra_row = 1
                                            if ((para_item_7[6]).encode('utf-8')): columnspan = (para_item_7[6]).encode('utf-8')


                                            child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                                            for para_row_8 in dbmgrpara4.query(child8_para_query):
                                                if ((para_row_8[5]) == "bold"):
                                                    child7_text_row += "<b> " + (para_row_8[4]).encode('utf-8') + " </b>"
                                                if ((para_row_8[5]) == "italic"):
                                                    child7_text_row += "<i> " + (para_row_8[4]).encode('utf-8') + " </i>"
                                                if ((para_row_8[5]) == "xref"):
                                                    child7_text_row += (para_row_8[4]).encode('utf-8') # paratext   

                                        #<th>row</th>
                                        print_results_rowth(child7_text_row, columnspan, cc1, cc2, cc3, cem, outputdirectory)

                                    #</tr>
                                    print_results_tr_end(cc1, cc2, cc3, cem, outputdirectory)

                        if ((para_item_5[5]) == "tbody"): # element
                            
                            child3_table_text += (para_item_5[4]).encode('utf-8') # paratext

                            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(para_item_5[0])+' ORDER BY id'
                            for para_item_6 in dbmgrpara1.query(child6_para_query):
                                
                                if ((para_item_6[5]) == "row"): # element
                                    #<tr>
                                    print_results_tr(cc1, cc2, cc3, cem, outputdirectory)
                                    child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(para_item_6[0])+' ORDER BY id'
                                    for para_item_7 in dbmgrpara2.query(child7_para_query):
                                        if ((para_item_7[5]) == "entry"): # element
                                            child7_text_row = ""
                                            child7_text_row += (para_item_7[4]).encode('utf-8') # paratext
                                            child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                                            for para_row_8 in dbmgrpara3.query(child8_para_query):
                                                if ((para_row_8[5]) == "bold"):
                                                    child7_text_row += "<b> " + (para_row_8[4]).encode('utf-8') + " </b>"
                                                if ((para_row_8[5]) == "italic"):
                                                    child7_text_row += "<i> " + (para_row_8[4]).encode('utf-8') + " </i>"
                                                if ((para_row_8[5]) == "xref"):
                                                    child7_text_row += (para_row_8[4]).encode('utf-8') # paratext    
                                        #<td>row</td>
                                        print_results_rowtd(child7_text_row, cc1, cc2, cc3, cem, outputdirectory)
                                    #</tr>
                                    print_results_tr_end(cc1, cc2, cc3, cem, outputdirectory)
                

            print_results_table_end(cc1, cc2, cc3, cem, outputdirectory)

            # Imprimir titulo tabla
            print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)


        elif ((row3[6]) == "xref"): # element
            #child4_text = (row4[5]).encode('utf-8') # item
            child3_text = ""
            #print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "para"): # element
            child3_text = (row3[5]).encode('utf-8') # paratext

            child4_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for para_row_4 in dbmgrpara1.query(child4_para_query):
                if ((para_row_4[6]) == "bold"):
                    child3_text += "<b> " + (para_row_4[5]).encode('utf-8') + " </b>"
                if ((para_row_4[6]) == "italic"):
                    child3_text += "<i> " + (para_row_4[5]).encode('utf-8') + " </i>"
                if ((para_row_4[6]) == "xref"):
                    child3_text += (para_row_4[5]).encode('utf-8') # paratext

                if ((para_row_4[6]) == "italic" or (para_row_4[6]) == "bold" or (para_row_4[6]) == "xref"): # element
                    child5_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child5 WHERE parentkey = '+str(para_row_4[0])+' ORDER BY id'
                    for para_row_5 in dbmgrpara2.query(child5_para_query):
                        if ((para_row_5[5]) == "bold"):
                            child3_text += "<b> " + (para_row_5[4]).encode('utf-8') + " </b>"
                        if ((para_row_5[5]) == "italic"):
                            child3_text += "<i> " + (para_row_5[4]).encode('utf-8') + " </i>"
                        if ((para_row_5[5]) == "xref"):
                            child3_text += (para_row_5[4]).encode('utf-8') # paratext

            print_results_aclass(element1, element2, child3_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "figure"): # element
            figure_title = (row3[3]).encode('utf-8')
            figure_entity = (row3[7]).encode('utf-8')
            figure_width = (row3[8]).encode('utf-8')
            figure_height = (row3[9]).encode('utf-8')
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row3[6]) == "list"): # element
            print_results_list(cc1, cc2, cc3, cem, outputdirectory)
            child3_list_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for row33 in dbmgrlist.query(child3_list_query):
                if ((row33[6]) == "item"): # element
                    child3_list_text = (row33[5]).encode('utf-8') # item

                    child5_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row33[0])+' ORDER BY id'
                    for para_item_5 in dbmgrpara1.query(child5_para_query):
                        if ((para_item_5[6]) == "bold"):
                            child3_list_text += "<b> " + (para_item_5[5]).encode('utf-8') + " </b>"
                        if ((para_item_5[6]) == "italic"):
                            child3_list_text += "<i> " + (para_item_5[5]).encode('utf-8') + " </i>"
                        if ((para_item_5[6]) == "xref"):
                            child3_list_text += (para_item_5[5]).encode('utf-8') # paratext

                    print_results_item(child3_list_text, cc1, cc2, cc3, cem, outputdirectory)
            print_results_list_end(cc1, cc2, cc3, cem, outputdirectory)


        elif ((row3[6]) == "biblioentry"): # element
            child3_biblioentry_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child4 WHERE parentkey = '+str(row3[0])+' ORDER BY id'
            for row_biblioentry in dbmgrbiblioentry.query(child3_biblioentry_query):
                if ((row_biblioentry[6]) == "biblioterm"): # element
                    child3_biblioentry_text = (row_biblioentry[5]).encode('utf-8') # item
                    print_results(child3_biblioentry_text, cc1, cc2, cc3, cem, outputdirectory)
                if ((row_biblioentry[6]) == "bibliodef"): # element
                    child3_biblioentry_text = (row_biblioentry[5]).encode('utf-8') # item
                    print_results(child3_biblioentry_text, cc1, cc2, cc3, cem, outputdirectory)


        elif (row3[3]):
            child3_text = str(row3[3]) #title
            print_titles_aclass(element1, element2, child3_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        elif (row3[4]):
            child3_text = str(row3[4]) #name
            print_titles_aclass(element1, element2, child3_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child3_text = str(row3[2])
            #print_results(child3_text, cc1, cc2, cc3, cem, outputdirectory)


    #------------------------------------------------------------------------------

    def child4_to_html(self, element1, element2, element3, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row4, cc1, cc2, cc3, cem, outputdirectory):

        if ((row4[6]) == "item"): # element
            child4_text = ""
      
        elif ((row4[6]) == "acronymterm"): # element
            child4_text = (row4[5]).encode('utf-8') # acomponent
            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row4[6]) == "acronymterm"): # element
            child4_text = (row4[5]).encode('utf-8') # acomponent
            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row4[6]) == "glossentry"): # element
            if ((row4[5]).encode('utf-8') != ""):
                child4_text = "<b> " + (row4[5]).encode('utf-8') + ": </b> "
                print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row4[6]) == "glossterm"): # element
            child4_text = "<b> " + (row4[5]).encode('utf-8') + ": </b> "
            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row4[6]) == "glossdef"): # element
            child4_text = (row4[5]).encode('utf-8') # acomponent
            child5_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
            for para_row_5 in dbmgrpara2.query(child5_para_query):
                if ((para_row_5[6]) == "bold"):
                    child4_text += "<b> " + (para_row_5[5]).encode('utf-8') + " </b>"
                if ((para_row_5[6]) == "italic"):
                    child4_text += "<i> " + (para_row_5[5]).encode('utf-8') + " </i>"
                if ((para_row_5[6]) == "xref"):
                    child4_text += (para_row_5[5]).encode('utf-8') # paratext
            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (((row4[6]) == "glossnote") or ((row4[6]) == "glossalt") or ((row4[6]) == "glosssource")): # element
            child4_text = (row4[5]).encode('utf-8') # acomponent
            child5_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
            for para_row_5 in dbmgrpara2.query(child5_para_query):
                if ((para_row_5[6]) == "bold"):
                    child4_text += "<b> " + (para_row_5[5]).encode('utf-8') + " </b>"
                if ((para_row_5[6]) == "italic"):
                    child4_text += "<i> " + (para_row_5[5]).encode('utf-8') + " </i>"
                if ((para_row_5[6]) == "xref"):
                    child4_text += (para_row_5[5]).encode('utf-8') # paratext

                if ((para_row_5[6]) == "italic" or (para_row_5[6]) == "bold" or (para_row_5[6]) == "xref"): # element
                    child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(para_row_5[0])+' ORDER BY id'
                    for para_row_6 in dbmgrpara3.query(child6_para_query):
                        if ((para_row_6[5]) == "bold"):
                            child4_text += "<b> " + (para_row_6[4]).encode('utf-8') + " </b>"
                        if ((para_row_6[5]) == "italic"):
                            child4_text += "<i> " + (para_row_6[4]).encode('utf-8') + " </i>"
                        if ((para_row_6[5]) == "xref"):
                            child4_text += (para_row_6[4]).encode('utf-8') # paratext

            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)


        elif (((row4[6]) == "f-element")): # element
            child4_text = "<b> " + (row4[5]).encode('utf-8') + "</b> "


        elif ((row4[6]) == "table"): # element
            child4_text = ""
            print_results_table(cc1, cc2, cc3, cem, outputdirectory)
            #<table border="1">

            child5_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
            for para_row_5 in dbmgrpara1.query(child5_para_query):
                if ((para_row_5[6]) == "title"): # element
                    child4_text += (para_row_5[5]).encode('utf-8') # paratext
                    # TITULO TABLA

                if ((para_row_5[6]) == "tgroup"): # element
                    

                    child4_table_text = ""
                    child6_item_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(para_row_5[0])+' ORDER BY id'
                    for para_item_6 in dbmgritem.query(child6_item_query):
                        if ((para_item_6[5]) == "thead"): # element
                            
                            
                            child9_extra_row = 0
                            child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(para_item_6[0])+' ORDER BY id'
                            for para_item_7 in dbmgrpara2.query(child7_para_query):
                                if ((para_item_7[5]) == "row"): # element
                                    #<tr>
                                    print_results_tr(cc1, cc2, cc3, cem, outputdirectory)
                                    if (child9_extra_row == 1 ):
                                        print_results_rowth("", "1", cc1, cc2, cc3, cem, outputdirectory)
                                        child9_extra_row = 0

                                    child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element, columnspan FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                                    for para_item_8 in dbmgrpara3.query(child8_para_query):
                                        columnspan = 1

                                        if ((para_item_8[5]) == "entry"): # element

                                            child8_text_row = ""
                                            child8_text_row += (para_item_8[4]).encode('utf-8') # paratext

                                            if (child8_text_row == ""): child9_extra_row = 1
                                            if ((para_item_8[6]).encode('utf-8')): columnspan = (para_item_8[6]).encode('utf-8')


                                            child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(para_item_8[0])+' ORDER BY id'
                                            for para_row_9 in dbmgrpara4.query(child9_para_query):
                                                if ((para_row_9[5]) == "bold"):
                                                    child8_text_row += "<b> " + (para_row_9[4]).encode('utf-8') + " </b>"
                                                if ((para_row_9[5]) == "italic"):
                                                    child8_text_row += "<i> " + (para_row_9[4]).encode('utf-8') + " </i>"
                                                if ((para_row_9[5]) == "xref"):
                                                    child8_text_row += (para_row_9[4]).encode('utf-8') # paratext

                                        #<th>row</th>
                                        print_results_rowth(child8_text_row, columnspan, cc1, cc2, cc3, cem, outputdirectory)

                                    #</tr>
                                    print_results_tr_end(cc1, cc2, cc3, cem, outputdirectory)

                        if ((para_item_6[5]) == "tbody"): # element
                            
                            child4_table_text += (para_item_6[4]).encode('utf-8') # paratext

                            child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(para_item_6[0])+' ORDER BY id'
                            for para_item_7 in dbmgritem.query(child7_para_query):
                                
                                if ((para_item_7[5]) == "row"): # element
                                    #<tr>
                                    print_results_tr(cc1, cc2, cc3, cem, outputdirectory)
                                    child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                                    for para_item_8 in dbmgrpara1.query(child8_para_query):
                                        if ((para_item_8[5]) == "entry"): # element
                                            child8_text_row = ""
                                            child8_text_row += (para_item_8[4]).encode('utf-8') # paratext
                                            child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(para_item_8[0])+' ORDER BY id'
                                            for para_row_9 in dbmgrpara2.query(child9_para_query):
                                                if ((para_row_9[5]) == "bold"):
                                                    child8_text_row += "<b> " + (para_row_9[4]).encode('utf-8') + " </b>"
                                                if ((para_row_9[5]) == "italic"):
                                                    child8_text_row += "<i> " + (para_row_9[4]).encode('utf-8') + " </i>"
                                                if ((para_row_9[5]) == "xref"):
                                                    child8_text_row += (para_row_9[4]).encode('utf-8') # paratext
                                        #<td>row</td>
                                        print_results_rowtd(child8_text_row, cc1, cc2, cc3, cem, outputdirectory)
                                    #</tr>
                                    print_results_tr_end(cc1, cc2, cc3, cem, outputdirectory)
                

            print_results_table_end(cc1, cc2, cc3, cem, outputdirectory)
            print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)


        elif ((row4[6]) == "xref"): # element
            child4_text = ""

        elif ((row4[6]) == "para"): # element
            child4_text = (row4[5]).encode('utf-8') # paratext
            
            child5_para_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
            for para_row_5 in dbmgrpara2.query(child5_para_query):

                if ((para_row_5[6]) == "bold"):
                    child4_text += "<b> " + (para_row_5[5]).encode('utf-8') + " </b>"
                if ((para_row_5[6]) == "italic"):
                    child4_text += "<i> " + (para_row_5[5]).encode('utf-8') + " </i>"
                if ((para_row_5[6]) == "xref"):
                    child4_text += (para_row_5[5]).encode('utf-8') # paratext

                if ((para_row_5[6]) == "italic" or (para_row_5[6]) == "bold" or (para_row_5[6]) == "xref"): # element

                    child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(para_row_5[0])+' ORDER BY id'
                    for para_row_6 in dbmgrpara3.query(child6_para_query):
                        if ((para_row_6[5]) == "bold"):
                            child4_text += "<b> " + (para_row_6[4]).encode('utf-8') + " </b>"
                        if ((para_row_6[5]) == "italic"):
                            child4_text += "<i> " + (para_row_6[4]).encode('utf-8') + " </i>"
                        if ((para_row_6[5]) == "xref"):
                            child4_text += (para_row_6[4]).encode('utf-8') # paratext

            print_results_aclass_child4(element1, element2, element3, child4_text, cc1, cc2, cc3, cem, outputdirectory) # ase-app-reuse-pp2

        elif ((row4[6]) == "ae-developer"): # element
            child4_text = "<b>" + (row4[5]).encode('utf-8') + "</b>"
            print_results_aclass_child4(element1, element2, element3, child4_text, cc1, cc2, cc3, cem, outputdirectory) 


        elif ((row4[6]) == "ae-content"): # element
            child4_text = "<b>" + (row4[5]).encode('utf-8') + "</b>"
            print_results_aclass_child4(element1, element2, element3, child4_text, cc1, cc2, cc3, cem, outputdirectory) 


        elif ((row4[6]) == "ae-evaluator"): # element
            child4_text = "<b>" + (row4[5]).encode('utf-8') + "</b>"
            print_results_aclass_child4(element1, element2, element3, child4_text, cc1, cc2, cc3, cem, outputdirectory) 


        elif ((row4[6]) == "ae-dc-element"): # element
            child4_text = (row4[5]).encode('utf-8') # paratext
            print_results_aclass_child4(element1, element2, element3, child4_text, cc1, cc2, cc3, cem, outputdirectory) 


        elif ((row4[6]) == "figure"): # element
            figure_title = (row4[3]).encode('utf-8')
            figure_entity = (row4[7]).encode('utf-8')
            figure_width = (row4[8]).encode('utf-8')
            figure_height = (row4[9]).encode('utf-8')
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)
        
        elif ((row4[6]) == "equation"): # element
            figure_title = (row4[3]).encode('utf-8')
            figure_entity = (row4[7]).encode('utf-8')
            figure_width = (row4[8]).encode('utf-8')
            figure_height = (row4[9]).encode('utf-8')
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row4[6]) == "list"): # element
            print_results_list_aclass(element1, element2, cc1, cc2, cc3, cem, outputdirectory)
            child4_list_query = 'SELECT id, parentkey, idelement, title, name, paratext, element FROM child5 WHERE parentkey = '+str(row4[0])+' ORDER BY id'
            for row_c4 in dbmgrlist.query(child4_list_query):
                if ((row_c4[6]) == "item"): # element
                    child4_list_text = (row_c4[5]).encode('utf-8') # item
                    child6_item_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row_c4[0])+' ORDER BY id'
                    for para_item_6 in dbmgritem.query(child6_item_query):
                        if ((para_item_6[5]) == "bold"):
                            child4_list_text += "<b> " + (para_item_6[4]).encode('utf-8') + " </b>"
                        if ((para_item_6[5]) == "italic"):
                            child4_list_text += "<i> " + (para_item_6[4]).encode('utf-8') + " </i>"
                        if ((para_item_6[5]) == "xref"):
                            child4_list_text += (para_item_6[4]).encode('utf-8') # paratext

                        elif ((para_item_6[5]) == "url"): # element
                            child4_list_text += " " + (para_item_6[2]).encode('utf-8') + " " # idelement
                            child4_list_text += (para_item_6[4]).encode('utf-8') # paratext

                    print_results_item_aclass(element1, element2, child4_list_text, cc1, cc2, cc3, cem, outputdirectory)

                    #--------------------------------------------
                    child6_item_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row_c4[0])+' ORDER BY id'
                    for para_item_6 in dbmgritem.query(child6_item_query):
                        if ((para_item_6[5]) == "list"): # element
                            print_results_list_aclass(element1, element2,cc1, cc2, cc3, cem, outputdirectory)
                            child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(para_item_6[0])+' ORDER BY id'
                            for para_item_7 in dbmgrpara1.query(child7_para_query):
                                if ((para_item_7[5]) == "item"): # element
                                    child7_text = (para_item_7[4]).encode('utf-8') # paratext
                                    child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                                    for para_row_8 in dbmgrpara2.query(child8_para_query):
                
                                        if ((para_row_8[5]) == "bold"):
                                            child7_text += "<b> " + (para_row_8[4]).encode('utf-8') + " </b>"
                                        if ((para_row_8[5]) == "italic"):
                                            child7_text += "<i> " + (para_row_8[4]).encode('utf-8') + " </i>"
                                        if ((para_row_8[5]) == "xref"):
                                            child7_text += (para_row_8[4]).encode('utf-8') # paratext

                                    print_results_item_aclass(element1, element2, child7_text, cc1, cc2, cc3, cem, outputdirectory)
                            print_results_list_end_aclass(element1, element2, cc1, cc2, cc3, cem, outputdirectory)

                    #--------------------------------------------

            print_results_list_end_aclass(element1, element2, cc1, cc2, cc3, cem, outputdirectory)
            
            child4_text = (row4[5]).encode('utf-8') # paratext
            print_results_aclass(element1, element2, child4_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (row4[3]):
            child4_text = str(row4[3]) #title
            print_titles(child4_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        elif (row4[4]):
            child4_text = str(row4[4]) #title
            print_titles(child4_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child4_text = str(row4[2])
            #print_results(child4_text, cc1, cc2, cc3, cem, outputdirectory)


    #------------------------------------------------------------------------------

    def child5_to_html(self, element1, element2, element3, element4, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row5, cc1, cc2, cc3, cem, outputdirectory):

        if ((row5[6]) == "item"): # element
            child5_text = ""

        elif ((row5[6]) == "m-workunit"): # element
            child5_text = "<b>Workunit</b> " + (row5[5]).encode('utf-8') # acomponent
            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
            for para_row_6 in dbmgrpara1.query(child6_para_query):
                if ((para_row_6[5]) == "ae-dc-element"): # element
                    child5_text += "<b>" + (para_row_6[4]).encode('utf-8') + "</b>" # paratext
            print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "glossentry"): # element
            if ((row5[5]).encode('utf-8') != ""):
                child5_text = "<b> " + (row5[5]).encode('utf-8') + ": </b> "
                print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "glossterm"): # element
            child5_text = "<b> " + (row5[5]).encode('utf-8') + ": </b> "
            print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "glossdef"): # element
            child5_text = (row5[5]).encode('utf-8') # acomponent
            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
            for para_row_6 in dbmgrpara1.query(child6_para_query):
                if ((para_row_6[5]) == "bold"):
                    child5_text += "<b> " + (para_row_6[4]).encode('utf-8') + " </b>"
                if ((para_row_6[5]) == "italic"):
                    child5_text += "<i> " + (para_row_6[4]).encode('utf-8') + " </i>"
                if ((para_row_6[5]) == "xref"):
                    child5_text += (para_row_6[4]).encode('utf-8') # paratext
            print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "glossnote"): # element
            child5_text = (row5[5]).encode('utf-8') # acomponent
            print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "xref"): # element
            child5_text = ""

        elif ((row5[6]) == "table"): # element
            child5_text = ""
            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
            for para_row_6 in dbmgrpara1.query(child6_para_query):
                if ((para_row_6[5]) == "title" ): # element
                    child5_text += (para_row_6[4]).encode('utf-8') # paratext
            print_results(child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "para"): # element
            child5_text = (row5[5]).encode('utf-8') # paratext

            child6_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
            for para_row_6 in dbmgrpara1.query(child6_para_query):

                if ((para_row_6[5]) == "bold"):
                    child5_text += "<b> " + (para_row_6[4]).encode('utf-8') + " </b>"
                if ((para_row_6[5]) == "italic"):
                    child5_text += "<i> " + (para_row_6[4]).encode('utf-8') + " </i>"
                if ((para_row_6[5]) == "xref"):
                    child5_text += (para_row_6[4]).encode('utf-8') # paratext

            print_results_aclass_child5(element1, element2, element3, element4, child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "figure"): # element
            figure_title = (row5[3]).encode('utf-8')
            figure_entity = (row5[7]).encode('utf-8')
            figure_width = (row5[8]).encode('utf-8')
            figure_height = (row5[9]).encode('utf-8')
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row5[6]) == "list"): # element

            print_results_list_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)
            child5_list_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child6 WHERE parentkey = '+str(row5[0])+' ORDER BY id'
            for row_c5 in dbmgrlist.query(child5_list_query):
                if ((row_c5[5]) == "item"): # element
                    child5_list_text = (row_c5[4]).encode('utf-8') # item

                    child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(row_c5[0])+' ORDER BY id'
                    for para_item_7 in dbmgrpara1.query(child7_para_query):

                        if ((para_item_7[5]) == "bold"):
                            child5_list_text += "<b> " + (para_item_7[4]).encode('utf-8') + " </b>"
                        if ((para_item_7[5]) == "italic"):
                            child5_list_text += "<i> " + (para_item_7[4]).encode('utf-8') + " </i>"
                        if ((para_item_7[5]) == "xref"):
                            child5_list_text += (para_item_7[4]).encode('utf-8') # paratext


                    print_results_item_aclass_child6(element1, element2, element3, element4, child5_list_text, cc1, cc2, cc3, cem, outputdirectory)

                    #--------------------------------------------
                    child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(row_c5[0])+' ORDER BY id'
                    for para_item_7 in dbmgrpara1.query(child7_para_query):
                        if ((para_item_7[5]) == "list"):
                            print_results_list_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)
                            child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_7[0])+' ORDER BY id'
                            for para_item_8 in dbmgrpara2.query(child8_para_query):
                                if ((para_item_8[5]) == "item"): # element
                        
                                    child8_text = (para_item_8[4]).encode('utf-8') # paratext
                                    child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(para_item_8[0])+' ORDER BY id'
                                    for para_row_9 in dbmgrpara3.query(child9_para_query):
                                        if ((para_row_9[5]) == "bold"):
                                            child8_text += "<b> " + (para_row_9[4]).encode('utf-8') + " </b>"
                                        if ((para_row_9[5]) == "italic"):
                                            child8_text += "<i> " + (para_row_9[4]).encode('utf-8') + " </i>"
                                        if ((para_row_9[5]) == "xref"):
                                            child8_text += (para_row_9[4]).encode('utf-8') # paratext

                                    print_results_item_aclass_child6(element1, element2, element3, element4, child8_text, cc1, cc2, cc3, cem, outputdirectory)
                            print_results_list_end_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)

                    #--------------------------------------------

                    
            print_results_list_end_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)
            
            child5_text = (row5[5]).encode('utf-8') # paratext
            print_results_aclass_child5(element1, element2, element3, element4, child5_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (row5[3]):
            child5_text = str(row5[3]) #title
            print_titles(child5_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        elif (row5[4]):
            child5_text = str(row5[4]) #title
            print_titles(child5_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child5_text = str(row5[2])


    #------------------------------------------------------------------------------

    def child6_to_html(self, element1, element2, element3, element4, element5, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row6, cc1, cc2, cc3, cem, outputdirectory):

        if ((row6[5]) == "item"): # element
            child6_text = ""
            
        elif ((row6[5]) == "xref"): # element
            child6_text = ""


        elif ((row6[5]) == "para"): # element
            child6_text = (row6[4]).encode('utf-8') # paratext
            child7_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(row6[0])+' ORDER BY id'
            for para_row_7 in dbmgrpara1.query(child7_para_query):
                if ((para_row_7[5]) == "bold"):
                    child6_text += "<b> " + (para_row_7[4]).encode('utf-8') + " </b>"
                if ((para_row_7[5]) == "italic"):
                    child6_text += "<i> " + (para_row_7[4]).encode('utf-8') + " </i>"
                if ((para_row_7[5]) == "xref"):
                    child6_text += (para_row_7[4]).encode('utf-8') # paratext

            print_results_aclass_child5(element1, element2, element3, element4, child6_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row6[5]) == "equation"): # element
            figure_title = ""
            figure_entity = (row6[6]).encode('utf-8')
            figure_width = ""
            figure_height = ""
            print_results_figure(figure_title, figure_entity, figure_width, figure_height, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row6[5]) == "list"): # element
            print_results_list_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)
            child6_list_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child7 WHERE parentkey = '+str(row6[0])+' ORDER BY id'
            for row_c6 in dbmgrlist.query(child6_list_query):
                if ((row_c6[5]) == "item"): # element
                    child6_list_text = (row_c6[4]).encode('utf-8') # item

                    child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(row_c6[0])+' ORDER BY id'
                    for para_item_8 in dbmgrpara1.query(child8_para_query):

                        if ((para_item_8[5]) == "bold"):
                            child6_list_text += "<b> " + (para_item_8[4]).encode('utf-8') + " </b>"
                        if ((para_item_8[5]) == "italic"):
                            child6_list_text += "<i> " + (para_item_8[4]).encode('utf-8') + " </i>"
                        if ((para_item_8[5]) == "xref"):
                            child6_list_text += (para_item_8[4]).encode('utf-8') # paratext


                    print_results_item_aclass_child6(element1, element2, element3, element4,child6_list_text, cc1, cc2, cc3, cem, outputdirectory)

                    #--------------------------------------------
                    child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(row_c6[0])+' ORDER BY id'
                    for para_item_8 in dbmgrpara1.query(child8_para_query):
                        
                        if ((para_item_8[5]) == "list"):
                            print_results_list_aclass_child6(element1, element2, element3, element4, cc1, cc2, cc3, cem, outputdirectory)

                            child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(para_item_8[0])+' ORDER BY id'
                            for para_row_9 in dbmgrpara2.query(child9_para_query):
                                if ((para_row_9[5]) == "item"): # element
                                    child9_text = (para_row_9[4]).encode('utf-8') # paratext
                                    child10_para_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(para_row_9[0])+' ORDER BY id'
                                    for para_row_10 in dbmgrpara3.query(child10_para_query):

                                        if ((para_row_10[4]) == "bold"):
                                            child9_text += "<b> " + (para_row_10[3]).encode('utf-8') + " </b>"
                                        if ((para_row_10[4]) == "italic"):
                                            child9_text += "<i> " + (para_row_10[3]).encode('utf-8') + " </i>"
                                        if ((para_row_10[4]) == "xref"):
                                            child9_text += (para_row_10[3]).encode('utf-8') # paratext

                                    print_results_item_aclass_child6(element1, element2, element3, element4,child9_text, cc1, cc2, cc3, cem, outputdirectory)
                            print_results_list_end_aclass_child6(element1, element2, element3, element4,cc1, cc2, cc3, cem, outputdirectory)
                    #--------------------------------------------

            print_results_list_end_aclass_child6(element1, element2, element3, element4,cc1, cc2, cc3, cem, outputdirectory)

            child6_text = (row6[4]).encode('utf-8') # paratext
            print_results_aclass_child5(element1, element2, element3, element4, child6_text, cc1, cc2, cc3, cem, outputdirectory)
            

        elif (row6[3]):
            child6_text = str(row6[3]) #title
            print_titles(child6_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child6_text = str(row6[2])
            #print_results(child6_text, cc1, cc2, cc3, cem, outputdirectory)


    #------------------------------------------------------------------------------

    def child7_to_html(self, element1, element2, element3, element4, element5, element6, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row7, cc1, cc2, cc3, cem, outputdirectory):

        if ((row7[5]) == "item"): # element
            child7_text = ""
            
        elif ((row7[5]) == "xref"): # element
            child7_text = ""

        elif ((row7[5]) == "para"): # element
            child7_text = (row7[4]).encode('utf-8') # paratext
            child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(row7[0])+' ORDER BY id'
            for para_row_8 in dbmgrpara1.query(child8_para_query):

                if ((para_row_8[5]) == "bold"):
                    child7_text += "<b> " + (para_row_8[4]).encode('utf-8') + " </b>"
                if ((para_row_8[5]) == "italic"):
                    child7_text += "<i> " + (para_row_8[4]).encode('utf-8') + " </i>"
                if ((para_row_8[5]) == "xref"):
                    child7_text += (para_row_8[4]).encode('utf-8') # paratext

            print_results(child7_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row7[5]) == "list"): # element
        # fix repeated elements
            if ((row7[0]) in (5, 7, 9, 11, 195, 1447)):
                child7_list_text = ""
            else:
                print_results_list_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                child7_list_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(row7[0])+' ORDER BY id'
                for row_c7 in dbmgrlist.query(child7_list_query):
                    if ((row_c7[5]) == "item"): # element
                        child7_list_text = (row_c7[4]).encode('utf-8') # item

                        child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(row_c7[0])+' ORDER BY id'
                        for para_item_9 in dbmgrpara1.query(child9_para_query):
                            if ((para_item_9[5]) == "bold"):
                                child7_list_text += "<b> " + (para_item_9[4]).encode('utf-8') + " </b>"
                            if ((para_item_9[5]) == "italic"):
                                child7_list_text += "<i> " + (para_item_9[4]).encode('utf-8') + " </i>"
                            if ((para_item_9[5]) == "xref"):
                                child7_list_text += (para_item_9[4]).encode('utf-8') # paratext

                        print_results_item_aclass_child7(element1, element2, element3, element4, element5, child7_list_text, cc1, cc2, cc3, cem, outputdirectory)
                        
                        #--------------------------------------------
                        child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(row_c7[0])+' ORDER BY id'
                        for para_item_9 in dbmgrpara2.query(child9_para_query):
                            if ((para_item_9[5]) == "list"):

                                print_results_list_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                                child10_para_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(para_item_9[0])+' ORDER BY id'
                                for para_row_10 in dbmgrpara3.query(child10_para_query):
                                    child10_text = (para_row_10[3]).encode('utf-8') # paratext
                                    if ((para_row_10[4]) == "item"):
                                        child10_text = (para_row_10[3]).encode('utf-8') # paratext
                                        print_results_item_aclass_child7(element1, element2, element3, element4, element5, child10_text, cc1, cc2, cc3, cem, outputdirectory)
                                    if ((para_row_10[4]) == "italic"): # element
                                        child10_text += "<i> " + (para_row_10[3]).encode('utf-8') + " </i>"
                                        print_results_item_aclass_child7(element1, element2, element3, element4, element5,child10_text, cc1, cc2, cc3, cem, outputdirectory)
                                    if ((para_row_10[4]) == "bold"): # element
                                        child10_text += "<b> " +(para_row_10[3]).encode('utf-8') + " </b>"
                                        print_results_item_aclass_child7(element1, element2, element3, element4, element5,child10_text, cc1, cc2, cc3, cem, outputdirectory)
                                    if ((para_row_10[4]) == "xref"): # element
                                        child10_text += (para_row_10[3]).encode('utf-8') # paratext
                                        print_results_item_aclass_child7(element1, element2, element3, element4, element5,child10_text, cc1, cc2, cc3, cem, outputdirectory)

                                print_results_list_end_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                                        
                            if ((para_item_9[4] != "") and (para_item_9[5] != "xref")): # element
                                print_results_list_end_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                                child7_text = (para_item_9[4]).encode('utf-8') # paratext
                                child8_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child8 WHERE parentkey = '+str(para_item_9[0])+' ORDER BY id'
                                for para_row_8 in dbmgrpara4.query(child8_para_query):
                                    if ((para_row_8[5]) == "bold"):
                                        child7_text += "<b> " + (para_row_8[4]).encode('utf-8') + " </b>"
                                    if ((para_row_8[5]) == "italic"):
                                        child7_text += "<i> " + (para_row_8[4]).encode('utf-8') + " </i>"
                                    if ((para_row_8[5]) == "xref"):
                                        child7_text += (para_row_8[4]).encode('utf-8') # paratext

                                print_results(child7_text, cc1, cc2, cc3, cem, outputdirectory)
                                print_results_list_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                                
                            
                                

                        #--------------------------------------------

                print_results_list_end_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
            
            child7_text = (row7[4]).encode('utf-8') # paratext
            print_results_aclass_child5(element1, element2, element3, element4, child7_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (row7[3]):
            child7_text = str(row7[3]) #title
            print_titles(child7_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child7_text = str(row7[2])
            #print_results(child7_text, cc1, cc2, cc3, cem, outputdirectory)
        

    #------------------------------------------------------------------------------

    def child8_to_html(self, element1, element2, element3, element4, element5, element6, element7, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row8, cc1, cc2, cc3, cem, outputdirectory):

        if ((row8[5]) == "item"): # element
            child8_text = ""
            
        elif ((row8[5]) == "xref"): # element
            child8_text = ""

        elif ((row8[5]) == "list"): # element
            # fix repeated elements
            if ((row8[0]) == 34):
                child8_list_text = ""
            else:
                print_results_list(cc1, cc2, cc3, cem, outputdirectory)
                child8_list_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(row8[0])+' ORDER BY id'
                for row_c8 in dbmgrlist.query(child8_list_query):
                    if ((row_c8[5]) == "item"): # element
                        child8_list_text = (row_c8[4]).encode('utf-8') # item

                        child10_para_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(row_c8[0])+' ORDER BY id'
                        for para_item_10 in dbmgrpara1.query(child10_para_query):
                            if ((para_item_10[4]) == "italic"): # element
                                # fix repeated elements
                                if ((para_item_10[0]) in (1,2,3)):
                                    child8_list_text = ""
                                else:
                                    child8_list_text += "<i>" + (para_item_10[3]).encode('utf-8') + " </i>"
                            if ((para_item_10[4]) == "bold"): # element
                                # fix repeated elements
                                if ((para_item_10[0]) in (1,2,3)):
                                    child8_list_text = ""
                                else:
                                    child8_list_text += "<b>" + (para_item_10[3]).encode('utf-8') + " </b>"
                            if ((para_item_10[4]) == "xref"): # element
                                # fix repeated elements
                                if ((para_item_10[0]) in (1,2,3)):
                                    child8_list_text = ""
                                else:
                                    child8_list_text += (para_item_10[3]).encode('utf-8') # paratext
                        if (child8_list_text != ""): print_results_item(child8_list_text, cc1, cc2, cc3, cem, outputdirectory)
                print_results_list_end(cc1, cc2, cc3, cem, outputdirectory)
                

        elif ((row8[5]) == "para"): # element
            child8_text = (row8[4]).encode('utf-8') # paratext
            child9_para_query = 'SELECT id, parentkey, idelement, title, paratext, element FROM child9 WHERE parentkey = '+str(row8[0])+' ORDER BY id'
            for para_row_9 in dbmgrpara1.query(child9_para_query):

                if ((para_row_9[5]) == "bold"):
                    child8_text += "<b> " + (para_row_9[4]).encode('utf-8') + " </b>"
                if ((para_row_9[5]) == "italic"):
                    child8_text += "<i> " + (para_row_9[4]).encode('utf-8') + " </i>"
                if ((para_row_9[5]) == "xref"):
                    child8_text += (para_row_9[4]).encode('utf-8') # paratext

            print_results(child8_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (row8[3]):
            child8_text = str(row8[3]) #title
            print_titles(child8_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child8_text = str(row8[2])
        

    #------------------------------------------------------------------------------

    def child9_to_html(self, element1, element2, element3, element4, element5, element6, element7, element8, dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row9, cc1, cc2, cc3, cem, outputdirectory):

        if ((row9[5]) == "item"): # element
            child9_text = ""
            
        elif ((row9[5]) == "xref"): # element
            child9_text = ""
            
        # TODO poner footnote mas pequeño
        elif ((row9[5]) == "footnote"): # element
            child9_text = (row9[4]).encode('utf-8') # paratext
            child10_para_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(row9[0])+' ORDER BY id'
            for para_row_10 in dbmgrpara1.query(child10_para_query):

                if ((para_row_10[4]) == "bold"):
                    child9_text += "<b> " + (para_row_10[3]).encode('utf-8') + " </b>"
                if ((para_row_10[4]) == "italic"):
                    child9_text += "<i> " + (para_row_10[3]).encode('utf-8') + " </i>"
                if ((para_row_10[4]) == "xref"):
                    child9_text += (para_row_10[3]).encode('utf-8') # paratext
            print_results(child9_text, cc1, cc2, cc3, cem, outputdirectory)

        elif ((row9[5]) == "list"): # element
            if ((row9[0]) in (255,256,269,270)):
                child9_text = ""
            else:
                print_results_list_aclass_child7(element1, element2, element3, element4, element5, cc1, cc2, cc3, cem, outputdirectory)
                child9_list_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(row9[0])+' ORDER BY id'
                for row_c9 in dbmgrlist.query(child9_list_query):
                    if ((row_c9[4]) == "item"): # element
                        child9_list_text = (row_c9[3]).encode('utf-8') # item

                        print_results_item_aclass_child7(element1, element2, element3, element4, element5, child9_list_text, cc1, cc2, cc3, cem, outputdirectory)
                print_results_list_end_aclass_child7(element1, element2, element3, element4, element5,cc1, cc2, cc3, cem, outputdirectory)
            

        elif ((row9[5]) == "para"): # element
            child9_text = (row9[4]).encode('utf-8') # paratext
            child10_para_query = 'SELECT id, parentkey, idelement, paratext, element FROM child10 WHERE parentkey = '+str(row9[0])+' ORDER BY id'
            for para_row_10 in dbmgrpara1.query(child10_para_query):
                if ((para_row_10[4]) == "bold"):
                    child9_text += "<b> " + (para_row_10[3]).encode('utf-8') + " </b>"
                if ((para_row_10[4]) == "italic"):
                    child9_text += "<i> " + (para_row_10[3]).encode('utf-8') + " </i>"
                if ((para_row_10[4]) == "xref"):
                    child9_text += (para_row_10[3]).encode('utf-8') # paratext
            print_results(child9_text, cc1, cc2, cc3, cem, outputdirectory)

        elif (row9[3]):
            child9_text = str(row9[3]) #title
            print_titles(child9_text, "href", cc1, cc2, cc3, cem, outputdirectory)
        else: 
            child9_text = str(row9[2])
        
    #------------------------------------------------------------------------------

    def child10_to_html(self, element1, element2, element3, element4, element5, element6, element7, element8, element9,dbmgrbiblioentry, dbmgrpara1, dbmgrpara2, dbmgrpara3, dbmgrpara4, dbmgritem, dbmgrlist, row10, cc1, cc2, cc3, cem, outputdirectory):

        if ((row10[4]) == "item"): # element
            child10_text = (row10[3]).encode('utf-8') # item
        elif ((row10[4]) == "xref"): # element
            child10_text = ""
        elif (row10[3]):
            child10_text = (row10[3]).encode('utf-8') # paratext
        elif (row10[2]):
            child10_text = str(row10[2]) #title
        else: 
            child10_text = str(row10[1])
        
    #------------------------------------------------------------------------------


###############################################################################
#------------------------------------------------------------------------------
# Class CChtmlExport
#------------------------------------------------------------------------------
###############################################################################

class CChtmlExport:

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

    # Database
    if not (os.path.isfile(results.database)):
      print os.linesep + "Error loading database. Must run CCParser.py first" + os.linesep
      sys.exit(1)
    try:
        # Creates or opens a SQLite3 DB
        #conn = sqlite3.connect(results.database)
        dbmgr1 = DatabaseManager(results.database)
    except NameError:
        print os.linesep + "Error loading database" + os.linesep
        sys.exit(1)
    
    #---------------------------------------------------------------------------
    # Global variables
    #---------------------------------------------------------------------------
    table0 = []
    table1 = []
    table2 = []
    table3 = []
    table4 = []
    table5 = []
    table6 = []
    table7 = []

    #---------------------------------------------------------------------------
    # Output
    #---------------------------------------------------------------------------

    # Create output directory for results
    outputdirectory = 'output'
    datenow = datetime.now()
    outputdate = datenow.strftime('%Y-%m-%d_%H_%M_%S')
    if os.path.exists(outputdirectory): shutil.rmtree(outputdirectory)
    os.makedirs(outputdirectory)
    os.makedirs(outputdirectory + '/txt')
    os.makedirs(outputdirectory + '/html/reports')
    os.makedirs(outputdirectory + '/html/css')
    os.makedirs(outputdirectory + '/html/js')
    os.makedirs(outputdirectory + '/html/fonts')
    os.makedirs(outputdirectory + '/html/img')
    os.makedirs(outputdirectory + '/html/img/icons')
    os.makedirs(outputdirectory + '/html/reports/a-class')
    os.makedirs(outputdirectory + '/html/reports/a-class/graphics')
    os.makedirs(outputdirectory + '/html/reports/clause')
    os.makedirs(outputdirectory + '/html/reports/clause/graphics')
    os.makedirs(outputdirectory + '/html/reports/clause/equations')
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')


    #------------------------------------------------------------------------------

    # Output html
    cc1_html_file = 'CCpart1.html'
    cc2_html_file = 'CCpart2.html'
    cc3_html_file = 'CCpart3.html'
    cem_html_file = 'CEM.html'

    # Create the txt results file
    cc_txt_file = 'cc.txt'
    create_txt_file(cc_txt_file, outputdirectorytxt)

    # Create the html results file
    cc_html_file = 'cc.html'
    create_html_file(cc_html_file, outputdirectoryhtml, outputdate)


    index_menu = {'cc': cc_html_file,
                'cc1': cc1_html_file, 'cc2': cc2_html_file,
                'cc3': cc3_html_file, 'cem': cem_html_file}

    htmlaudit(cc_html_file, outputdirectoryhtml, index_menu)

    create_blank_html_file(cc1_html_file, outputdirectoryhtml, outputdate, index_menu)
    create_blank_html_file(cc2_html_file, outputdirectoryhtml, outputdate, index_menu)
    create_blank_html_file(cc3_html_file, outputdirectoryhtml, outputdate, index_menu)
    create_blank_html_file(cem_html_file, outputdirectoryhtml, outputdate, index_menu)

    #------------------------------------------------------------------------------

    cat_menu = {}

    #------------------------------------------------------------------------------
    # CC1, CC2, CC3
    #------------------------------------------------------------------------------

    document = 0

    child1_query = "SELECT id, title, name, element, orderdoc, cc1, cc2, cc3, cem FROM child1 ORDER BY orderdoc ASC"
    for row in dbmgr1.query(child1_query):
        cat_menu.setdefault(str(row[0]), [])
        orderdoc = str(row[4])
        cc1 = row[5]
        cc2 = row[6]
        cc3 = row[7]
        cem = row[8]

        if (row[5] == 1):
            if (document != 1): print os.linesep + ((colored("CC Part 1", 'red')))
            document = 1
        elif (row[6] == 1):
            if (document != 2): print os.linesep + ((colored("CC Part 2", 'red')))
            document = 2
        elif (row[7] == 1):
            if (document != 3): print os.linesep + ((colored("CC Part 3", 'red')))
            document = 3
        if (row[8] == 1):
            cem = 0
            continue

        
        InitParseChild = ParseChild()

        child1_title = InitParseChild.child1_to_html(row, cc1, cc2, cc3, cem , outputdirectory)
        cat_menu[str(row[0])] = child1_title
        
        print((colored(' - Chapter: ', 'green')) + (colored(child1_title, 'white')))

        stuff = Iterate()
        stuff.search(row, results.database, cc1, cc2, cc3, cem, outputdirectory)


    #------------------------------------------------------------------------------
    # CEM
    #------------------------------------------------------------------------------


    document = 0

    child1_query = "SELECT id, title, name, element, orderdoc, cc1, cc2, cc3, cem FROM child1 ORDER BY orderdoc ASC"
    for row in dbmgr1.query(child1_query):
        cat_menu.setdefault(str(row[0]), [])
        #html_file = cc_file(str(row[0]))
        orderdoc = str(row[4])
        cc1 = row[5]
        cc2 = row[6]
        cc3 = row[7]
        cem = row[8]


        if (row[8] == 1):
            if (document != 4): print os.linesep + ((colored("CEM", 'red')))
            document = 4
        else:
            continue
            
        InitParseChild = ParseChild()

        child1_title = InitParseChild.child1_to_html(row, cc1, cc2, cc3, cem , outputdirectory)
        cat_menu[str(row[0])] = child1_title
        
        print((colored(' - Chapter: ', 'green')) + (colored(child1_title, 'white')))

        stuff = Iterate()
        stuff.search(row, results.database, cc1, cc2, cc3, cem, outputdirectory)

    #------------------------------------------------------------------------------

    htmlend(cc_html_file, outputdirectoryhtml)
    htmlend(cc1_html_file, outputdirectoryhtml)
    htmlend(cc2_html_file, outputdirectoryhtml)
    htmlend(cc3_html_file, outputdirectoryhtml)
    htmlend(cem_html_file, outputdirectoryhtml)

    #---------------------------------------------------------------------------
    htmldatadashboard(cc_html_file, outputdirectoryhtml, cat_menu)
    htmllast(cc_html_file, outputdirectoryhtml)
    htmldatadashboardjs(cc_html_file, outputdirectoryhtml)
    #--------------------------------------------------------------------------
    htmldashboardend(cc_html_file, outputdirectoryhtml)

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
    if CChtmlExport.failure:
        sys.exit(1)
