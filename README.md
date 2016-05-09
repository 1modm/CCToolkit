CCToolkit
=========

What's CCToolkit?
-----------------

**CCToolkit** is an open source tool and Python Based Toolkit that helps you to parse, export and generate a quick workunit checklist using the official Common Criteria XML provided in https://www.commoncriteriaportal.org/cc/. **Use by your own risk!**


License
=======

[The BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

```
CCToolkit

Author: https://github.com/1modm

Project site: https://github.com/1modm/CCToolkit

Copyright (c) 2016, https://github.com/1modm/
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
```


Installation
============
CCToolkit doesn't require installation, only are needed the dependencies mentioned below.

Dependencies
------------

* 2.7 < Python < 3.0
* python datetime module
* python argparse module
* python sys module
* python platform module
* python pysqlite module
* python os module
* python xlsxwriter module
* python python-docx module
* python pythondialog module
* python commands module
* python Tkinter module
* python shutil module
* python hashlib module


Linux Debian
------
```
# apt-get install python python-pip python-dev build-essential libsqlite3-dev python-tk python3-dialog
# git clone https://github.com/1modm/CCToolkit.git && cd CCToolkit
# pip install -r requirements.lst
```

Windows
------
```
- Install python 2.X https://www.python.org/downloads/windows/
- Download https://github.com/1modm/CCToolkit/archive/master.zip
- Install required modules
```


Usage
=====

With Graphical User Interface
-----------------------------

```
python CCToolkit.py -gui
```

Using command line
------------------
```
python CCToolkit.py -cmd
```


The ToolKit is composed by three independent modules, each one able to provide a different functionallity
----------------------------------------------------------------------------------------------------------
- **Parse CC into a Database:** Parse cc3R4.xml and insert into Database
```
python CCParser.py doc/cc3R4.xml
```

- **Export CC:** Export Database into HTML
```
python CChtmlExport.py data/ccdb.sqlite3
```

- **Generate Checklist:** Create workunit checklist references in .docx, .xlsx and txt
```
python CCChecklist.py -eal EAL4 -ac AVA_VAN.5 -p 1 data/ccdb.sqlite3
```


Output
======
![CCToolkit](https://dl.dropboxusercontent.com/u/5741635/CCToolkit1.png "CCToolkit Menu")
![CCToolkit](https://dl.dropboxusercontent.com/u/5741635/CCToolkit2.png "CCToolkit Menu")
![CCToolkit](https://dl.dropboxusercontent.com/u/5741635/CCToolkit3.png "CCToolkit Menu")
![CCToolkit](https://dl.dropboxusercontent.com/u/5741635/CCToolkit4.png "CCToolkit Menu")

- Checklist output
![CCToolkit](https://dl.dropboxusercontent.com/u/5741635/CCToolkit5.png "Checklist output")



