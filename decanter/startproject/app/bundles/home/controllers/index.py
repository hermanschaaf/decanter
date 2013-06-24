#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bottle import static_file
from decanter.lib.decorator import get
from decanter.lib.config import Config

@get('/')
@get('/hello/<name>')
def home(name=u'世界'):
    return {'greeting': u"Hello {0}!".format(name.title())}

@get('/favicon.ico')
def favicon():
    config = Config.get_instance()
    dirpath = os.path.join(config.apppath, config.assets_path)
    return static_file('images/favicon.ico', root=dirpath)

@get('/json', apply='json', skip='jinja2')
def index():
    return {'word': u'Hello 世界!'}

    