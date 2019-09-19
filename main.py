import os
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from databasequery import OperationDatabase
from flask import jsonify

ALLOWED_EXTENSIONS = set(['mp4', 'm4a', 'mkv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/report')
		else:
			flash('Allowed file types are mp4, m4a, mkv')
			return redirect(request.url)


@app.route('/report')
def report():
	return render_template('report.html')


@app.route('/getdata',methods = ["GET"])
def data():
    DatabaseObject = OperationDatabase()
    resp = DatabaseObject.selectquery()
    return jsonify(resp)


if __name__ == "__main__":
    app.run()