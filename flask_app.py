from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_mysqldb import MySQL

app = Flask (__name__)
app.secret_key = 'appsecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dmanzanares'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'crud'

mysql =  MySQL(app)

#CONSULTAR LA BASE DE DATOS 
@app.route('/tarea')
def tarea():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cliente")
    data = cur.fetchall()
    cur.close()
    return render_template('/tarea.html', cliente=data)

#INSERTAR DATOS A LA BASE DE DATOS
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Datos insertados satisfactoriamente")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cliente(name,email,phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('/tarea'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') 

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)