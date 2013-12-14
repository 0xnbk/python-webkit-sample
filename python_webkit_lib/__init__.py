# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

'''facade - makes python_webkit_lib package easy to refactor

while keeping its api constant'''
from . helpers import set_up_logging
from . Window import Window
from . python_webkitconfig import get_version
