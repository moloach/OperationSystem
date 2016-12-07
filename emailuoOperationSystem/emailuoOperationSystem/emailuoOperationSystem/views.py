#coding=utf-8
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, session, redirect,url_for, flash
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


@app.route('/serverDetail/<serverId>')
def serverDetail(serverId):
    return render_template(
        'serverDetail.html',
        title='serverDetail',
        year=datetime.now().year,
        comment = data.get_one_host(serverId)
        )


@app.route('/deleteServer/<serverId>')
def deleteServer(serverId):
    result = data.delete_host(serverId)
    if result :
        flash('success!')
        return redirect(url_for('serverManagement'))
    else:
        flash("error occured, please try again!")
        return redirect(url_for('home'))

@app.route('/editServer/<serverId>')
def editServer(serverId):
    return render_template()

@app.route('/addServer')
def addServer():
    form = 
    return render_template('serverAdd.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title = 'Error',year = datetime.now().year), 404

@app.errorhandler(500)
def internel_server_error(e):
    return render_template('500.html'), 500
