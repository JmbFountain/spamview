from flask import Flask, render_template, make_response, request, session
import uuid
from werkzeug.utils import secure_filename
# import mimetypes
import fsops
import mail_analyzer


app = Flask(__name__)
# app.secret_key = os.urandom(16)


@app.route('/')
def main():
    resp = make_response(render_template("main.html"))
    session_id = str(uuid.uuid4())
    resp.set_cookie(key='session', value=session_id, samesite="strict")
    return resp


@app.post("/uploademl")
def upload_file():
    requestid = secure_filename(request.cookies['session'])
    requestpath = "tmp/" + requestid
    fsops.mkdir(requestpath)
    f = request.files['file']
    fpath = requestpath + "/mail.eml"
    f.save(fpath)
    mail_analyzer.analyze(fpath)
    return render_template("analyzing.html")


