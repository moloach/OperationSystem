"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from emailuoOperationSystem import app
from emailuoOperationSystem import database

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField('Submit')

data = database.Database()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/mailManagement')
def mailManagement():
    """Renders the mail page."""
    #mail_app = 
    return render_template(
        'email.html',
        title='mailManagement',
        year=datetime.now().year,
        message='Your contact page.',
        current_time = datetime.utcnow()
    )

@app.route('/serverManagement')
def serverManagement():
    """Renders the server page."""
    #email.app()
    return render_template(
        'serverManagement.html',
        title='serverManagement',
        year=datetime.now().year,
       comments = data.get_host()
        #message='Your application description page.'
    )

@app.route('/serverStatus')
def serverStatus():
    """Render the ServerStatus page."""
    return render_template(
        'serverStatus.html',
        title = 'serverStatus',
        year = datetime.now().year)


@app.route('/serverDetail', methods = ['GET','POST'])
def serverDetail():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.date = ''
    return render_template(
        'serverDetail.html',
        form = form,
        name =name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title = 'Error',year = datetime.now().year), 404

@app.errorhandler(500)
def internel_server_error(e):
    return render_template('500.html'), 500
