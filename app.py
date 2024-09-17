from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask (__name__)

#app.secret_key = 'appsecretkey'

mysql=MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'dmanzanares'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'crud'
app.config['MYSQL_CURSORCLASS']='DictCursor' #Diccionario de la database
mysql.init_app(app)

#CONSULTAR LA BASE DE DATOS 
@app.route('/cliente')
def cliente():
    
    sql = "SELECT * FROM cliente"
    
    conexion = mysql.connection #
    cursor = conexion.cursor()
    cursor.execute(sql) #EJE
    clientes = cursor.fetchall() #RECUPERAR LA VARIABLE
    conexion.commit()
    return render_template('cliente.html', clientes=clientes)

#INSERTAR DATOS A LA BASE DE DATOS
@app.route('/guardar', methods=['POST'])
def insertar():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cliente(name,email,phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('cliente'))


#ELIMINAR UN REGISTRO DE LA BASE DE DATOS
@app.route('/borrar/<int:id>', methods = ['GET'])
def borrar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cliente WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('cliente'))

#EDITAR DATOS DE LA BASE DEATOS
@app.route('/edit/<int:id>') 
def edit(id):
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM cliente WHERE id=%s", (id,))
    clientes=cursor.fetchone()
    conexion.commit()
    return render_template('editar.html', clientes=clientes)
    
    '''
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    
    sql = "INSERT INTO cliente(name, email, phone), VALUES(%s, %s, %s)"
    datos = (name, email, phone)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/cliente')
    
    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM ciente")
    #data = cur.fetchall()
    #cur.close()
    return render_template('/cliente.html', cliente=data)


#INSERTAR DATOS A LA BASE DE DATOS
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Datos insertados satisfactoriamente.")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cliente(name,email,phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('tarea'))

#ACTUALIZAR DATOS EN LA BASE DE DATOS
@app.route('/update', methods= ['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE cliente SET name=%s, email=%s, phone=%s
        WHERE id=%s
        """, (name, email, phone, id_data))
        #mysql.connection.commit()
        flash("Los datos se Actualizaron Satisfactoriamente")
        return redirect(url_for('tarea'))

#ELIMINAR UN REGISTRO DE LA BASE DE DATOS
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cliente WHERE id=%s", (id_data,))
    mysql.connection.commit()
    flash("El registro se ha eliminado correctamente.")
    #mysql.close()
    return redirect(url_for('tarea'))
'''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html') 

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