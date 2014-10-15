#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from werkzeug.contrib.fixers import ProxyFix
from app import create_app

app = create_app()

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, Debug=True)

