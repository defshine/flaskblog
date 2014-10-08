#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models import Category

from app import db

java = Category('Java')
python = Category('Python')

db.session.add(java)
db.session.add(python)

db.session.commit()
