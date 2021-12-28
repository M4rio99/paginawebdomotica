from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def Inicio():
    return render_template('home.html')

@app.route('/Sobre_nosotros')
def Acerca_de_nosotros():
    return render_template('informacion.html')

@app.route('/contactanos')
def contacto():
    return render_template('contacto.html')

@app.route('/Instalacioncctv')
def Instalacionescctv():
    return render_template('CCTV.html')

@app.route('/Home_cctv')
def Home_cctv():
    return render_template('home_cctv.html')

@app.route('/Home_oficina')
def Home_oficina():
    return render_template('home_oficina.html')

@app.route('/Home_cocina')
def Home_cocina():
    return render_template('home_cocina.html')

@app.route('/Home_recamaras')
def Home_recamara():
    return render_template('home_recamara.html')

@app.route('/Home_jardín')
def Home_jardín():
    return render_template('home_jardín.html')

@app.route('/Home_salas')
def Home_sala():
    return render_template('home_sala.html')

@app.route('/Redes_sociales')
def redes():
    return render_template('redes.html')






if __name__ == '__main__':
    app.run(debug=True)