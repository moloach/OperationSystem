# coding=utf-8
import os
from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.mail import Mail, Message
from threading import Thread

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_SUBJECT_PREFIX'] = '[systemmail]'
app.config['MAIL_SENDER'] = 'engoo admin <fanf@engoo.cn>'

manager = Manager(app)
mail = Mail(app)

@app.route('/mail')
def email():
	user = 'ok'
	# user.name = 'jack'
	send_mail('183924638@qq.com', 'Test mail', 'mail/mail', user=user)
	return 'ok'
#显示已发送的文件


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)
#异步发送邮件

def send_mail(to, subject, template, **kwargs):
	msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + subject,
		sender=app.config['MAIL_SENDER'], recipients=[to])

	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)

	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr



manager.run()
