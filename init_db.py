#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from app.models import User
import hashlib

db.create_all()

# create admin user

m = hashlib.md5()
m.update('123456')
pwd = m.hexdigest()

admin = User('admin', pwd)
db.session.add(admin)
db.session.commit()