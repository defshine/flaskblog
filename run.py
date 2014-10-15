#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app

app = create_app()

app.run(host='0.0.0.0')