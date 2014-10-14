from wtforms import form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms import validators
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from app.core.models import db, User


class LoginForm(form.Form):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def validate_username(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(user_name=self.username.data).first()