from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/") #Llamamos a la página principal
def front_page():
    return render_template('index.html')

@app.route("/cv") #Llamamos a la página del cv
def cv():
    return render_template('cv.html')

@app.route("/contact",methods=['GET','POST']) #Llamamos a la página principal
def contact(): #Usamos métodos para mostrar la página de confirmación
    if request.method == 'GET': #Si todavía no tenemos datos usamos GET
        return render_template('contact.html',form = True)
    name = request.form['name']
    email = request.form['email']
    if request.method == 'POST': #Si es post, indicamos que queremos mostrar la página de confirmación
        return render_template('contact.html',form = False, name=name,email=email)

#flask --app practica3 run EJECUTAR EN TERMINAL PARA VER
