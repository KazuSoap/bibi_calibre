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
__version__    = '1.2.0'
__license__    = 'GPL v3'
__author__     = 'Daisuke Cato'
__maintainer__ = 'KazuSoap'
__url__        = 'https://github.com/KazuSoap/bibi_calibre'
__docformat__  = 'restructuredtext en'

try:
    from PyQt5 import QtWidgets as QtGui
    from PyQt5.Qt import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
except ImportError as e:
    from PyQt4 import QtGui
    from PyQt4.Qt import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from calibre.utils.config import JSONConfig

STORE_NAME = 'Options'
KEY_PATH_BROWSER = 'pathBrowser'

DEFAULT_STORE_VALUES = {
    KEY_PATH_BROWSER: '',
}

# This is where all preferences for this plugin will be stored
plugin_prefs = JSONConfig('plugins/Bibi Calibre')

# Set defaults
plugin_prefs.defaults[STORE_NAME] = DEFAULT_STORE_VALUES

class ConfigWidget(QWidget):

    def __init__(self, plugin_action):
        QWidget.__init__(self)
        self.plugin_action = plugin_action
        layout = QGridLayout(self)
        self.setLayout(layout)

        c = plugin_prefs[STORE_NAME]

        layout.addWidget(QLabel('Browser command:', self), 0, 0)
        path_browser = c.get(KEY_PATH_BROWSER, DEFAULT_STORE_VALUES[KEY_PATH_BROWSER])
        self.path_browser_ledit = QLineEdit(path_browser, self)
        layout.addWidget(self.path_browser_ledit, 1, 0)

    def save_settings(self):
        new_prefs = {}
        new_prefs[KEY_PATH_BROWSER] = self.path_browser_ledit.text()

        plugin_prefs[STORE_NAME] = new_prefs
