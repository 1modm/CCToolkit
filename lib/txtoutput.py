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

#------------------------------------------------------------------------------

def create_txt_file(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __create_file__ = open(__file__, 'w')
    __create_file__.write(os.linesep)
    __create_file__.close()


def print_result_txt(childtext, file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __file__ = open(__file__, 'a')
    __file__.write(childtext)
    __file__.write(os.linesep)
    __file__.close()

def print_result_linesep_txt(childtext, file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __file__ = open(__file__, 'a')
    __file__.write(os.linesep * 2)
    __file__.write(childtext)
    __file__.write(os.linesep)
    __file__.close()

def print_title_txt(title_name, file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __file__ = open(__file__, 'a')
    __file__.write(os.linesep * 2)
    __file__.write("--------------------------------------------------------------------------------------------------------------------------" + os.linesep)
    __file__.write(title_name + os.linesep)
    __file__.write("--------------------------------------------------------------------------------------------------------------------------" + os.linesep * 3)
    __file__.close()
