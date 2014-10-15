#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.contrib.fixers import ProxyFix
from app import create_app

app = create_app()

app.wsgi_app = ProxyFix(app.wsgi_app)

app.run(host='0.0.0.0')

