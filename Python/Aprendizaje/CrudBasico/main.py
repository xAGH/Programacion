from flask import Flask, render_template, request, url_for, redirect, flash
from mysql import connector as sql

app = Flask(__name__)
app.secret_key = "abcde"
config = {
    "host": "localhost",
    "user": "root",
    "password": "alejo23001",
    "database": "prueba"
}

db = sql.connect(**config)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', tittle = "Pagina Principal")

@app.route('/cliente')
def add_cliente():
    return render_template('agregar_cliente.html', tittle = "Agregar Cliente")

@app.route('/cliente/agregar', methods = ['POST'])
def cliente_agregar():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    telefono = request.form.get("telefono")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO clientes(nombre, apellido, telefono) VALUES('{nombre}', '{apellido}', '{telefono}')")
    db.commit()
    flash('Cliente Agregado')
    return redirect(url_for("index"))

@app.route("/cliente/ver", methods=["GET"])
def ver_cliente():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()
    return render_template("ver_clientes.html", tittle = "Visualizar clientes", data = data, cont = len(data))

@app.route("/cliente/eliminar/<uid>")
def cliente_eliminar(uid):
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM clientes WHERE id = {uid}")
    db.commit()
    return redirect(url_for('ver_cliente'))

@app.route("/cliente/editar/<uid>")
def editar_cliente(uid):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM clientes WHERE id = {uid}")
    data = cursor.fetchone()
    return render_template("editar_cliente.html", tittle = "Editar cliente", data = data)

@app.route("/cliente/edit/<uid>", methods = ["POST"])
def cliente_editar(uid):
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    telefono = request.form.get("telefono")
    cursor = db.cursor()
    cursor.execute(f"UPDATE clientes SET nombre = '{nombre}', apellido = '{apellido}', telefono = '{telefono}' WHERE id = {uid}")
    db.commit()
    return redirect(url_for("ver_cliente"))

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)