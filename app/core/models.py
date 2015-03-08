from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import current_user
from flask.ext.cache import Cache

db = SQLAlchemy()
cache = Cache()


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Unicode(64))
    user_qq = db.Column(db.Unicode(16))
    user_mail = db.Column(db.Unicode(64))
    password = db.Column(db.Unicode(128))

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

   # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def __unicode__(self):
        return self.user_name


class Post(db.Model):

    __tablename__ = 'post'

    post_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    author_id = db.Column(db.BIGINT, db.ForeignKey('user.user_id'))
    post_date = db.Column(db.DateTime)
    post_content = db.Column(db.UnicodeText)
    post_title = db.Column(db.Unicode(256))
    category_id = db.Column(db.BIGINT, db.ForeignKey('category.cat_id'))
    post_modified_date = db.Column(db.DateTime)
    category = db.relationship('Category', backref='post')
    author = db.relationship('User', backref='post')

    def __init__(self):
        self.post_modified_date = datetime.now()
        self.author_id = current_user.user_id
        self.post_date = datetime.now()

    def __unicode__(self):
        return self.user_name

    def to_json(self):
        return {
            'post_id': self.post_id,
            'author': self.author.user_name,
            'post_date': self.post_date,
            'post_content': self.post_content,
            'post_title': self.post_title,
            'category': self.category.cat_name,
            'post_modified_date': self.post_modified_date,
        }


class Category(db.Model):

    __tablename__ = 'category'

    cat_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    cat_name = db.Column(db.Unicode(128))
    cat_description = db.Column(db.Unicode(256))

    def __unicode__(self):
        return self.cat_name

    @staticmethod
    def list_category():
        categories = Category.query.all()
        return [c.to_json() for c in categories]

    def to_json(self):
        return {
            'cat_id': self.cat_id,
            'cat_name': self.cat_name,
            'cat_description': self.cat_description
        }


class Blogroll(db.Model):

    __tablename__ = 'blogroll'

    br_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    br_name = db.Column(db.Unicode(128))
    br_url = db.Column(db.Unicode(256))

    def __unicode__(self):
        return self.br_name

    @staticmethod
    def list_blogroll():
        blogrolls = Blogroll.query.all()
        return [b.to_json() for b in blogrolls]

    def to_json(self):
        return {
            'br_id': self.br_id,
            'br_name': self.br_name,
            'br_url': self.br_url
        }


