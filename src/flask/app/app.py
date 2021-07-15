from flask import Flask
from flask import render_template
from flask import request
from flask import session
import os
import shutil
from werkzeug.utils import secure_filename
import requests
import mimetypes
import fsops
import mail_analyzer

app = Flask(__name__)
app.secret_key = os.urandom(16)





@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        requestid = secure_filename(str(session))
        requestpath = "/tmp/" + requestid
        os.mkdir(requestpath) 
        f = requests.files['the_file']
        fpath = requestpath + "/" + secure_filename(f.filename)
        fsops.createFile(fpath)
        mail_analyzer.analyze(fpath)


