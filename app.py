# imports
from flask import Flask, render_template, request, redirect, send_file, url_for, flash
from config import DevelopmentConfig
from jinja2 import Environment, FileSystemLoader
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# imports from modules
from logic.BackGroundDeletion import BackgroundDeletion

# global
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

## --------------------------- Endpoints for every module ------------------------------------

# Endpoint for the app view

@app.route('/')
def init():
    return index("")

@app.route('/index')
def index(message):
    return render_template('index.html', message = message)

@app.route('/erase_bckgnd', methods=['POST'])
def erase_background():
    message = ""
    try:
        if request.method == "POST":
            file = request.files['img']
            if file and allowed_file(file.filename):
                delete = BackgroundDeletion(secure_filename(file.filename))
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                input_path,output_path = delete.delete_background(delete.save_image())
                in_name, out_name = delete.get_names()
        message = "¡Fondo de tu imagen borrada con exito!"
        return render_template('bckgnd_erased.html',message = message, in_path = input_path ,del_path = output_path, in_name = in_name, out_name = out_name)
    except Exception as e:
        message = str(e)
    return render_template('index.html', message = message)

@app.route('/download_image', methods=['POST'])
def download_image():
    message = ""
    try: 
        return send_file(request.form['output'], as_attachment=True)
    except Exception as e:
        message = str(e)
    return render_template('index.html',message = message)

#service for saving files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# app start
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.run(debug=True)
