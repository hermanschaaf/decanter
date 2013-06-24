#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The configuration for your development environment. We leave
the production environment setup to you.
"""

import os

debug = True

home = lambda filename: os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), filename)

host_url = 'http://localhost'

# pid file
pidfile = home("run/decanter_{0}.py")

# logging
logger = {
    # log directory path, first {0} is the port number and second {1} is the
    # date
    'filepath': home('log/decanter_{0}-{1}.log'),
    # DEBUG, INFO, WARNING, ERROR, FATAL
    'level': 'DEBUG'
}

# default routes
default = {
    'bundle': 'home',
    'controller': 'index'
}

# list of plugins names to install by default
plugins = ['jinja2']

# path to assets files
assets_path = 'assets'

# the application directory
apppath = home('app')

# session settings
session = {
    # the cookie key
    'name': 'dev_myGSession',
    # lifetime in seconds. use 0 to have the session last until the
    # until browser is closed or up to 24h
    'lifetime': 60 * 60 * 24 * 14,
    # type (class implementation of session)
    'type': 'express',
}
