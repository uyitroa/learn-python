from bottle import *
@route('/say/<name>')
def said(name):
	return template('You have just said {{nom}}',nom=name)
run(host='localhost',port=8080,debug=True)
