from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>You have just said {{name}}</b>!', name=name)

run(host='localhost', port=8080)
