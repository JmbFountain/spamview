from flask import Flask
from flask import render_template
from flask import request
from flask import session
import os
import shutil
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = os.urandom(16)
def cleanup(path)
    if os.path.isdir(path):
        shutil.rmtree(path)
        return 0
    else:
        return 1



@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        requestid = secure_filename(str(session))
        requestpath = "/tmp/" + requestid
        os.mkdir(requestpath) 
        f = requests.files['the_file']
        fpath = requestidpath + "/" + secure_filename(f.filename)
        f.save(fpath)
        
