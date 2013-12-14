# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('python-webkit')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('python_webkit')

from python_webkit_lib import Window
from python_webkit.AboutPythonWebkitDialog import AboutPythonWebkitDialog
from python_webkit.PreferencesPythonWebkitDialog import PreferencesPythonWebkitDialog

# See python_webkit_lib.Window.py for more details about how this class works
class PythonWebkitWindow(Window):
    __gtype_name__ = "PythonWebkitWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(PythonWebkitWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutPythonWebkitDialog
        self.PreferencesDialog = PreferencesPythonWebkitDialog

        # Code for other initialization actions should be added here.

