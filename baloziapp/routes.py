from os import name, removedirs
from flask.helpers import flash, make_response
from flask_sqlalchemy import _make_table
from sqlalchemy.orm import query
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.operators import exists
from werkzeug.wrappers import request, response
from baloziapp import app, db
from flask import Flask, render_template, url_for, redirect, jsonify, request, Response
#import  pandas as pd 
#import numpy as np
import json
from sqlalchemy.sql import text
from baloziapp.forms import BaloziForm, DistrictForm, MpangajiForm, RegionForm, UpdateBaloziForm
from baloziapp.models import Balozi, District, Region


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/mkoa', methods=['GET','POST'])
def mkoa_page():
    form = RegionForm()
    if form.validate_on_submit():
        _region = Region(regionname = form.regionname.data)
        exists = db.session.query(Region.regionname).filter_by(regionname=form.regionname.data).first() is not None
        if exists:
            flash(f'The region {_region.regionname} already in database', category='danger')
        else:
            db.session.add(_region)
            db.session.commit()
            results = Region.query
            return render_template('sajili_mkoa.html', results=results, form=form)
      
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f'There was an error creating the region {errMsg}', category='danger')

    return render_template('sajili_mkoa.html', form=form)

@app.route('/wilaya', methods=['GET','POST'])
def wilaya_page():
    form = DistrictForm()
    if form.validate_on_submit():
        _district = District(districtname = form.districtname.data, region_id = form.region_id.data)
        exists = db.session.query(District.districtname).filter_by(districtname=form.districtname.data).first() is not None
        if exists:
            flash(f'The district {_district.districtname} already in database', category='danger')
        else:
        #num_rows_updated = District.query.filter_by(id=157).update(dict(districtname='Kilindi'))
        #db.session.commit()
            db.session.add(_district)
            db.session.commit()
            results = District.query
            return render_template('sajili_wilaya.html', results=results, form=form) 
      
    if form.errors != {}:
        for errMsg in form.errors.values():
            flash(f'There was an error creating the district {errMsg}', category='danger')

    return render_template('sajili_wilaya.html', form=form)



@app.route('/balozi')
def balozi_page():
     results = db.session.query(Balozi, District, Region).filter(Balozi.district_id==District.id, Balozi.region_id == Region.id).add_columns(Balozi.id, Balozi.name,Balozi.surname,Balozi.nida,Balozi.phonenumber, Balozi.street, Balozi.neighborhood ,Balozi.county, District.id, District.districtname, Region.id, Region.regionname)
     return render_template('balozi.html', results = results)
  

@app.route('/create_balozi', methods=['GET', 'POST'])
def create_balozi_page():
    form = BaloziForm()
    if form.validate_on_submit():
        if exists:
            flash(f'Namba ya NIDA {form.nida.data} imesajiliwa na balozi mwengine, hakikisha namba vizuri', category='danger')
        else:
            _balozi = Balozi(name = form.name.data.upper(), surname = form.surname.data.upper(),nida = text(form.nida.data),phonenumber = text(form.phonenumber.data), street = form.street.data.upper(), neighborhood = form.neighborhood.data.upper(), county = form.county.data.upper(), region_id = int(form.region_id.data), district_id = int(form.district_id.data), region = form.region.data.upper(), district = form.district.data.upper())
            db.session.add(_balozi)
            db.session.commit()
      
            return redirect(url_for('balozi_page'))

    if form.errors != {}:
            for errMsg in form.errors.values():
                flash(f'There was an error creating the balozi {errMsg},{form.district_id.data},{form.region_id.data}',  category='danger')
    regions = db.session.query(Region).all()
    districts = db.session.query(District).all()
    return render_template('create_balozi.html', form=form, regions = regions, districts = districts)

@app.route('/balozi_details/<id>', methods=['GET'])
def balozi_details_page(id):
    form = BaloziForm()
    balozi_details = Balozi.query.get_or_404(id)
    
    return render_template('balozi_details.html', form = form, balozi_details = balozi_details)


@app.route('/region/<region_id>')
def region(region_id):
  
    districts = District.query.filter_by(region_id=region_id).all()
    distrArray = []
    for distr in districts:
        distrObj = {}
        distrObj['id'] = distr.id
        distrObj['districtname'] = distr.districtname
        distrArray.append(distrObj)
    return jsonify({'districts' : distrArray})

@app.route('/delete_balozi/<int:id>')
def delete_balozi(id):
    task_to_delete = Balozi.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('balozi_page'))
    except:
        return 'There was a problem delete that task'

@app.route('/confirm_delete/<int:id>')
def confirm_delete(id):
    balozi_id = id
    task_to_delete = Balozi.query.get_or_404(id)
    return render_template('confirm_delete.html', balozi_id = balozi_id, task_to_delete=task_to_delete)

@app.route('/update_balozi/<int:id>', methods=['GET', 'POST'])
def update_balozi(id):

    balozi_to_update = Balozi.query.get_or_404(id)

    regions = db.session.query(Region).all()
    
    districts = District.query
    form = UpdateBaloziForm()
    form.region_id = [(region.id, region.regionname) for region in Region.query.all()]
    if request.method == 'POST':
        balozi_to_update.name = request.form['name']
        balozi_to_update.surname = request.form['surname']
        balozi_to_update.nida = request.form['nida']
        balozi_to_update.phonenumber = request.form['phonenumber']
        balozi_to_update.street = request.form['street']
        balozi_to_update.neighborhood = request.form['neighborhood']
        balozi_to_update.county = request.form['county']
        balozi_to_update.district_id = request.form['district_id']#District.query.filter_by(id = form.district_id.data).first()
        balozi_to_update.region = request.form['region']
        balozi_to_update.district = request.form['district']
        balozi_to_update.region_id = request.form['region_id']
        try:
            db.session.commit()
            return redirect(url_for('balozi_page'))  
        except:
            return 'There was an issue updating that task'        

    else:
        return render_template('update_balozi.html', balozi_to_update=balozi_to_update, regions=regions, districts=districts, form = form)

@app.route('/region/')
def statebycountry(get_state):
    regions = Region.query.filter_by(id = get_state).all()
    regionArray = []
    for region in regions:
        regionObj = {}
        regionObj['id'] = region.id
        regionObj['regionname'] = region.regionname
        regionArray.append(regionObj)
    return jsonify({'regions': regionArray})

@app.route('/districts/<int:get_city>', methods=['GET'])
def city(get_city):
    region_data = District.query.filter_by(region_id = get_city).all()
    districtArray = []
    for dist in region_data:
        distObj = {}
        distObj['id'] = dist.id
        distObj['districtname'] = dist.districtname
        districtArray.append(distObj)
    return jsonify({'districts': districtArray})

@app.route('/sajili_mpangaji', methods=['GET', 'POST'])
def sajili_mpangaji_page():
    form = MpangajiForm()
    if form.validate_on_submit():
        if exists:
            flash(f'Namba ya NIDA {form.nida.data} imesajiliwa na balozi mwengine, hakikisha namba vizuri', category='danger')
        else:
            pass
      
            return redirect(url_for('balozi_page'))

    if form.errors != {}:
            for errMsg in form.errors.values():
                flash(f'There was an error creating the balozi {errMsg},{form.district_id.data},{form.region_id.data}',  category='danger')
    regions = db.session.query(Region).all()
    districts = db.session.query(District).all()
    return render_template('sajili_mpangaji.html', form=form, regions = regions, districts = districts)
      
      
     
 

