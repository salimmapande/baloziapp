from flask.app import Flask
from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, PasswordField, SubmitField
from wtforms import SelectField
from wtforms.validators import Email, Length, EqualTo, DataRequired, ValidationError
#from tamisemisystem.models import User
from baloziapp.models import District, Region

""" class RegisterForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(username = check_user.data).first()
        if user:
            raise ValidationError('This username already exists please try a different username')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Length(max=30), Email(), DataRequired()])
    password1  = PasswordField(label='Password:', validators=[Length(min=5), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Sign In')

 """
class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    password  = PasswordField(label='Password:', validators=[Length(min=5), DataRequired()])
    submit = SubmitField(label='Log In')


class BaloziForm(FlaskForm):
    name = StringField(label="Jina la kwanza: ", validators=[Length(max=50, min=2), DataRequired()])
    surname = StringField(label="Jina la Mwisho: ", validators=[Length(max=50, min=2), DataRequired()])
    nida = StringField(label="Namba ya NIDA: ", validators=[Length(max=30), DataRequired()])
    street = StringField(label="Mtaa/Kijiji: ", validators=[DataRequired()])
    neighborhood = StringField(label="Kitongoji: ", validators=[DataRequired()])
    county = StringField(label="Kata: ", validators=[DataRequired()])
    district_id = SelectField('Wilaya',coerce=int, choices=[(d.id, d.districtname) for d in District.query.all()])
    district = StringField(validators=[Length(max=50)])
    region_id = SelectField('Mkoa',coerce=int,  choices=[(r.id, r.regionname) for r in Region.query.all()])
    region = StringField(validators=[Length(max=50)], id="region")
    phonenumber = StringField(label="Namba ya simu: ", validators=[Length(max=15)])
    submit = SubmitField(label='Create')

class UpdateBaloziForm(FlaskForm):
    name = StringField(label="Jina la kwanza: ", validators=[Length(max=50, min=2), DataRequired()])
    surname = StringField(label="Jina la Mwisho: ", validators=[Length(max=50, min=2), DataRequired()])
    nida = StringField(label="Namba ya NIDA: ", validators=[Length(max=30), DataRequired()])
    street = StringField(label="Mtaa: ", validators=[DataRequired()])
    neighborhood = StringField(label="Kitongoji: ", validators=[DataRequired()])
    county = StringField(label="Kata: ", validators=[DataRequired()])
    district_id = SelectField('Wilaya', choices=[])
    district = StringField(validators=[Length(max=50)])
    region_id = SelectField('Mkoa',  choices=[])
    region = StringField(validators=[Length(max=50)], id="region")
    phonenumber = StringField(label="Namba ya simu: ", validators=[Length(max=15)])
    submit = SubmitField(label='Badili')



class RegionForm(FlaskForm):
    regionname = StringField(label='Jina la mkoa')
    submit = SubmitField(label='Create')

class DistrictForm(FlaskForm):
   # region = Region.query
    
    districtname = StringField(label='Jina la wilaya')
    region_id = SelectField('Mkoa',  choices=[(region.id, region.regionname) for region in Region.query.all()])
    submit = SubmitField(label='Create')

