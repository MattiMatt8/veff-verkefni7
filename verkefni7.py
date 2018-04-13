from bottle import *
import os
from beaker.middleware import SessionMiddleware

# Session
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)


username = "admin"
password = "hallo123"

@route('/')
def index():
    return template('v7/index')

@route('/lidur1')
def lidur1():
    return template('v7/lidur1')

@route('/lidur1/skra-inn',method="POST")
def skraInn():
    notandanafn = request.forms.get('notandanafn')
    lykilord = request.forms.get('lykilord')
    if notandanafn == username and lykilord == password:
        response.set_cookie("notandi",notandanafn,secret="bara-eitthvad")
        return redirect("lokad")
    else:
        return template('v7/villa',villa="Rangt notandanafn eða lykilorð")

@route('/lidur1/lokad')
def lokad():
    if request.get_cookie("notandi",secret="bara-eitthvad"):
        return template('v7/lokad')
    else:
        return template('v7/villa',villa="Þú þarft að vera skráður inn")

@route('/lidur1/skra-ut')
def skraUt():
    if request.get_cookie("notandi",secret="bara-eitthvad"):
        response.set_cookie("notandi","",expires=0)
    return redirect("/lidur1")

vorur = [
    {"Vörunafn":"Epli","Verð":500},
    {"Vörunafn":"Appelsína","Verð":600},
    {"Vörunafn":"Stóll","Verð":3000},
    {"Vörunafn":"Borð","Verð":9000},
    {"Vörunafn":"Skjávarpi","Verð":40000}
]
#sess = ["Epli":{"Vörunafn":"Epli","Magn":1}}]

@route('/lidur2')
def lidur1():
    return template('v7/lidur2',vorur=vorur)

@route('/lidur2/add/<vara>')
def add(vara):
    s = request.environ.get('beaker.session')
    voruReytur = -1
    for x in range(len(vorur)):
        if vorur[x]["Vörunafn"] == vara:
            voruReytur = x
    if voruReytur != -1:
        if s.get("Karfa"):
            for x in range(len(s["Karfa"])):
                if s["Karfa"][x]["Vörunafn"] == vara:
                    s["Karfa"][x]["Magn"] += 1
                    break
            else:
                s["Karfa"].append({"Vörunafn":vara,"Magn":1,"Reytur":voruReytur})
        else:
            s["Karfa"] = [{"Vörunafn":vara,"Magn":1,"Reytur":voruReytur}]
        s.save()
    else:
        return template("./v7/villa2",villa="Vara ekki til")
    return redirect('/lidur2/karfa')

@route('/lidur2/eyda')
def eyda():
    s = request.environ.get('beaker.session')
    s.delete()
    return template("./v7/villa2",villa="Öllu hefur verið eytt úr körfunni")

@route('/lidur2/karfa')
def karfa():
    s = request.environ.get('beaker.session')
    if s.get("Karfa"):
        return template('./v7/karfa',karfa=s["Karfa"],vorur=vorur)
    else:
        return template("./v7/villa2",villa="Ekkert í körfunni")

@route('/css/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./v7/css')

@error(404)
def villa404(error):
    return template('v7/error',villa="Error 404 Síða fannst ekki")

@error(500)
def villa500(error):
    return template('v7/error',villa="Error 500 Villa í forriti")

#run(host="0.0.0.0", port=os.environ.get('PORT'), app=app)
run(host='localhost', port=80, app=app, debug=True, reloader=True)