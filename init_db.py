#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash

from app import db
from app.core.models import User


db.create_all()

# create admin user


admin = User('admin', generate_password_hash('123456'))

db.session.add(admin)
db.session.commit()