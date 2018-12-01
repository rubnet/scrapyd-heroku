#!/usr/bin/env python

from os.path import join, dirname
from sys import argv

from twisted.scripts.twistd import run

import scrapyd_heroku as project
import os
import base64


env = os.environ
def getEnv(var):
	binVar = env[var].encode('ascii') if env.get(var) else b''
	return base64.b64decode(binVar).decode('ascii')


domain = getEnv('DOMAIN')
ip = getEnv('IP')
user = getEnv('USER')
passwd = getEnv('PASSWD')


def main():
    argv[1:1] = ['-n', '-y', join(dirname(project.__file__), 'app.py')]
    run()


if __name__ == '__main__':
    main()
