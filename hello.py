from flask import Flask,render_template #importar la libreria de flask
#inicializar el servidor de flask
# en mac: export FLASK_APP=hello.py
# en windows: set FLASK_APP=hello.py 

#Comando para ejecutar el servidor: flask --app hello run

#Comando para actualizar el servidor con cambios de codigo en tiempo real
#flask --app hello --debug run

#Comando especial para lanzar el servidor en un puerto diferente
#Esto se utiliza en el caso que el puerto 5000 este ocupado
#flask --app hello run -p 5001

#Comando para lanzar en modo debug y con puerto cambiado
#flask --app hello --debug run -p 5001


app = Flask(__name__)#inicializar flask en app

@app.route("/hola")#definimos la ruta donde vamos a estar ejecutando esta funcion
def hola_mundo():#retorna un string hola mundo flask
    return "hola mundo flask"

#ejercicio crear una ruta adios que retorne una despedida ejemplo: hasta pronto Rolando
@app.route("/adios")
def despedida():
    return "Hasta pronto Jorge!!!"

#ejemplo para enviar parametros en las rutas
@app.route("/nombre/<n>")
def name(n):
    return f"Tu nombre es {n}"

#ejercicio realizar una ruta con parametro que devuelve el cuadrado de un numero
@app.route("/numero/<int:n1>/<int:n2>")#podemos asignar tipo de parametro en la ruta int,float, str
def cuadrado(n1,n2):
    return f"La suma es {n1+n2}"

#ejercicio realizar un ruta que dinamicamente pueda solicitar realizar
# operaciones de suma,resta,multiplicacion y division segun los parametros 
# pasados por ruta url
            #operaciones/10/5/suma #retornar La suma es 15
@app.route('/operaciones/<float:n1>/<float:n2>/<ope>')
def calculadora(n1,n2,ope):
    if ope=="sum":
        return render_template("hola.html",resultado=f"La suma {n1} y {n2} es {n1+n2}")
    elif ope=="res":
        return render_template("hola.html",resultado=f"La resta de {n1} y {n2} es {n1-n2}")
    elif ope=="mult":
        return render_template("hola.html",resultado=f"La multiplicacion {n1} y {n2} es {n1*n2}")
    elif ope=="div":
        return render_template("hola.html",resultado=f"La division {n1} y {n2} es {n1/n2}")          

#ejemplo de como devolver un html por flask

@app.route("/primerhtml/<nombre>")
def callhtml(nombre):
    return render_template("hola.html",name=nombre)
