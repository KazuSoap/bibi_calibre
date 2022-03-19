# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

"""This file is part of BiBi Calibre Plugin.

Open epub by BiBi EPUB reader

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__copyright__  = 'Copyright (C) 2016 Daisuke Cato <daisuke.cato@gmail.com>'
__version__    = '1.2.0.2'
__license__    = 'GPL v3'
__author__     = 'Daisuke Cato'
__maintainer__ = 'KazuSoap'
__url__        = 'https://github.com/KazuSoap/bibi_calibre'
__docformat__  = 'restructuredtext en'

# The class that all Interface Action plugin wrappers must inherit from
from calibre.customize import InterfaceActionBase

PLUGIN_AUTHORS = \
__author__ + ' (maintainer: ' + __maintainer__  + ')\n' + \
__copyright__  + '\n'

class ActionBibiCalibre(InterfaceActionBase):
    '''
    This class is a simple wrapper that provides information about the actual
    plugin class. The actual interface plugin class is called InterfacePlugin
    and is defined in the ui.py file, as specified in the actual_plugin field
    below.

    The reason for having two classes is that it allows the command line
    calibre utilities to run without needing to load the GUI libraries.
    '''
    name                    = 'BiBi Calibre Plugin'
    description             = 'Open epub by BiBi EPUB reader'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = PLUGIN_AUTHORS
    version                 = tuple([int(x) for x in __version__.split(".")])
    minimum_calibre_version = (5, 0, 0)

    #: This field defines the GUI plugin class that contains all the code
    #: that actually does something. Its format is module_path:class_name
    #: The specified class must be defined in the specified module.
    actual_plugin           = 'calibre_plugins.bibi_calibre.action:BibiCalibreAction'

    def is_customizable(self):
        '''
        This method must return True to enable customization via
        Preferences->Plugins
        '''
        return True

    def config_widget(self):
        '''
        Implement this method and :meth:`save_settings` in your plugin to
        use a custom configuration dialog.

        This method, if implemented, must return a QWidget. The widget can have
        an optional method validate() that takes no arguments and is called
        immediately after the user clicks OK. Changes are applied if and only
        if the method returns True.

        If for some reason you cannot perform the configuration at this time,
        return a tuple of two strings (message, details), these will be
        displayed as a warning dialog to the user and the process will be
        aborted.

        The base class implementation of this method raises NotImplementedError
        so by default no user configuration is possible.
        '''
        if self.actual_plugin_:
            from calibre_plugins.bibi_calibre.config import ConfigWidget
            return ConfigWidget(self.actual_plugin_)

    def save_settings(self, config_widget):
        '''
        Save the settings specified by the user with config_widget.

        :param config_widget: The widget returned by :meth:`config_widget`.
        '''
        config_widget.save_settings()
