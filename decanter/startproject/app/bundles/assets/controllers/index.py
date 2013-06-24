#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bottle import static_file
from decanter.lib.decorator import route
from decanter.lib.config import Config


@route('/assets/<filepath:path>')
def assets(filepath):
    """
    This function delivers static files and should only be used during
    development. In production a server such as nginx should be used.
    """
    print "HELLO!"
    config = Config.get_instance()
    dirpath = os.path.join(config.apppath, config.assets_path)
    return static_file(filepath, root=dirpath)