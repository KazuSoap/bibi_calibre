# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

import os
import sys
import shutil
import urllib.error
import urllib.request
from setuptools import setup
from setuptools.command.build_py import build_py

_PRJ_DIR = os.path.dirname(os.path.abspath(__file__))
_BIBI_URL = 'https://github.com/satorumurmur/bibi/releases/download/v1.2.0/Bibi-v1.2.0.zip'

class make_plugin(build_py):
    prj_dir = _PRJ_DIR
    bibi_url = _BIBI_URL

    def run(self):
        package_name = os.path.basename(self.prj_dir)
        package_dir = os.path.join(self.prj_dir, package_name)
        root_zip = os.path.join(self.prj_dir, 'build', 'lib', package_name)

        # Normal build process
        build_py.run(self)

        # Download Bibi ver.1.2.0 from Github release page
        bibi_path = os.path.join(root_zip, os.path.basename(self.bibi_url))
        download_file(self.bibi_url, bibi_path)

        # make package archive
        for f in ('LICENSE', 'README.md'):
            f = os.path.join(self.prj_dir, f)
            shutil.copy(f, root_zip)

        shutil.make_archive(package_dir, 'zip', root_dir=root_zip)

        # remove tmp dirs
        for d in ('build', package_name + '.egg-info'):
            d = os.path.join(self.prj_dir, d)
            shutil.rmtree(d)

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)
        exit()

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2 or args[1] != 'mk_plugin':
        sys.argv = [args[0], 'mk_plugin']

    setup(
        cmdclass={
            'mk_plugin': make_plugin,
        },
    )
