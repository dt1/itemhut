from bottle import *

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')

# home page    
@route("/")
def index():
    return template("views/home.tpl")

debug(True)
run(reloader=True, host="localhost", port=8080)
