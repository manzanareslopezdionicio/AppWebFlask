from flask import Flask, render_template

app = Flask (__name__)

""" @app.route('/')
def principal():
    return "Bienvenidos o bienvenida a mi sitio web con PYTHON"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contactos HOY"

@app.route('/lenguajeprogramacion')
def lenguajes():
    return "Esta es la pagina de lenguajes de programación" """
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html') 

@app.route('/lenguaje')
def lenguaje():
    return render_template('lenguajeprogramacion.html')

if __name__ == '__main__':
    app.run(debug=True)