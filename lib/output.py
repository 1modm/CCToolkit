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
# Plugins
#------------------------------------------------------------------------------
from lib.htmloutput import htmlinfo, htmltitle, htmlinfolist, htmlinfoitem, htmlinfolistend,\
                           htmltitle_subclase, htmltitle_figure, htmlinfotable, htmlinfotr, htmlinfotrend, htmlinforowtd,\
                           htmlinforowth, htmlinforowtd, htmlinfotableend
from lib.txtoutput import print_result_txt, print_title_txt



#------------------------------------------------------------------------------

# Output html
cc1_html_file = 'CCpart1.html'
cc2_html_file = 'CCpart2.html'
cc3_html_file = 'CCpart3.html'
cem_html_file = 'CEM.html'

# Create the txt results file
cc_txt_file = 'cc.txt'


#------------------------------------------------------------------------------
def results(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    element1 = e1
    element2 = e2
    element3 = e3
    element4 = e4
    element5 = e5

    if (cc1 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinfo(childtext, cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinfo(childtext, cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      if (element2 not in ("ac-overview", "ma-introduction", "ma-objectives", "ma-application-notes", "msa-objectives")):
        if (element3 not in ("af-overview", "msa-objectives")):
          if (element4 not in ("msa-objectives", "msa-input", "ae-evaluator", "msa-application-notes")):
            print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
            htmlinfo(childtext, cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      if (element2 not in ("ac-introduction", "ac-overview")):
        print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
        htmlinfo(childtext, cem_html_file, outputdirectoryhtml)

#------------------------------------------------------------------------------
def titles(e1, e2, e3, e4, e5, title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    element1 = e1
    element2 = e2
    element3 = e3
    element4 = e4
    element5 = e5

    if (cc1 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle(cc1_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cc2 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle(cc2_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cc3 > 0):
      if (element2 not in ("ac-overview", "ma-introduction", "ma-objectives", "ma-application-notes", "msa-objectives")):
        print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
        htmltitle(cc3_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cem > 0):
      if (element2 not in ("ac-introduction", "ac-overview")):
        print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
        htmltitle(cem_html_file, outputdirectoryhtml, title_name, hrefsection)


#------------------------------------------------------------------------------
def list(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    element1 = e1
    element2 = e2
    element3 = e3
    element4 = e4
    element5 = e5

    if (cc1 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfolist(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfolist(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      if (element2 not in ("ac-overview", "ma-introduction", "ma-objectives", "ma-application-notes", "msa-objectives")):
        if (element3 not in ("af-overview")):
          if (element4 not in ("msa-objectives", "msa-input")):
            if (element5 not in ("m-workunit")):
              print_result_txt("", cc_txt_file, outputdirectorytxt)
              htmlinfolist(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      if (element2 not in ("ac-introduction", "ac-overview")):
        print_result_txt("", cc_txt_file, outputdirectorytxt)
        htmlinfolist(cem_html_file, outputdirectoryhtml)

#------------------------------------------------------------------------------
def listend(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    element1 = e1
    element2 = e2
    element3 = e3
    element4 = e4
    element5 = e5

    if (cc1 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfolistend(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfolistend(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      if (element2 not in ("ac-overview", "ma-introduction", "ma-objectives", "ma-application-notes", "msa-objectives")):
        if (element3 not in ("af-overview")):
          if (element4 not in ("msa-objectives", "msa-input")):
            if (element5 not in ("m-workunit")):
              print_result_txt("", cc_txt_file, outputdirectorytxt)
              htmlinfolistend(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      if (element2 not in ("ac-introduction", "ac-overview")):
        print_result_txt("", cc_txt_file, outputdirectorytxt)
        htmlinfolistend(cem_html_file, outputdirectoryhtml)

#------------------------------------------------------------------------------
def item(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    element1 = e1
    element2 = e2
    element3 = e3
    element4 = e4
    element5 = e5

    if (cc1 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinfoitem(childtext, cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinfoitem(childtext, cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      if (element2 not in ("ac-overview", "ma-introduction", "ma-objectives", "ma-application-notes", "msa-objectives")):
        if (element3 not in ("af-overview")):
          if (element4 not in ("msa-objectives", "msa-input")):
            if (element5 not in ("m-workunit")):
              print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
              htmlinfoitem(childtext, cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      if (element2 not in ("ac-introduction", "ac-overview")):
        print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
        htmlinfoitem(childtext, cem_html_file, outputdirectoryhtml)


#------------------------------------------------------------------------------

def print_results(childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = "None"
    e2 = "None"
    e3 = "None"
    e4 = "None"
    e5 = "None"
    results(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_aclass(element1, element2, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    results(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_aclass_child4(element1, element2, element3, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    results(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_aclass_child5(element1, element2, element3, element4, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = "None"
    results(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)



def print_titles(title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory):

    e1 = "None"
    e2 = "None"
    e3 = "None"
    e4 = "None"
    e5 = "None"
    titles(e1, e2, e3, e4, e5, title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_titles_aclass(element1, element2, title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory):

    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    titles(e1, e2, e3, e4, e5, title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list_aclass(element1, element2, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    list(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list_aclass_child6(element1, element2, element3, element4, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = "None"
    list(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)

def print_results_list_aclass_child7(element1, element2, element3, element4, element5, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = element5
    list(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = "None"
    e2 = "None"
    e3 = "None"
    e4 = "None"
    e5 = "None"
    list(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list_end_aclass(element1, element2, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    listend(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list_end(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = "None"
    e2 = "None"
    e3 = "None"
    e4 = "None"
    e5 = "None"
    listend(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)
 

def print_results_list_end_aclass_child6(element1, element2, element3, element4, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = "None"
    listend(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_list_end_aclass_child7(element1, element2, element3, element4, element5, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = element5
    listend(e1, e2, e3, e4, e5, cc1file, cc2file, cc3file, cemfile, outputdirectory)



def print_results_item_aclass(element1, element2, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = "None"
    e4 = "None"
    e5 = "None"
    item(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)



def print_results_item_aclass_child6(element1, element2, element3, element4, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = "None"
    item(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)



def print_results_item_aclass_child7(element1, element2, element3, element4, element5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = element1
    e2 = element2
    e3 = element3
    e4 = element4
    e5 = element5
    item(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)


def print_results_item(childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    e1 = "None"
    e2 = "None"
    e3 = "None"
    e4 = "None"
    e5 = "None"
    item(e1, e2, e3, e4, e5, childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory)



def print_results_table(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt("None", cc_txt_file, outputdirectorytxt)
      htmlinfotable(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotable(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotable(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotable(cem_html_file, outputdirectoryhtml)



def print_results_tr(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotr(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotr(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotr(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotr(cem_html_file, outputdirectoryhtml)



def print_results_tr_end(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotrend(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotrend(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotrend(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotrend(cem_html_file, outputdirectoryhtml)


def print_results_rowtd(childtext, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowtd(childtext, cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowtd(childtext, cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowtd(childtext, cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowtd(childtext, cem_html_file, outputdirectoryhtml)



def print_results_rowth(childtext, columnspan, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowth(childtext, columnspan, cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowth(childtext, columnspan, cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowth(childtext, columnspan, cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt(childtext, cc_txt_file, outputdirectorytxt)
      htmlinforowth(childtext, columnspan, cem_html_file, outputdirectoryhtml)



def print_results_table_end(cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotableend(cc1_html_file, outputdirectoryhtml)
    if (cc2 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotableend(cc2_html_file, outputdirectoryhtml)
    if (cc3 > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotableend(cc3_html_file, outputdirectoryhtml)
    if (cem > 0):
      print_result_txt("", cc_txt_file, outputdirectorytxt)
      htmlinfotableend(cem_html_file, outputdirectoryhtml)





def print_titles_subclase(title_name, hrefsection, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt/')
    outputdirectoryhtml = (outputdirectory + '/html/')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_subclase(cc1_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cc2 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_subclase(cc2_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cc3 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_subclase(cc3_html_file, outputdirectoryhtml, title_name, hrefsection)
    if (cem > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_subclase(cem_html_file, outputdirectoryhtml, title_name, hrefsection)




def print_results_figure(title_name, entity, width, height, cc1file, cc2file, cc3file, cemfile, outputdirectory):
    outputdirectorytxt = (outputdirectory + '/txt/')
    outputdirectoryhtml = (outputdirectory + '/html/')
    cc1 = int(cc1file)
    cc2 = int(cc2file)
    cc3 = int(cc3file)
    cem = int(cemfile)

    if (cc1 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_figure(cc1_html_file, outputdirectoryhtml, title_name, entity, width, height)
    if (cc2 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_figure(cc2_html_file, outputdirectoryhtml, title_name, entity, width, height)
    if (cc3 > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_figure(cc3_html_file, outputdirectoryhtml, title_name, entity, width, height)
    if (cem > 0):
      print_title_txt(title_name, cc_txt_file, outputdirectorytxt)
      htmltitle_figure(cem_html_file, outputdirectoryhtml, title_name, entity, width, height)


