"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, login_manager
from flask import render_template, request, redirect, url_for, flash
from app.forms import CreateForm
from werkzeug.utils import secure_filename
from app.models import Property  

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create", methods=['POST', 'GET'])
def create():
    form= CreateForm()
    if form.validate_on_submit:
        title= form.title.data
        bedrooms= form.bedrooms.data
        bathrooms= form.bathrooms.data
        location= form.location.data
        price= form.price.data
        type= form.type.data
        description= form.description.data
        photo = request.form.get('photo')  # Obtain the file from the form submission
        if photo: 
            filename = secure_filename(photo.filename)  # Secure the filename
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Property successfully added!', 'success')
        return redirect(url_for("properties"))
    return render_template("create.html", form=form)   

@app.route("/properties", methods=["GET"])
def properties():
    properties= Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route("/properties/<propertyid>", methods=["GET"])
def property_id(propertyid):
    property= Property.query.get(propertyid)
    return render_template('property.html', property=property)

@login_manager.user_loader
def load_user(id):
    return Property.query.get(int(id))
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
