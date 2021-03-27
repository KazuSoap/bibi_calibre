# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

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
