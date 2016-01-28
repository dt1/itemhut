from bottle import *

@error(404)
def error404(error):
    return "404; please press the back button"

@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static/")

@route("/products/<storefront>")
def product_store(storefront = None):
    if storefront in ["ebay", "amazon"]:
        return template("views/products")
    else:
        error404("err")

@route("/products")
def products():
    return template("views/products")

    
@route("/")
def index():
    return template("views/home.tpl")

debug(True)
run(reloader=True, host="localhost", port=8080)
