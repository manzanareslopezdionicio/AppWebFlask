from flask import Flask, render_template

app = Flask (__name__)
   
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') 

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguaje')
def lenguaje():
    return render_template('lenguaje.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/tarea')
def tarea():
    return render_template('tarea.html')


if __name__ == '__main__':
    app.run(debug=True)