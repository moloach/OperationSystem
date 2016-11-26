"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from emailuoOperationSystem import app
import email 

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
        'mail.html',
        title='mailManagement',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/serverManagement')
def serverManagement():
    """Renders the server page."""
    #email.app()
    return render_template(
        'server.html',
        title='serverManagement',
        year=datetime.now().year,
        #message='Your application description page.'
    )
