from flask import Flask

app = Flask (__name__)

@app.route('/')
def principal():
    return "Bienvenidos o bienvenida a mi sitio web con PYTHON"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contactos"

@app.route('/lenguajeprogramacion')
def lenguajes():
    return "Esta es la pagina de lenguajes de programación"

if __name__ == '__main__':
    app.run(debug=True, port=5017)