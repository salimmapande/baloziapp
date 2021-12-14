from flask.app import Flask
from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, PasswordField, SubmitField
from wtforms import SelectField
from wtforms.fields import DateField
from wtforms.validators import Email, Length, EqualTo, DataRequired, ValidationError
#from tamisemisystem.models import User
from baloziapp.models import Balozi, District, Region
from datetime import datetime
from wtforms import  DateField


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

class MpangajiForm(FlaskForm):
    region_id = SelectField('Mkoa',  choices=[(r.id, r.regionname) for r in Region.query.all()])
    region = StringField(validators=[Length(max=50)], id="region")
    district_id = SelectField('Wilaya', choices=[])
    district = StringField(validators=[Length(max=50)])
    baloziname = SelectField('Balozi', choices=[(b.name, b.surname) for b in Balozi.query.all()])
    
    street = StringField(label="Mtaa: ", validators=[DataRequired()])
    neighborhood = StringField(label="Kitongoji: ", validators=[DataRequired()])
    county = StringField(label="Kata: ", validators=[DataRequired()])
    nida = StringField(label="Namba ya NIDA: ", validators=[Length(max=30), DataRequired()])
    landloadname = StringField("Mwenye nyumba", validators=[Length(max=50, min=2), DataRequired()])
    lanloadphone = StringField(label="Simu ya mwenye nyumba: ", validators=[Length(max=50, min=2), DataRequired()])
    housenumber = StringField(label="Namba ya nyumba: ", validators=[Length(max=30), DataRequired()])
    tenantname = StringField(label="Jina la kwanza la mpangaji: ", validators=[DataRequired()])
    tenantsurname = StringField(label="Jina la pili la mpangaji: ", validators=[DataRequired()])
    jinsia = SelectField('Jinsia', choices=['MME', 'MKE'])
    kazi = StringField(label="Kazi ya mpangaji: ")
    guestname = StringField(label="Jina la mgeni")
    guessaddress = StringField(label="Anuwani ya Mgeni",validators=[Length(max=50)])
    datein = DateField("Tarehe ya kuingia", validators=None, format="%Y-%m-%d",  default=datetime.now())
    dateout = DateField("Tarehe ya kutoka",validators=None, format="%Y-%m-%d", default=datetime.now())
    tenantphone = StringField(label="Namba ya simu: ", validators=[Length(max=15)])
    submit = SubmitField(label='Create')



class RegionForm(FlaskForm):
    regionname = StringField(label='Jina la mkoa')
    submit = SubmitField(label='Create')

class DistrictForm(FlaskForm):
   # region = Region.query
    
    districtname = StringField(label='Jina la wilaya')
    region_id = SelectField('Mkoa',  choices=[(region.id, region.regionname) for region in Region.query.all()])
    submit = SubmitField(label='Create')

