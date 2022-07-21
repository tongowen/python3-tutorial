from flask import render_template
from app import app


@app.route('/')
@app.route('/owen')
@app.route('/info')
def hello():
	return '你好！我是owen!!'


@app.route('/user/<name>')
def user(name):
	return name


@app.route('/tem')
def tem():
	return render_template('index.html', name='owen is handsome!')
