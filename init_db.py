#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from app.models import User

db.create_all()

# create admin user
admin = User('admin', '123456')
db.session.add(admin)
db.session.commit()