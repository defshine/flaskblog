from app import db
from datetime import datetime


class User(db.Model):
    user_id = db.Column(db.BIGINT, primary_key=True)
    user_name = db.Column(db.VARCHAR(64))
    user_qq = db.Column(db.VARCHAR(16))
    user_mail = db.Column(db.VARCHAR(64))
    password = db.Column(db.VARCHAR(128))

    def __init__(self, user_name, password,user_qq=None, user_mail=None, user_id=None ):
        self.user_name = user_name
        self.password = password
        self.user_qq = user_qq
        self.user_mail = user_mail
        self.user_id = user_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.user_id)

    def __repr__(self):
        return '<User %r>' % self.user_name


class Post(db.Model):
    post_id = db.Column(db.BIGINT, primary_key=True)
    author_id = db.Column(db.BIGINT)
    post_date = db.Column(db.DateTime)
    post_content = db.Column(db.TEXT)
    post_title = db.Column(db.VARCHAR(256))
    post_status = db.Column(db.Integer)
    comment_status = db.Column(db.Integer)
    category_id = db.Column(db.BIGINT)
    post_modified_date = db.Column(db.DateTime)
    comment_count = db.Column(db.Integer)

    def __init__(self, author_id, post_date, post_title, post_content, post_status, category_id, post_modified_date,
                 post_id=None, comment_status=None, comment_count=None):
        self.author_id = author_id
        self.post_date = post_date
        self.post_title = post_title
        self.post_content = post_content
        self.post_status = post_status
        self.category_id = category_id
        self.post_modified_date = post_modified_date
        self.post_id = post_id
        self.comment_count = comment_count
        self.comment_status = comment_status

    @staticmethod
    def save(author_id, post_title, post_content, post_status, category_id):
        post = Post(author_id, datetime.now(), post_title, post_content, post_status, category_id, datetime.now())
        db.session.add(post)
        db.session.commit()
        return post.post_id

    @staticmethod
    def update(author_id, post_title, post_content, post_status, category_id, post_id):

        post = db.session.query(Post).filter(Post.post_id == post_id).first()
        post.post_modified_date = datetime.now()
        if post is not None:
            if author_id is not None:
                post.author_id = author_id
            if post_title is not None:
                post.post_title = post_title
            if post_content is not None:
                post.post_content = post_content
            if post_status is not None:
                post.post_status = post_status
            if category_id is not None:
                post.category_id = category_id

            db.session.commit()

    @staticmethod
    def delete(post_id):
        db.session.query(Post).filter_by(post_id=post_id).delete()
        db.session.commit()

    def to_json(self):
        return {
            'post_id': self.post_id,
            'author_id': self.author_id,
            'post_date': self.post_date,
            'post_content': self.post_content,
            'post_title': self.post_title,
            'post_status': self.comment_status,
            'comment_status': self.comment_status,
            'category_id': self.category_id,
            'post_modified_date': self.post_modified_date,
            'comment_count': self.comment_count
        }


class Category(db.Model):
    cat_id = db.Column(db.BIGINT, primary_key=True)
    cat_name = db.Column(db.VARCHAR(128))
    cat_description = db.Column(db.VARCHAR(256))
    cat_parent = db.Column(db.BIGINT)

    def __init__(self, cat_name, cat_description=None, cat_parent=None, cat_id=None):
        self.cat_id = cat_id
        self.cat_name = cat_name
        self.cat_description = cat_description
        self.cat_parent = cat_parent

    @staticmethod
    def list_category():
        categories = Category.query.all()
        return [c.to_json() for c in categories]

    def to_json(self):
        return {
            'cat_id': self.cat_id,
            'cat_name': self.cat_name,
            'cat_description': self.cat_description,
            'cat_parent': self.cat_parent
        }


class Comment(db.Model):
    comment_id = db.Column(db.BIGINT, primary_key=True)
    post_id = db.Column(db.BIGINT)
    comment_author = db.Column(db.VARCHAR(64))
    comment_author_email = db.Column(db.VARCHAR(64))
    comment_date = db.Column(db.DateTime)
    comment_content = db.Column(db.VARCHAR(256))
    comment_parent = db.Column(db.BIGINT)
    user_id = db.Column(db.BIGINT)




