"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, session, redirect,url_for
from emailuoOperationSystem import app
from emailuoOperationSystem import database

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app.config['SECRET_KEY'] = '4a1352f8d113d22e'

class NameForm(FlaskForm):
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
        session['name'] = form.name.data
        return redirect(url_for('serverManagement'))
    return render_template(
        'serverDetail.html',
        form = form,
       # name = session.get(name)
        name = session.get(name)
        )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title = 'Error',year = datetime.now().year), 404

@app.errorhandler(500)
def internel_server_error(e):
    return render_template('500.html'), 500
