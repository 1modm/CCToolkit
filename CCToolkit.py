#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """

CCToolkit

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
import subprocess
import locale
import platform
from tkMessageBox import *
from Tkinter import *
import random


#------------------------------------------------------------------------------
# Class AutoScrollbar
#------------------------------------------------------------------------------

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        #if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
        #    self.call("grid", "remove", self)
        #else:
        self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"


#------------------------------------------------------------------------------
# Command line parser using argparse
#------------------------------------------------------------------------------

def cmdline_parser():
    parser = argparse.ArgumentParser(conflict_handler='resolve', add_help=True,
        description='Example: python %(prog)s -gui', version='menu 0.1',
        usage="python %(prog)s [OPTIONS]")

    # Optional
    parser.add_argument('-gui', action='store_true', default=False, dest='gui')
    parser.add_argument('-cmd', action='store_true', default=False, dest='cmd')

    return parser

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

try:
    parser = cmdline_parser()
    # Show help if no args
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
except NameError:
    print "ERROR"
    sys.exit(1)

is_windows = any(platform.win32_ver())

if not (is_windows):
  try:
      from dialog import Dialog
  except ImportError:
      print 'pythondialog required. Install using `pip install pythondialog or apt-get install python-dialog`'
      sys.exit(1)



#---------------------------------------------------------------------------
# Global variables
#---------------------------------------------------------------------------
dictAC = {}
dictDetail = {}
dictEAL = {}
detailOption = 1


#------------------------------------------------------------------------------

def run_process(command, stderr=False):
  p = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  output = ""
  while(True):
    retcode = p.poll()
    if stderr:
      line = p.stderr.readline().decode('utf-8')
    else:
      line = p.stdout.readline().decode('utf-8')
    output = output + line

    if retcode is not None:
      break

  return {'retcode': retcode, 'output': output}

def commandline():

  TXT_WELCOME_TITLE = 'Yet Another Common Criteria Parser and Checklist Generator!\n\nThis tool helps you to generate a quick workunit checklist.\n\nUse by your own risk'

  locale.setlocale(locale.LC_ALL, '')
  # You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
  d = Dialog(dialog="dialog")
  #d = Dialog(dialog='dialog', autowidgetsize=True)
  # Dialog.set_background_title() requires pythondialog 2.13 or later
  d.set_background_title(TXT_WELCOME_TITLE)
  # For older versions, you can use:
  #   d.add_persistent_args(["--backtitle", "My little program"])

  # In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
  # "ok" (same object). In pythondialog 2.x, you have to use d.DIALOG_OK, which
  # is deprecated since version 3.0.0.
  code = d.yesno(TXT_WELCOME_TITLE, 
                  height="15", width="65", yes_label="OK", no_label="Cancel")

  if (code == Dialog.CANCEL or code == Dialog.ESC):
    clearquit()

  else:
    code, tag = d.menu("OK, then you have four options:",
                       choices=[("(1)", "Parse CC into a Database"),
                                ("(2)", "Export CC"),
                                ("(3)", "Parse and Export"),
                                ("(4)", "Generate Checklist")])
    if code == d.OK:
      if tag == "(1)":
        os.system('clear')
        if not (os.path.isfile("doc/cc3R4.xml")):
          d.msgbox("Error loading cc3R4.xml",height="10", width="45")
          sys.exit(1)
        os.system("python CCParser.py -ask doc/cc3R4.xml")
        d.msgbox("Generated database in data/ccdb.sqlite3",height="10", width="45")
        quit()

      elif tag == "(2)":
        os.system('clear')
        if not (os.path.isfile("data/ccdb.sqlite3")):
          d.msgbox("Error loading database. Must run CCParser.py first",height="10", width="45")
          sys.exit(1)
        os.system("python CChtmlExport.py -ask data/ccdb.sqlite3") 
        d.msgbox("Generated export in output/",height="10", width="45")
        quit()

      elif tag == "(3)":
        os.system('clear')
        if not (os.path.isfile("doc/cc3R4.xml")):
          d.msgbox("Error loading cc3R4.xml",height="10", width="45")
          sys.exit(1)
        os.system("python CCParser.py doc/cc3R4.xml && python CChtmlExport.py -ask data/ccdb.sqlite3") 
        d.msgbox("Generated database in data/ccdb.sqlite3 and export in output/",height="10", width="75")
        quit()

      elif tag == "(4)":
        if not (os.path.isfile("data/ccdb.sqlite3")):
          d.msgbox("Error loading database. Must run CCParser.py first",height="10", width="45")
          sys.exit(1)

        code, tag = d.menu("Evaluation Assurance Level:",
                           choices=[("(EAL1)", "Evaluation Assurance Level 1"),
                                    ("(EAL2)", "Evaluation Assurance Level 2"),
                                    ("(EAL3)", "Evaluation Assurance Level 3"),
                                    ("(EAL4)", "Evaluation Assurance Level 4"),
                                    ("(EAL5)", "Evaluation Assurance Level 5"),
                                    ("(EAL6)", "Evaluation Assurance Level 6"),
                                    ("(EAL7)", "Evaluation Assurance Level 7")])

        if code == d.OK:

          if tag == "(EAL1)": EALSELECTED = "EAL1"
          if tag == "(EAL2)": EALSELECTED = "EAL2"
          if tag == "(EAL3)": EALSELECTED = "EAL3"
          if tag == "(EAL4)": EALSELECTED = "EAL4"
          if tag == "(EAL5)": EALSELECTED = "EAL5"
          if tag == "(EAL6)": EALSELECTED = "EAL6"
          if tag == "(EAL7)": EALSELECTED = "EAL7"
     
          code, tags = d.checklist("Family",
                                   choices=[("ACO_DEV.1", "", False),
                                            ("ACO_DEV.2", "", False),
                                            ("ACO_DEV.3", "", False),
                                            ("ACO_REL.1", "", False),
                                            ("ACO_REL.2", "", False),
                                            ("ACO_CTT.1", "", False),
                                            ("ACO_CTT.2", "", False),
                                            ("ACO_VUL.1", "", False),
                                            ("ACO_VUL.2", "", False),
                                            ("ACO_VUL.3", "", False),
                                            ("ADV_ARC.1", "", False),
                                            ("ADV_FSP.2", "", False),
                                            ("ADV_FSP.3", "", False),
                                            ("ADV_FSP.4", "", False),
                                            ("ADV_FSP.5", "", False),
                                            ("ADV_FSP.6", "", False),
                                            ("ADV_IMP.1", "", False),
                                            ("ADV_IMP.2", "", False),
                                            ("ADV_INT.1", "", False),
                                            ("ADV_INT.2", "", False),
                                            ("ADV_SPM.1", "", False),
                                            ("ADV_TDS.3", "", False),
                                            ("ADV_TDS.4", "", False),
                                            ("ADV_TDS.5", "", False),
                                            ("AGD_OPE.1", "", False),
                                            ("AGD_PRE.1", "", False),
                                            ("ALC_CMC.1", "", False),
                                            ("ALC_CMC.2", "", False),
                                            ("ALC_CMC.3", "", False),
                                            ("ALC_CMC.4", "", False),
                                            ("ALC_CMC.5", "", False),
                                            ("ALC_CMS.1", "", False),
                                            ("ALC_CMS.2", "", False),
                                            ("ALC_CMS.3", "", False),
                                            ("ALC_CMS.4", "", False),
                                            ("ALC_CMS.5", "", False),
                                            ("ALC_DEL.1", "", False),
                                            ("ALC_DVS.1", "", False),
                                            ("ALC_DVS.2", "", False),
                                            ("ALC_FLR.1", "", False),
                                            ("ALC_FLR.2", "", False),
                                            ("ALC_FLR.3", "", False),
                                            ("ALC_LCD.1", "", False),
                                            ("ALC_LCD.2", "", False),
                                            ("ALC_TAT.1", "", False),
                                            ("ALC_TAT.2", "", False),
                                            ("ALC_TAT.3", "", False),
                                            ("APE_INT.1", "", False),
                                            ("APE_CCL.1", "", False),
                                            ("APE_SPD.1", "", False),
                                            ("APE_OBJ.1", "", False),
                                            ("APE_OBJ.2", "", False),
                                            ("APE_ECD.1", "", False),
                                            ("APE_REQ.1", "", False),
                                            ("APE_REQ.2", "", False),
                                            ("ASE_INT.1", "", False),
                                            ("ASE_CCL.1", "", False),
                                            ("ASE_SPD.1", "", False),
                                            ("ASE_OBJ.1", "", False),
                                            ("ASE_OBJ.2", "", False),
                                            ("ASE_ECD.1", "", False),
                                            ("ASE_REQ.1", "", False),
                                            ("ASE_REQ.2", "", False),
                                            ("ASE_TSS.1", "", False),
                                            ("ASE_TSS.2", "", False),
                                            ("ATE_COV.1", "", False),
                                            ("ATE_COV.2", "", False),
                                            ("ATE_DPT.1", "", False),
                                            ("ATE_DPT.2", "", False),
                                            ("ATE_DPT.3", "", False),
                                            ("ATE_FUN.1", "", False),
                                            ("ATE_IND.1", "", False),
                                            ("ATE_IND.2", "", False),
                                            ("AVA_VAN.1", "", False),
                                            ("AVA_VAN.2", "", False),
                                            ("AVA_VAN.3", "", False),
                                            ("AVA_VAN.4", "", False),
                                            ("AVA_VAN.5", "", False),
                                            ],
                                   title="Evaluation Assurance Level",
                                   backtitle="Select one...")

          if code == d.OK:

            AC =""
            for i in tags:
              AC = AC + " " + i

            code, tag = d.menu("Detail level:",
                               choices=[("(D1)", "Detail Level 1"),
                                        ("(D2)", "Detail Level 2"),
                                        ("(D3)", "Detail Level 3"),
                                        ("(D4)", "Detail Level 4")])
            if code == d.OK:

              if tag == "(D1)": DETAILSELECTED = "1"
              if tag == "(D2)": DETAILSELECTED = "2"
              if tag == "(D3)": DETAILSELECTED = "3"
              if tag == "(D4)": DETAILSELECTED = "4"

              if AC: 
                os.system('clear')
                os.system("python CCChecklist.py -eal " + EALSELECTED + " -ac " + AC + " -p "  + DETAILSELECTED + " -ask data/ccdb.sqlite3") 
              else:
                os.system('clear')
                os.system("python CCChecklist.py -eal " + EALSELECTED + " -p "  + DETAILSELECTED + " -ask data/ccdb.sqlite3") 
            else:
              quit()
              
            d.msgbox("Check /output folder")
            quit()
          else:
            quit()
        else:
          quit()
    else:
      quit()

def menuoption1():
  if not (os.path.isfile("doc/cc3R4.xml")):
    showwarning('Warning', 'Error loading doc/cc3R4.xml')
    sys.exit(1)
  os.system("python CCParser.py doc/cc3R4.xml")
  showinfo('Info', 'Generated database in data/ccdb.sqlite3')
  quit()

def menuoption2():
  if not (os.path.isfile("data/ccdb.sqlite3")):
    showwarning('Warning', 'Error loading database. Must run CCParser.py first')
    sys.exit(1)
  os.system("python CChtmlExport.py data/ccdb.sqlite3") 
  showinfo('Info', 'Generated export in output/')
  quit()

def menuoption3():
  if not (os.path.isfile("doc/cc3R4.xml")):
    showwarning('Warning', 'Error loading doc/cc3R4.xml')
    sys.exit(1)
  os.system("python CCParser.py doc/cc3R4.xml && python CChtmlExport.py data/ccdb.sqlite3") 
  showinfo('Info', 'Generated database in data/ccdb.sqlite3 and export in output/')
  quit()

def menuoption4():
  if not (os.path.isfile("data/ccdb.sqlite3")):
    showwarning('Warning', 'Error loading database. Must run CCParser.py first')
    sys.exit(1)
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame5.pack()

#------------------------------------------------------------------------------

def menuDetail1():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame3.pack()
  dictDetail["detailOption"] = 1;

def menuDetail2():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame3.pack()
  dictDetail["detailOption"] = 2;

def menuDetail3():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame3.pack()
  dictDetail["detailOption"] = 3;

def menuDetail4():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame3.pack()
  dictDetail["detailOption"] = 4;

#------------------------------------------------------------------------------
def eal1():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL1";
  menuCheckbutton()

def eal2():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL2";
  menuCheckbutton()

def eal3():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL3";
  menuCheckbutton()

def eal4():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL4";
  menuCheckbutton()

def eal5():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL5";
  menuCheckbutton()

def eal6():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL6";
  menuCheckbutton()

def eal7():
  frame5.pack_forget()
  frame4.pack_forget()
  frame3.pack_forget()
  frame2.pack_forget()
  frame4.pack()
  dictEAL["EAL"] = "EAL7";
  menuCheckbutton()


def menuCheckbutton():

  acs = ["ACO_DEV.1", "ACO_DEV.2", "ACO_DEV.3", "ACO_REL.1", "ACO_REL.2", "ACO_CTT.1", "ACO_CTT.2", "ACO_VUL.1", "ACO_VUL.2", "ACO_VUL.3", "ADV_ARC.1", "ADV_FSP.2", "ADV_FSP.3", "ADV_FSP.4", "ADV_FSP.5", "ADV_FSP.6", "ADV_IMP.1", "ADV_IMP.2", "ADV_INT.1", "ADV_INT.2", "ADV_SPM.1", "ADV_TDS.3", "ADV_TDS.4", "ADV_TDS.5", "AGD_OPE.1", "AGD_PRE.1", "ALC_CMC.1", "ALC_CMC.2", "ALC_CMC.3", "ALC_CMC.4", "ALC_CMC.5", "ALC_CMS.1", "ALC_CMS.2", "ALC_CMS.3", "ALC_CMS.4", "ALC_CMS.5", "ALC_DEL.1", "ALC_DVS.1", "ALC_DVS.2", "ALC_FLR.1", "ALC_FLR.2", "ALC_FLR.3", "ALC_LCD.1", "ALC_LCD.2", "ALC_TAT.1", "ALC_TAT.2", "ALC_TAT.3", "APE_INT.1", "APE_CCL.1", "APE_SPD.1", "APE_OBJ.1", "APE_OBJ.2", "APE_ECD.1", "APE_REQ.1", "APE_REQ.2", "ASE_INT.1", "ASE_CCL.1", "ASE_SPD.1", "ASE_OBJ.1", "ASE_OBJ.2", "ASE_ECD.1", "ASE_REQ.1", "ASE_REQ.2", "ASE_TSS.1", "ASE_TSS.2", "ATE_COV.1", "ATE_COV.2", "ATE_DPT.1", "ATE_DPT.2", "ATE_DPT.3", "ATE_FUN.1", "ATE_IND.1", "ATE_IND.2", "AVA_VAN.1", "AVA_VAN.2", "AVA_VAN.3", "AVA_VAN.4", "AVA_VAN.5"]

  for ac in acs:
    var = IntVar()
    Checkbutton(frame4, text=ac, variable=var).pack(side=TOP, anchor=W, expand=YES)
    dictAC[ac] = var; # Add new entry

  Button(frame4, text='Quit', command=root.quit).pack(side=RIGHT)
  Button(frame4, text='Generate Checklist', command=generateChecklist).pack(side=RIGHT)

  canvas.create_window(0, 0, anchor=NW, window=frame4)
  frame4.update_idletasks()
  canvas.config(scrollregion=canvas.bbox("all"))


#------------------------------------------------------------------------------

def clearquit():
  os.system('clear')
  sys.exit(0)

def quit():
  sys.exit(0)

#------------------------------------------------------------------------------

def generateChecklist():
  AC =""
  for e in dictAC:
    if (dictAC[e].get() == 1):
      AC = AC + " " + e

  if AC: 
    os.system('clear')
    os.system("python CCChecklist.py -eal " + dictEAL["EAL"] + " -ac " + AC + " -p "  + str(dictDetail["detailOption"]) + " data/ccdb.sqlite3")
    showinfo('Info', 'Generated checklist in output/')
    quit()
  else:
    os.system('clear')
    os.system("python CCChecklist.py -eal " + dictEAL["EAL"] + " -p "  + str(dictDetail["detailOption"]) + " data/ccdb.sqlite3")
    showinfo('Info', 'Generated checklist in output/')
    quit()


#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    results = parser.parse_args()

    if (results.gui):
      root = Tk()
      # width x height + x_offset + y_offset:
      root.geometry("570x500+300+100") 
      #root.attributes('-zoomed', True)
      root.title("CCToolkit")
      #screen_width = root.winfo_screenwidth()
      #screen_height = root.winfo_screenheight()
      #root.geometry("550x550+%d+%d" % (screen_width/175, screen_height/125))
      #root.configure(background='green')
      #root.lift ()
      #------------------------------------------------------------------------------
      vscrollbar = AutoScrollbar(root)
      vscrollbar.grid(row=0, column=1, sticky=N+S)
      hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
      hscrollbar.grid(row=1, column=0, sticky=E+W)

      canvas = Canvas(root,
                      yscrollcommand=vscrollbar.set,
                      xscrollcommand=hscrollbar.set)
      canvas.grid(row=0, column=0, sticky=N+S+E+W)

      vscrollbar.config(command=canvas.yview)
      hscrollbar.config(command=canvas.xview)

      # make the canvas expandable
      root.grid_rowconfigure(0, weight=1)
      root.grid_columnconfigure(0, weight=1)
      #------------------------------------------------------------------------------

      frame1 = Frame(canvas)
      frame2 = Frame(canvas)
      frame3 = Frame(canvas)
      frame4 = Frame(canvas)
      frame5 = Frame(canvas)
      frame1.pack()
      frame2.pack()

      # create canvas contents
      frame4 = Frame(canvas)
      frame4.rowconfigure(1, weight=1)
      frame4.columnconfigure(1, weight=1)


      if askyesno('Verify', 'Yet Another Common Criteria Parser and Checklist Generator!\n\nThis tool helps you to generate a quick workunit checklist.\n\nUse by your own risk'):
        menubar = Menu(frame1) 
        menubar.add_command(label="Quit", command=root.destroy)
        root.config(menu=menubar)

        Label(frame2, text="Parse CC into a Database: Parse cc3R4.xml and insert into Database", padx=5, pady=5, anchor=W, justify=LEFT, fg="red").pack(fill=X)
        Label(frame2, text="Export CC: Export Database into HTML", padx=5, pady=5,  anchor=W, justify=LEFT, fg="red").pack(fill=X)
        Label(frame2, text="Parse and Export: Parse cc3R4.xml and Export Database into HTML", padx=5, pady=5,  anchor=W, justify=LEFT, fg="red").pack(fill=X)
        Label(frame2, text="Generate Checklist: Create workunit checklist references in .docx, .xlsx and txt", padx=5, pady=5, anchor=W, justify=LEFT, fg="red").pack(fill=X)
        Button(frame2,text='Parse CC into a Database', command=menuoption1, padx=20, pady=20).pack(fill=X)
        Button(frame2,text='Export CC', command=menuoption2, padx=20, pady=20).pack(fill=X)
        Button(frame2,text='Parse and Export', command=menuoption3, padx=20, pady=20).pack(fill=X)
        Button(frame2,text='Generate Checklist', command=menuoption4, padx=20, pady=20).pack(fill=X)

        #Label(frame5, text="Number of paragraphs:", padx=20, pady=20).pack()
        Button(frame5,text='Detail Level 1', command=menuDetail1, padx=20, pady=20).pack(fill=X)
        Button(frame5,text='Detail Level 2', command=menuDetail2, padx=20, pady=20).pack(fill=X)
        Button(frame5,text='Detail Level 3', command=menuDetail3, padx=20, pady=20).pack(fill=X)
        Button(frame5,text='Detail Level 4', command=menuDetail4, padx=20, pady=20).pack(fill=X)

        #Label(frame3, text="Evaluation Assurance Level:", padx=20, pady=20).pack()
        Button(frame3,text='Evaluation Assurance Level 1', command=eal1, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 2', command=eal2, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 3', command=eal3, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 4', command=eal4, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 5', command=eal5, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 6', command=eal6, padx=10, pady=10).pack(fill=X)
        Button(frame3,text='Evaluation Assurance Level 7', command=eal7, padx=10, pady=10).pack(fill=X)

      #------------------------------------------------------------------------------
      else:
        quit()
               
      root.mainloop()


    if (results.cmd):
      commandline()
