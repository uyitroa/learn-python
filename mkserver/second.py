from bottle import *

x = input('just type: ')
@route('/hello/'+x)
def greet():
	return "What's up guys"
run(host='localhost',port=8080,debug=True)
