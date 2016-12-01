#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2016, Daisuke Cato <daisuke.cato@gmail.com>'
__docformat__ = 'restructuredtext en'

import os
import platform
import posixpath
import subprocess
import threading
import urllib

import SocketServer
import SimpleHTTPServer

from calibre import extract
from calibre.gui2 import error_dialog
from calibre.gui2.actions import InterfaceAction
from calibre.ptempfile import PersistentTemporaryDirectory

from calibre_plugins.bibi_calibre import config


class BibiCalibreAction(InterfaceAction):

    name = 'BiBi Calibre'
    action_spec = ('BiBi Calibre', None, 'Open epub by BiB/i EPUB reader', ())
    action_type = 'current'

    def genesis(self):
        self.qaction.setIcon(get_icons('images/bibi-logo_black.png'))
        self.qaction.triggered.connect(self.open_epub_by_bibi)

    def open_epub_by_bibi(self):

        c = config.plugin_prefs[config.STORE_NAME]

        rows = self.gui.library_view.selectionModel().selectedRows()
        if not rows or len(rows) != 1:
            return error_dialog(self.gui, 'No rows selected',
                'You must select one book to perform this action.', show=True)
        book_id = self.gui.library_view.get_selected_ids()[0]
        db = self.gui.library_view.model().db
        epubpath = db.format_abspath(book_id, "EPUB", index_is_id=True)

        if not epubpath or not os.path.exists(epubpath):
            return error_dialog(self.gui, 'No EPUB file',
                'You must select a book which has EPUB format.', show=True)

        if not hasattr(self, 'httpd'):
            self._start_webserver()

        book_path = str(book_id) + "_" + str(os.stat(epubpath).st_mtime)
        book_fullpath = os.path.join(self.htmlroot, 'bookshelf', book_path)


        if not os.path.exists(book_fullpath):
            extract(epubpath, book_fullpath)

        url = 'http://localhost:' + str(self.port) + '/i/?book=' + book_path

        browser = c.get(config.KEY_PATH_BROWSER).strip()
        if browser:
            # Open url by specified browser
            cmd = browser.split()
            cmd.append(url)
            subprocess.Popen(cmd)
        else:
            # Open url using platform default browser
            if platform.system() == "Windows":
                os.startfile(url)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", url])
            else:
                subprocess.Popen(["xdg-open", url])


    def _start_webserver(self):
        '''
        setup bibi and start web server
        '''

        self.htmlroot = PersistentTemporaryDirectory()
        print(self.htmlroot)

        zipfile = os.path.join(self.htmlroot, 'bibi-0.999.4.zip')
        with open(zipfile,'wb') as f:
            f.write(self.load_resources(['bibi-0.999.4.zip']).itervalues().next())
        extract(zipfile, self.htmlroot)

        handler = RootedHTTPRequestHandler
        handler.base_path = self.htmlroot

        self.httpd = ThreadedTCPServer(('localhost', 0), handler)
        self.ip, self.port = self.httpd.server_address

        print('server started at: ', self.ip, str(self.port))

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self.httpd.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread: ", server_thread.name)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    '''
    Asynchronous Mixins
    cf. http://docs.python.jp/2/library/socketserver.html
    '''
    pass

class RootedHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''
    htmlroot specifiable SimpleHTTPRequestHandler
    cf. http://louistiao.me/posts/python-simplehttpserver-recipe-serve-specific-directory/
    '''

    def translate_path(self, path):
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = self.base_path
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        return path
