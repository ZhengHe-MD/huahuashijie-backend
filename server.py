from os import path
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

API = '/flower'

PWD = path.abspath('.')
UPLOAD_FOLDER = path.join(PWD, 'files')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route(API, methods = ['GET', 'POST'])
def flowerAPI():
    if request.method == 'POST':
        if ('file' not in request.files):
            print('No file part')
            return 'no file part'
        f = request.files['file']

        if f.filename == '':
            print('No selected file')
            return 'No selected file'
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
    return 'this is huahushijie flowerAPI'
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''
