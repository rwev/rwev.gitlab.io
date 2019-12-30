#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {
    'deploy_path': './public',
    'port': 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])


@task
def build(c):
    """Build local version of site"""
    c.run('python3 -m pelican -s pelicanconf.py')


@task
def styles(c):
    """Transpile less -> css"""
    c.run('lesscpy ./tundra/static/css/style.less ./tundra/static/css/style.css')


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('python3 -m pelican -d -s pelicanconf.py')


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('python3 -m pelican -r -s pelicanconf.py')


@task
def serve(c):
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def publish(c):
    """Build production version of site"""
    c.run('python3 -m pelican -s publishconf.py')


