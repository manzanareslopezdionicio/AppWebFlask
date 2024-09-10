from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask (__name__)
app.secret_key = 'appsecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dmanzanares'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'crud'

mysql =  MySQL(app)
@app.route('/tarea')
def tarea():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cliente")
    data = cur.fetchall()
    cur.close()
    return render_template('/tarea.html', cliente=data)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') 

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
'''

@app.route('/tarea')
def tarea():
    return render_template('tarea.html')
'''

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)