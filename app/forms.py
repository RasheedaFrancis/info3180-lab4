from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileField, FileAllowed,FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[
        FileRequired(),
         FileAllowed(['jpg', 'png'], 'Images only!')])
      
