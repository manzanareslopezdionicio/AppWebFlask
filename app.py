from flask import Flask, render_template

app = Flask (__name__)
   
@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') 
'''
@app.route('/lenguaje')
def lenguaje():
    return render_template('lenguaje.html')
'''
if __name__ == '__main__':
    app.run(debug=True)