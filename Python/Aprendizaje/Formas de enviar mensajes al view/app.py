from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = 'JHBUHDGS7YDTS67DD'

@app.route('/')
def index():
    """FORMA DE MOSTRAR MENSAJES POR MEDIO DE VARIABLES ENVIADAS AL TEMPLATE
    <NOMBRE_VARIABLE> = <MENSAJE>
    return render_template('index.html', <NOMBRE_VARIABLE>=<NOMBRE_VARIABLE>)
    """

    """FORMA DE MOSTRAR LOS MENSAJES CON JAVASCRIPT
    <NOMBRE_VARIABLE> = <BANDERA/ACTIVADOR/EL QUE DE LA SEÑAL>
    return render_template('index.html', <NOMBRE_VARIABLE>=<NOMBRE_VARIABLE>)
    """

    """ FORMA DE MOSTRAR MENSAJES POR MEDIO DE FLASH
    usuario = "Alejo"
    flash(f"Hola como estas {usuario}")
    flash(f"Hola como estas Julian")
    return render_template('index.html')
    """

    

if __name__ == '__main__':
     app.run(debug=True, port=5000)