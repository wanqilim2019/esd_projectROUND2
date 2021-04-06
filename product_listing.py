from flask import render_template
from flask import request, redirect, url_for,flash
from werkzeug.utils import secure_filename
from main import app
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/static/images'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']




@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    return 'file uploaded successfully'
    
if __name__ == '__main__':
   app.run(port=5005,debug = True)