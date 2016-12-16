#coding=utf-8
"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template, Flask, session, redirect,url_for, flash, request
from emailuoOperationSystem import app
from emailuoOperationSystem import database
from emailuoOperationSystem import check_server

from flask_wtf import FlaskForm, CsrfProtect
from wtforms import StringField,SubmitField, IntegerField, SelectMultipleField, validators 
from wtforms.validators import Required


app.secret_key = '4a1352f8d113d22e'
app.config['SECRET_KEY'] = '4a1352f8d113d22e'
CsrfProtect(app)

class InstanceForm(FlaskForm):
    #name = StringField(validators = [Required()])
    #text field 
    server_name = StringField([validators.Required()])
    IP_address = StringField([validators.Required()])
    OS = StringField([validators.Required()])
    note = StringField( [validators.Required()])
    port = IntegerField( [validators.Required()])
    cycle = IntegerField([validators.Required()])
    server_type = StringField( [validators.Required()])
    submit = SubmitField('Submit')
    #submit button

data = database.Database()
#checks = check_server.check_server()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    server_status = data.get_logging_status()
    servers = data.get_host()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        comments = servers
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
    server_data = data.get_host()
    server_status = data.get_logging_status() 
    print server_status
    #server_data = server_data + server_status
    if server_status == []:
        server_status = ['check error']
    
    return render_template(
        'serverManagement.html',
        title='serverManagement',
        year=datetime.now().year,
       comments = server_data,
       status = server_status
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
        return redirect(url_for('serverManagement'))
    else:
        flash("error occured, please try again!")
        return redirect(url_for('home'))

@app.route('/editServer/<serverId>')
def editServer(serverId):
    return render_template()

@app.route('/addServer',methods = ["GET","POST"])
def addServer():
    form = InstanceForm()
    if request.method == 'POST':
        if  form.validate_on_submit():             
            post_format = {
            'server_name':form.server_name.data,
            'IP_address':form.IP_address.data,
            'OS':form.OS.data,
            'note':form.note.data,
            'port':form.port.data,
            'cycle':form.cycle.data,
            'server_type':form.server_type.data
            }
            #use the form['OS'] will fail because the form['XX'] is a StringField Object
            result = data.add_host(post_format)
            if result == True:
                return redirect('serverManagement')
            else:
                flash("The Form have some error!")
                return render_template('error.html',form = form)
        else:
            return redirect('/')
    else:
        return render_template('serverAdd.html',
                               form = form)
'''
@app.route('/addServer',methods = ["GET","POST"])
def addServer():
    name =None
    form = InstanceForm()
    if not form.validate_on_submit():
        name = form['name']
        #form['name'] = ''
        return render_template('serverAdd.html',form = form,name = name)
    return render_template('serverAdd.html',form = form, name =name)
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title = 'Error',year = datetime.now().year), 404

@app.errorhandler(500)
def internel_server_error(e):
    return render_template('500.html',title = 'Error',year = datetime.now().year), 500


@app.route('/getHealthData')
def getHealthData():
    last_status = data.get_last_logging_status()
    servers = data.get_host()
    health_data = []
    server_data = []
    for item in last_status['status']:
        if item == '200':
            health_data.append(1)
        else:
            health_data.append(0)
    #return json.dumps(health_data)
    return health_data