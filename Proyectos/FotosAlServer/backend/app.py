from flask import request, render_template, Flask, redirect, url_for
import os

app = Flask(__name__)
fotos = []

@app.route('/subida', methods=['POST'])
def subidaImg():
    f = request.files['uploadFile']
    fn = f.filename
    f.save(os.path.join("./backend/static/images/", fn))
    fotos.append(fn)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template("images.html", fotos = fotos)

if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True, load_dotenv=True)
