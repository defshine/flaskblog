from app import db


class User(db.Model):
    user_id = db.Column(db.BIGINT, primary_key=True)
    user_name = db.Column(db.VARCHAR(64))
    user_qq = db.Column(db.VARCHAR(16))
    user_mail = db.Column(db.VARCHAR(64))
    password = db.Column(db.VARCHAR(128))

    def __repr__(self):
        return '<User %r>' % self.user_name
