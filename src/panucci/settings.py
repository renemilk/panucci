# -*- coding: utf-8 -*-
#
# This file is part of Panucci.
# Copyright (c) 2008-2011 The Panucci Project
#
# Panucci is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Panucci is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Panucci.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

import logging
import panucci
import os.path
import ConfigParser
from panucci import util

CONFIG_FOLDER = os.path.expanduser('~/.config/panucci')

if not os.path.exists(CONFIG_FOLDER):
    import os
    os.mkdir(CONFIG_FOLDER)

if not os.path.exists(CONFIG_FOLDER + '/panucci.conf'):
    import shutil
    _filepath = util.find_data_file("panucci.conf")
    shutil.copy(_filepath, CONFIG_FOLDER)

class Settings(object):
    def __init__(self):
        self.__log = logging.getLogger('panucci.settings.Settings')
        self.config = ConfigParser.SafeConfigParser()
        # Parse everything
        _file = open(util.find_data_file("panucci-all.conf"))
        self.config.readfp(_file)
        _file.close()
        # Parse non editable 
        if os.path.exists(CONFIG_FOLDER + '/panucci-noedit.conf'):
            _file = open(CONFIG_FOLDER + "/panucci-noedit.conf")
            self.config.readfp(_file)
            _file.close()
        # Parse editable
        _file = open(CONFIG_FOLDER + "/panucci.conf")
        self.config.readfp(_file)
        _file.close()
    """
    def __getattr__(self, key):
        if DEFAULTS.has_key(key):
            # FIXME: Load settings from somewhere
            return DEFAULTS[key]
        else:
            self.__log.warning('Setting "%s" doesn\'t exist.' % key)
            raise AttributeError

    def __setattr__(self, key, value):
        if DEFAULTS.has_key(key):
            if type(value) == type(DEFAULTS[key]):
                # Don't set the value if it's the same as it used to be
                #if getattr(self, key) != value:
                # FIXME: Save setting somewhere

                return True
            else:
                self.__log.warning(
                    'Type of "%s" (%s) does not match default type (%s)',
                    key, type(value).__name__,
                    type(DEFAULTS[key]).__name__ )
        else:
            object.__setattr__( self, key, value )
            self.__log.warning('Setting "%s" doesn\'t exist.', key)

        return False

    def attach_checkbutton(self, button, setting):
        button.connect(
            'toggled', lambda w: setattr( self, setting, w.get_active()) )
        #self.register(
        #    setting + SIGNAL_NAME_SUFFIX, lambda v: button.set_active(v) )
        button.set_active( getattr(self, setting) )
     """
settings = Settings()
