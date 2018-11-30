#!/usr/bin/env python

from os.path import join, dirname
from sys import argv

from twisted.scripts.twistd import run

import scrapyd_heroku as project
import os
import base64


env = os.environ
domain = base64.b64decode(env['DOMAIN'].encode('ascii'))
ip = base64.b64decode(env['IP'].encode('ascii'))
user = base64.b64decode(env['USER'].encode('ascii'))
passwd = base64.b64decode(env['PASSWD'].encode('ascii'))


def main():
    argv[1:1] = ['-n', '-y', join(dirname(project.__file__), 'app.py')]
    run()


if __name__ == '__main__':
    main()
