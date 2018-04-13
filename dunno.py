from bottle import *
@route('/')
def index():
    return """
            <a href='/kaka'>Búa til köku</a>
            <a href='/eyda'>eyða köku</a>
            """
@route('/eyda')
def index():
    response.set_cookie("Hentai","", expires=0)
    return "kaka eyðinlögð<a href='/kaka'>Búa til köku</a>"
    
@route('/kaka')
def kaka():
    response.set_cookie("Hentai","Lover9000")
    return "kaka til <a href='/eyda'>eyða köku</a>"

run()
