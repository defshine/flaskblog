from app import db


class User(db.Model):
    user_id = db.Column(db.BIGINT, primary_key=True)
    user_name = db.Column(db.VARCHAR(64))
    user_qq = db.Column(db.VARCHAR(16))
    user_mail = db.Column(db.VARCHAR(64))
    password = db.Column(db.VARCHAR(128))

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


class Category(db.Model):
    cat_id = db.Column(db.BIGINT, primary_key=True)
    cat_name = db.Column(db.VARCHAR(128))
    cat_description = db.Column(db.VARCHAR(256))
    cat_parent = db.Column(db.BIGINT)

    def __init__(self, cat_id, cat_name, cat_description, cat_parent):
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




