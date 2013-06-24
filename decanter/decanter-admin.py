#! /usr/bin/env python
# -*- encoding=utf8 -*-

"""
A collection of utility functions for managing a decanter project.
Normally you would call this from the command line, such as

    decanter create myproject

which creates a base project called `myproject` to start working in.
"""

import os
import errno
import argparse
import shutil
try:
    import decanter.startproject as app
except ImportError:
    # probably running from within decanter:
    import startproject as app

def create_project(args):
    print "Creating your project..."
    project_name = args.name
    shutil.copytree(src=os.path.dirname(app.__file__), dst=project_name)
    print "Directory structure created!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='decanter-admin',
        usage='%(prog)s command [options]',
        description="Manage your Decanter project")
    subparsers = parser.add_subparsers()

    # create a sub-parser for the "create" command
    parser_create = subparsers.add_parser(
        'create', help='create a new Decanter project')
    parser_create.add_argument('name', type=str, help='name parameter')
    parser_create.set_defaults(func=create_project)

    args = parser.parse_args()
    args.func(args)
