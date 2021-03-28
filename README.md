Bibi Calibre Plug-in
================================================================================================================================

Bibi EPUB reader plug-in for calibre.


Summary
--------------------------------------------------------------------------------------------------------------------------------

Bibi is a browser based pretty-looking EPUB reader.
Bibi can handle EPUB which uses vertical writing system well, so this plug-in
is mainly intended for people using vertical writing system.
But Bibi itself is very good EPUB reader so maybe useful for others.

Bibi calibre plug-in makes it easy to read EPUB files on calibre library
using Bibi. You don't need to install Bibi. Just install this plug-in,
select an epub book, and click button, that all!


### About Bibi

* EPUB 3+ and 2 compliant. Supports both reflowable and fixed-layout books of various language.
* Made with JavaScript. Works compatibly with all major web browsers on various OS/devices.
* Free. Open source software released under the MIT License.
* [Bibi's web site](http://bibi.epub.link/)
* [Bibi's GitHub repositoly page](https://github.com/satorumurmur/bibi)


Table of Contents
--------------------------------------------------------------------------------------------------------------------------------

1. How to build
2. How to setup
3. How to use
4. License


--------------------------------------------------------------------------------------------------------------------------------


How to build
--------------------------------------------------------------------------------------------------------------------------------

### Requirements
* calibre >= 5
* python >= 3.6
* python-setuptools >= 30.3.0

### Arrangements
1. Clone [this repository](https://github.com/KazuSoap/bibi_calibre).
2. `$ cd <the local repository>`
3. Use the following command while in the local repository then you can find the plug-in .zip.

    `$ python setup.py`


How to setup
--------------------------------------------------------------------------------------------------------------------------------

1. Build the plug-in zip file.
2. In Calibre choose **Preferences->Plugins**. Click the **Load plugin from file** button to browse to your plug-in .zip file and click OK.
3. You are asked which toolbars/menus you would like the plugin to appear on.
Main toolbar is a plain choice but any toolbars/menus should work.
4. Restart calibre.


How to use
--------------------------------------------------------------------------------------------------------------------------------

Select a book which has an EPUB format and press plug-in's action button.

Bibi calibre plug-in opens Bibi using platform's default web browser by default.
If you want to open Bibi using other browser, go to plug-in preference and
specify command you want to use.


License
--------------------------------------------------------------------------------------------------------------------------------

### Bibi Calibre Plug-in

* &copy; [Daisuke Cato](https://github.com/dcato/bibi_calibre)
* Licensed under [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
