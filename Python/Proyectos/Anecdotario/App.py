from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL Conexión

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'anecdotario'
mysql = MySQL(app)

#SETTINGS

app.secret_key = 'mysecretkey'

#INDEX

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    tittle = 'Menú Principal'
    return render_template('index.html', tittle = tittle)

#ESTUDIANTES

@app.route('/estudiante', methods=["POST", "GET"])
def estudiante():
    tittle = 'Estudiante'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiantes')
    datos = cur.fetchall()
    return render_template('estudiante.html', tittle = tittle, datos = datos)
    
#DOCENTE

@app.route('/docente', methods=["POST","GET"])
def docente():
    tittle = "Docente"
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM docentes')
    datos = cur.fetchall()
    return render_template('docente.html', tittle = tittle, datos = datos)

#ACUDIENTE

@app.route('/acudiente', methods=['POST', 'GET'])
def acudiente():
    tittle = 'Acudiente'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM acudientes')
    datos = cur.fetchall()
    return render_template('acudiente.html', tittle = tittle, datos = datos)

#ASIGNATURA

@app.route('/asignatura', methods=['POST', 'GET'])
def asignatura():
    tittle = 'Asignatura'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asignatura')
    datos = cur. fetchall()
    return render_template('asignatura.html', tittle = tittle, datos = datos)

#AGREGAR ESTUDIANTE

@app.route('/agg_estudiante', methods=['POST'])
def agg_estudiante():
    if request.method == "POST":
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        grado = request.form['grado']
        fecha_nac = request.form['fecha_nac']
        direccion = request.form['direccion']
        num_doc = request.form['num_doc']
        email = request.form['email']
        telefono = request.form['telefono']
        nombre_acu = request.form['nombre_acu']
        doc_acuiente = request.form['doc_acudiente']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO estudiantes (nombres, apellidos, sexo, grado, fecha_nac, direccion, num_doc, email, telefono, nombre_acu, doc_acudiente)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                    [nombres, apellidos, sexo, grado, fecha_nac, direccion, 
                    num_doc, email, telefono, nombre_acu, doc_acuiente])
        mysql.connection.commit()
        flash('Estudiante Agregado Correctamente')
        return redirect(url_for('estudiante'))

#EDITAR ESTUDIANTE

@app.route('/edit_estudiante/<id>')
def get_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM estudiantes WHERE id=%s", [id])
    dato = cur.fetchall()
    print(dato[0])
    return render_template('/editar_estudiante.html',dato = dato[0])

@app.route('/update_estudiante/<id>', methods = ['POST'])
def update_estudiante(id):
    if request.method == "POST":
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        grado = request.form['grado']
        fecha_nac = request.form['fecha_nac']
        direccion = request.form['direccion']
        num_doc = request.form['num_doc']
        email = request.form['email']
        telefono = request.form['telefono']
        nombre_acu = request.form['nombre_acu']
        doc_acudiente = request.form['doc_acudiente']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE estudiantes SET nombres = %s, 
        apellidos = %s, sexo = %s, grado = %s, fecha_nac = %s,
        direccion = %s, num_doc = %s, email = %s, telefono = %s, 
        nombre_acu = %s, doc_acudiente = %s WHERE id = %s""", 
        [nombres, apellidos, sexo, grado, fecha_nac, direccion, 
        num_doc, email, telefono, nombre_acu, doc_acudiente, id])
        mysql.connection.commit()
        flash('Estudiante Actualizado Correctamente')
        return redirect(url_for('estudiante'))

#ELIMINAR ESTUDIANTE

@app.route('/eliminar_estudiante/<string:id>')
def delete_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM estudiantes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Estudiante Eliminado Correctamente')
    return redirect(url_for('estudiante'))

#AGREGAR DOCENTE 

@app.route('/agg_docente', methods=['POST'])
def agg_docente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        asignatura = request.form['asignatura']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO docentes (nombre, apellidos, sexo, asignatura, direccion, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    [nombre, apellidos, sexo, asignatura, direccion, telefono, email])
        mysql.connection.commit()
        flash('Docente Agregado Correctamente')   
        return redirect(url_for('docente'))

#EDITAR DOCENTE

@app.route('/edit_docente/<id>')
def get_docente(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM docentes WHERE id=%s", [id])
    dato = cur.fetchall()
    print(dato[0])
    return render_template('/editar_docente.html',dato = dato[0])

@app.route('/update_docente/<id>', methods = ['POST'])
def update_docente(id):
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        asignatura = request.form['asignatura']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE docentes SET nombre = %s, 
        apellidos = %s, sexo = %s, asignatura = %s, direccion = %s, telefono = %s, 
        email = %s WHERE id = %s""", 
        [nombre, apellidos, sexo, asignatura, direccion, telefono, email, id])
        mysql.connection.commit()
        flash('Docente Actualizado Correctamente')
        return redirect(url_for('docente'))
        
#ELIMINAR DOCENTE

@app.route('/eliminar_docente/<string:id>')
def delete_docente(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM docentes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Docente Eliminado Correctamente')
    return redirect(url_for('docente'))

#AGREGAR ACUDIENTE

@app.route('/agg_acudiente', methods=['POST'])
def agg_acudiente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        num_doc = request.form['num_doc']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO acudientes (nombre, direccion, num_doc, telefono, email)
                    VALUES (%s, %s, %s, %s, %s)""",
                    [nombre, direccion, num_doc,  telefono, email])
        mysql.connection.commit()
        flash('Acudiente Agregado Correctamente')   
        return redirect(url_for('acudiente'))

#EDITAR ACUDIENTE

@app.route('/edit_acudiente/<id>')
def get_acudiente(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM acudientes WHERE id=%s", [id])
    dato = cur.fetchall()
    print(dato[0])
    return render_template('/editar_acudiente.html',dato = dato[0])

@app.route('/update_acudiente/<id>', methods = ['POST'])
def update_acudiente(id):
    if request.method == "POST":
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        num_doc = request.form['num_doc']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE acudientes SET nombre = %s, 
        direccion = %s, num_doc = %s, telefono = %s, email = %s WHERE id = %s""", 
        [nombre, direccion, num_doc,  telefono, email, id])
        mysql.connection.commit()
        flash('Acudiente Actualizado Correctamente')
        return redirect(url_for('acudiente'))

#ELIMINAR ACUDIENTE

@app.route('/eliminar_acudiente/<string:id>')
def delete_acudiente(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM acudientes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Acudiente Eliminado Correctamente')
    return redirect(url_for('acudiente'))

#AGREGAR ASIGNATURA

@app.route('/agg_asignatura', methods=['POST'])
def agg_asignatura():
    if request.method == 'POST':
        nombre = request.form['nombre']
        doc_encargado = request.form['doc_encargado']
        horas_semanales = request.form['horas_semanales']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO asignatura (nombre, doc_encargado, horas_semanales)
                    VALUES (%s, %s, %s)""",
                    [nombre, doc_encargado, horas_semanales])
        mysql.connection.commit()
        flash('Asignatura Agregado Correctamente')   
        return redirect(url_for('asignatura'))

#EDITAR ASIGNATURA

@app.route('/edit_asignatura/<id>')
def get_asignatura(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM asignatura WHERE id=%s", [id])
    dato = cur.fetchall()
    print(dato[0])
    return render_template('/editar_asignatura.html',dato = dato[0])

@app.route('/update_asignatura/<id>', methods = ['POST'])
def update_asignatura(id):
    if request.method == "POST":
        nombre = request.form['nombre']
        doc_encargado = request.form['doc_encargado']
        horas_semanales = request.form['horas_semanales']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE asignatura SET nombre = %s, 
        doc_encargado = %s, horas_semanales = %s WHERE id = %s""", 
        [nombre, doc_encargado, horas_semanales, id])
        mysql.connection.commit()
        flash('Asignatura Actualizado Correctamente')
        return redirect(url_for('asignatura'))

#ELIMINAR ASIGNATURA

@app.route('/eliminar_asignatura/<string:id>')
def delete_asignatura(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM asignatura WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Asignatura Eliminado Correctamente')
    return redirect(url_for('asignatura'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
