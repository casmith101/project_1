from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FloatField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class CreateForm(FlaskForm):
    title= StringField('Title', validators=[InputRequired()])
    bedrooms= IntegerField('Number of bedrooms', validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    bathrooms= IntegerField('Number of bathrooms', validators=[InputRequired()])
    price= FloatField('Price', validators=[InputRequired()])
    type= SelectField('Property Type', validators=[InputRequired()], 
        choices=[('house', 'House'), ('apartment', 'Apartment')
    ])
    description= TextAreaField('Description', validators=[InputRequired()])
    photo= FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])