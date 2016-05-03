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

import shutil

#------------------------------------------------------------------------------


def create_html_file(file_name, outputdir, outputdate):

    templateadmin = 'lib/html/NiceAdmin'
    
    # Copy css, img and js
    cssoutput = outputdir + '/css'
    shutil.copy2(templateadmin + '/css/timeline.css', cssoutput)
    shutil.copy2(templateadmin + '/css/social-buttons.css', cssoutput)
    shutil.copy2(templateadmin + '/css/bootstrap.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/bootstrap-theme.css', cssoutput)
    shutil.copy2(templateadmin + '/css/elegant-icons-style.css', cssoutput)
    shutil.copy2(templateadmin + '/css/font-awesome.css', cssoutput)
    shutil.copy2(templateadmin + '/css/font-awesome.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/fullcalendar.css', cssoutput)
    shutil.copy2(templateadmin + '/css/jquery-jvectormap-1.2.2.css', cssoutput)
    shutil.copy2(templateadmin + '/css/jquery-ui-1.10.4.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/line-icons.css', cssoutput)
    shutil.copy2(templateadmin + '/css/owl.carousel.css', cssoutput)
    shutil.copy2(templateadmin + '/css/style.css', cssoutput)
    shutil.copy2(templateadmin + '/css/style-responsive.css', cssoutput)
    shutil.copy2(templateadmin + '/css/widgets.css', cssoutput)
    shutil.copy2(templateadmin + '/css/xcharts.min.css', cssoutput)

    fontsoutput = outputdir + '/fonts'
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.ttf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/FontAwesome.otf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.ttf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.ttf', fontsoutput)

    jsoutput = outputdir + '/js'
    shutil.copy2(templateadmin + '/js/additional-methods.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-switch.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-wysiwyg-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-wysiwyg.js', jsoutput)
    shutil.copy2(templateadmin + '/js/calendar-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/chartjs-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-flot.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-other.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-xcharts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/dynamic-table.js', jsoutput)
    shutil.copy2(templateadmin + '/js/easy-pie-chart.js', jsoutput)
    shutil.copy2(templateadmin + '/js/excanvas.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/form-component.js', jsoutput)
    shutil.copy2(templateadmin + '/js/form-validation-script.js', jsoutput)
    shutil.copy2(templateadmin + '/js/fullcalendar.js', jsoutput)
    shutil.copy2(templateadmin + '/js/fullcalendar.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/ga.js', jsoutput)
    shutil.copy2(templateadmin + '/js/gdp-data.js', jsoutput)
    shutil.copy2(templateadmin + '/js/gritter.js', jsoutput)
    shutil.copy2(templateadmin + '/js/html5shiv.js', jsoutput)
    shutil.copy2(templateadmin + '/js/index.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-1.8.3.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.autosize.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.customSelect.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.flot.pie.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.hotkeys.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-jvectormap-1.2.2.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-jvectormap-world-mill-en.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.localscroll.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.nicescroll.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.placeholder.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.rateit.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.scrollTo.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.slimscroll.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.smartWizard.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.sparkline-11.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.sparkline.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.stepy.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.tagsinput.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-ui-1.10.4.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-ui-1.9.2.custom.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.validate.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/lte-ie7.js', jsoutput)
    shutil.copy2(templateadmin + '/js/morris.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/morris-script.js', jsoutput)
    shutil.copy2(templateadmin + '/js/owl.carousel.js', jsoutput)
    shutil.copy2(templateadmin + '/js/scripts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sliders.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sparkline-chart.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sparklines.js', jsoutput)
    shutil.copy2(templateadmin + '/js/xcharts.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/d3.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/d3pie.js', jsoutput)

    imgoutput = outputdir + '/img'
    shutil.copy2(templateadmin + '/img/avatar1_small.png', imgoutput)
    imgoutput = outputdir + '/img/icons'
    shutil.copy2(templateadmin + '/img/icons/line-icon-c.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/line-icon-hover.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/line-icon.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/search-line-icon.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/social.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/weather-hover.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/weather.png', imgoutput)

    imagescc = 'lib/html/img'
    imgoutput = outputdir + '/reports/a-class/graphics'
    shutil.copy2(imagescc + '/a-class/graphics/FSP-types-of-interfaces.png', imgoutput)
    shutil.copy2(imagescc + '/a-class/graphics/TDS-components-and-modules.png', imgoutput)
    shutil.copy2(imagescc + '/a-class/graphics/ADV-relationships.png', imgoutput)
    shutil.copy2(imagescc + '/a-class/graphics/aco_family_interaction.png', imgoutput)
    shutil.copy2(imagescc + '/a-class/graphics/aco_family_relation.png', imgoutput)
    shutil.copy2(imagescc + '/a-class/graphics/part3alc-1.png', imgoutput)

    imgoutput = outputdir + '/reports/clause/graphics'
    shutil.copy2(imagescc + '/clause/graphics/ACO-interact-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/ACO-interact-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/ACO-interact-3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/ACO-interact-4.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/API-diagram.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part302-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part302-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/componenttaxonomy.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part302-3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part302-4.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part3cap1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part3cap2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_01_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_02_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_04_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_A1_rel3_2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_06_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_08_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_09_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_11_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part1_10_rel3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part201-3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part201-4.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part202-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part202-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part2_05_patch.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part202-4.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part2anA-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part2anA-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/part2anA-3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/cem2_ch1-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/cem2_ch2-3.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/cem2_ch1-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/cem2_ch2-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/graphics/cem2_ch2-2.png', imgoutput)

    imgoutput = outputdir + '/reports/clause/equations'
    shutil.copy2(imagescc + '/clause/equations/cem2_anb-1.png', imgoutput)
    shutil.copy2(imagescc + '/clause/equations/cem2_anb-2.png', imgoutput)
    shutil.copy2(imagescc + '/clause/equations/cem2_anb-3.png', imgoutput)


    __title__ = outputdate
    __file__ = outputdir + '/' + file_name
    __htmFile__ = open(__file__, 'w')
    __htmFile__.write(head(__title__))
    __htmFile__.close


#------------------------------------------------------------------------------


def create_blank_html_file(file_name, outputdir, outputdate, menu_html):
    __title__ = outputdate
    __file__ = outputdir + '/reports/' + file_name
    __htmFile__ = open(__file__, 'w')
    __htmFile__.write(headreports(__title__))
    __htmFile__.write(navbarreports(menu_html))
    __htmFile__.write(bodyblank())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlaudit(file_name, outputdir, menu_html):
    __file__ = outputdir + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(navbar(menu_html))
    __htmFile__.write(bodydashboard(file_name))
    __htmFile__.close


#------------------------------------------------------------------------------

def htmltitle(file_name, outputdirectory, title, href):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodytitle(title, href))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmltitle_subclase(file_name, outputdirectory, title, href):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodytitle_subclase(title, href))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmltitle_figure(file_name, outputdirectory, title, entity, width, height):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodytitle_figure(title, entity, width, height))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinfo(childtext, file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfo(childtext))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinfolist(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfolist())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlinfolistend(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfolistend())
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinfotable(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfotable())
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinfotr(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfotr())
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinfotrend(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfotrend())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlinforowth(childtext, columnspan, file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinforowth(childtext, columnspan))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmlinforowtd(childtext, file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinforowtd(childtext))
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlinfotableend(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfotableend())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlinfoitem(childtext, file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfoitem(childtext))
    __htmFile__.close

#------------------------------------------------------------------------------

def htmllast(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyend())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmldashboardend(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyendhtml())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlend(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyendhtmljs())
    __htmFile__.close


#------------------------------------------------------------------------------


def htmldatadashboard(file_name, outputdirectory, menu_html):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(tablecontent(menu_html))
    __htmFile__.close

#------------------------------------------------------------------------------


def htmldatadashboardjs(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyjsend())
    __htmFile__.close


#------------------------------------------------------------------------------

def head(title):
    __head__ = ("""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>

    <!-- Bootstrap CSS -->    
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- bootstrap theme -->
    <link href="css/bootstrap-theme.css" rel="stylesheet">
    <!--external css-->
    <!-- font icon -->
    <link href="css/elegant-icons-style.css" rel="stylesheet" />
    <link href="css/font-awesome.min.css" rel="stylesheet" />    
    <!-- Custom styles -->
    <link href="css/style.css" rel="stylesheet">
    <link href="css/style-responsive.css" rel="stylesheet" />

    <link href="css/social-buttons.css" rel="stylesheet">
    <link href="css/timeline.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
      <script src="js/respond.min.js"></script>
      <script src="js/lte-ie7.js"></script>
    <![endif]-->
  </head>

    """) % title

    return (__head__)


#------------------------------------------------------------------------------

def headreports(title):
    __head__ = ("""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>


    <!-- Bootstrap CSS -->    
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <!-- bootstrap theme -->
    <link href="../css/bootstrap-theme.css" rel="stylesheet">
    <!--external css-->
    <!-- font icon -->
    <link href="../css/elegant-icons-style.css" rel="stylesheet" />
    <link href="../css/font-awesome.min.css" rel="stylesheet" />    
    <!-- Custom styles -->
    <link href="../css/style.css" rel="stylesheet">
    <link href="../css/style-responsive.css" rel="stylesheet" />

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 -->
    <!--[if lt IE 9]>
      <script src="../js/html5shiv.js"></script>
      <script src="../js/respond.min.js"></script>
      <script src="../js/lte-ie7.js"></script>
    <![endif]-->
  </head>
    """) % title

    return (__head__)


#------------------------------------------------------------------------------

def navbar(menuhtml):

    
    __navbar__ = ("""
  <body>
  <!-- container section start -->
  <section id="container" class="">
     
      
      <header class="header dark-bg">
            <div class="toggle-nav">
                <div class="icon-reorder tooltips" data-original-title="Toggle Navigation" data-placement="bottom"></div>
            </div>

            <!--logo start-->
            <a href="" class="logo">Common Criteria (non official) Parser<span class="lite"> Use by your own risk</span></a>
            <!--logo end-->

      </header>      
      <!--header end-->


      <!--sidebar start-->
      <aside>
          <div id="sidebar"  class="nav-collapse ">
              <!-- sidebar menu start-->
              <ul class="sidebar-menu">                
                  <li class="active">
                      <a class="" href="%s">
                          <i class="icon_house_alt"></i>
                          <span>Dashboard</span>
                      </a>
                  </li>


    """) % (menuhtml['cc'])

    __navbar__ += ("""

                    <li>
                          <a class="" href="reports/%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart1</span>
                          </a>
                      </li>
                    <li>
                          <a class="" href="reports/%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart2</span>
                          </a>
                      </li>
                    <li>
                          <a class="" href="reports/%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart3</span>
                          </a>
                      </li>
                           <li>
                          <a class="" href="reports/%s">
                              <i class="icon_shield_alt"></i>
                              <span>CEM</span>
                          </a>
                      </li>
        """) % (menuhtml['cc1'], menuhtml['cc2'],menuhtml['cc3'],menuhtml['cem'])

    __navbar__ += ("""
  
              </ul>
              <!-- sidebar menu end-->
          </div>
      </aside>
      <!--sidebar end-->

    """)

    return (__navbar__)


#------------------------------------------------------------------------------


def navbarreports(menuhtml):

    __navbar__ = ("""

  <body>
  <!-- container section start -->
  <section id="container" class="">
     
      
      <header class="header dark-bg">
            <div class="toggle-nav">
                <div class="icon-reorder tooltips" data-original-title="Toggle Navigation" data-placement="bottom"></div>
            </div>

            <!--logo start-->
            <a href="" class="logo">Common Criteria (non official) Parser<span class="lite"> Use by your own risk</span></a>
            <!--logo end-->

      </header>      
      <!--header end-->


      <!--sidebar start-->
      <aside>
          <div id="sidebar"  class="nav-collapse ">
              <!-- sidebar menu start-->
              <ul class="sidebar-menu">                
                  <li class="active">
                      <a class="" href="../%s">
                          <i class="icon_house_alt"></i>
                          <span>Dashboard</span>
                      </a>
                  </li>

    """) % (menuhtml['cc'])


    __navbar__ += ("""

                    <li>
                          <a class="" href="%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart1</span>
                          </a>
                      </li>
                    <li>
                          <a class="" href="%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart2</span>
                          </a>
                      </li>
                    <li>
                          <a class="" href="%s">
                              <i class="icon_shield_alt"></i>
                              <span>CCpart3</span>
                          </a>
                      </li>
                           <li>
                          <a class="" href="%s">
                              <i class="icon_shield_alt"></i>
                              <span>CEM</span>
                          </a>
                      </li>
        """) % (menuhtml['cc1'], menuhtml['cc2'],menuhtml['cc3'],menuhtml['cem'])

    __navbar__ += ("""
  
              </ul>
              <!-- sidebar menu end-->
          </div>
      </aside>
      <!--sidebar end-->

    """)

    return (__navbar__)


#------------------------------------------------------------------------------


def bodydashboard(htmlfile):
    __body__ = ("""


      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
              <!--
            <div class="row">
                <div class="col-lg-12">
                    <h3 class="page-header"><i class="fa fa-laptop"></i> Dashboard</h3>
                    <ol class="breadcrumb">
                        <li><i class="fa fa-home"></i><a href="%s">Home</a></li>
                        <li><i class="fa fa-laptop"></i>Dashboard</li>                          
                    </ol>
                </div>
            </div>
            -->

    """) % (htmlfile)

    return (__body__)


#------------------------------------------------------------------------------


def tablecontent(menuhtml):
    keylist = menuhtml.keys()
    sorteddict = sorted(keylist, key=int) 

    __body__ = ("""

            <div class="col-lg-12">
                      <!--Project Activity start-->

                      <section class="panel">
                          <div class="panel-body progress-panel">
                            <div class="row">
                              <div class="col-lg-8 task-progress pull-left">
                                  <h1>Chapters</h1>                                  
                              </div>
                                <div class="col-lg-12">
                                <!--
                                <span class="profile-ava pull-right">
                                        <img alt="" class="simple" src="img/avatar1_small.png">
                                        Auditor
                                </span>        
                                -->                        
                              </div>
                            </div>
                          </div>
                          <table class="table table-hover">
                              <tbody>

    """)

    for key in sorteddict:
        htmlfile = key + ".html"
        __body__ += ("""

                      <tr>
                          <!--<td>%s</td> --><td>%s</td>

                      </tr>
       
        """)% (key, menuhtml[key])


    __body__ += ("""

                              </tbody>
                          </table>
                      </section>
                  </div>

                <pre>
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
                </pre>

              </div><br><br>
    """)

    return (__body__)


#------------------------------------------------------------------------------


def bodyblank():
    __body__ = ("""


      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">

    """)

    return (__body__)

#------------------------------------------------------------------------------


def bodytitle(title, href):
    __title__ = ("""<a name="%s"></a>

                <div class="col-lg-12">  
                    <h3><strong>%s</strong></h3>  
                </div>  
    <br>

    """) % (href, title)

    return (__title__)

#------------------------------------------------------------------------------


def bodytitle_subclase(title, href):
    __title__ = ("""<a name="%s"></a>

                <div class="col-lg-12">  
                    <h4><strong>%s</strong></h4>  
                </div>  
    <br>

    """) % (href, title)

    return (__title__)


#------------------------------------------------------------------------------


def bodytitle_figure(title, entity, width, height):
    __title__ = ("""
        <br><br>
        <center>
        <img src="%s" alt="%s">
        <br><br>
        <strong>Figure %s</strong>
        </center>
        <br><br>
    """) % (entity,title,title)

    return (__title__)



#------------------------------------------------------------------------------


def bodyinfo(childtext):
    __bodyinfo__ = ("""
        <div class="col-lg-12">
            <p>%s</p>
        </div>
        """) % (childtext)

    return (__bodyinfo__)

#------------------------------------------------------------------------------


def bodyinfolist():
    __bodyinfo__ = ("""
        <ol type="a">
        """)

    return (__bodyinfo__)

#------------------------------------------------------------------------------


def bodyinfolistend():
    __bodyinfo__ = ("""
        </ol>
        """)

    return (__bodyinfo__)

#------------------------------------------------------------------------------


def bodyinfotable():
    __bodyinfo__ = ("""
        <table border='1' width=90%>
        """)

    return (__bodyinfo__)


#------------------------------------------------------------------------------


def bodyinfotr():
    __bodyinfo__ = ("""
        <tr>
        """)

    return (__bodyinfo__)


#------------------------------------------------------------------------------


def bodyinfotrend():
    __bodyinfo__ = ("""
        </tr>
        """)

    return (__bodyinfo__)


#------------------------------------------------------------------------------


def bodyinfotableend():
    __bodyinfo__ = ("""
        </table>
        """)

    return (__bodyinfo__)

#------------------------------------------------------------------------------


def bodyinforowth(childtext, columnspan):
    __bodyinfo__ = ("""
        <th colspan="%s" style="text-align:center">
            %s
        </th>
        """) % (columnspan, childtext)

    return (__bodyinfo__)
#------------------------------------------------------------------------------


def bodyinforowtd(childtext):
    __bodyinfo__ = ("""
        <td style="text-align:left">
            %s
        </td>
        """) % (childtext)

    return (__bodyinfo__)


#------------------------------------------------------------------------------


def bodyinfoitem(childtext):
    __bodyinfo__ = ("""
        <li>
            %s
        </li>
        """) % (childtext)

    return (__bodyinfo__)


#------------------------------------------------------------------------------

def bodyend():
    __bodyend__ = ("""
                    <br><br><br><br><br><br><br><br><br>
                          <div class="col-lg-12">
            <div class="text-center">
                <br>
                Nice Admin - Creative - Bootstrap 3 Responsive Admin Template
                <br>
                Author GeeksLabs
            </div>
          </div>
          </section>
      </section>
      <!--main content end-->
  </section>
  <!-- container section start -->
    """)

    return (__bodyend__)


#------------------------------------------------------------------------------

def bodyjsend():

    __bodyjsend__ = ("""


    <!-- javascripts -->
    <script src="js/jquery.js"></script>
    <script src="js/jquery-ui-1.10.4.min.js"></script>
    <script src="js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-1.9.2.custom.min.js"></script>
    <!-- bootstrap -->
    <script src="js/bootstrap.min.js"></script>
    <!-- nice scroll -->
    <script src="js/jquery.scrollTo.min.js"></script>
    <script src="js/jquery.nicescroll.js" type="text/javascript"></script>


    <!--custome script for all page-->
    <script src="js/scripts.js"></script>
  


    """)

    return (__bodyjsend__)

#------------------------------------------------------------------------------


def bodyendhtmljs():
    __bodyendhtml__ = ("""
                    <br><br><br><br><br><br><br><br><br>
                          <div class="col-lg-12">
            <div class="text-center">
                <br>
                Nice Admin - Creative - Bootstrap 3 Responsive Admin Template
                <br>
                Author GeeksLabs
            </div>
          </div>


          </section>
      </section>
      <!--main content end-->
  </section>
  <!-- container section start -->


    <!-- javascripts -->
    <script src="../js/jquery.js"></script>
    <script src="../js/jquery-ui-1.10.4.min.js"></script>
    <script src="../js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="../js/jquery-ui-1.9.2.custom.min.js"></script>
    <!-- bootstrap -->
    <script src="../js/bootstrap.min.js"></script>
    <!-- nice scroll -->
    <script src="../js/jquery.scrollTo.min.js"></script>
    <script src="../js/jquery.nicescroll.js" type="text/javascript"></script>


    <!--custome script for all page-->
    <script src="../js/scripts.js"></script>
  

  </body>
</html>
    """)

    return (__bodyendhtml__)

#------------------------------------------------------------------------------


def bodyendhtml():
    __bodyendhtml__ = ("""
  </body>
</html>
    """)

    return (__bodyendhtml__)


