from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from query import search

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imageFile']
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        results = search(filepath)
        return render_template('result.html', results=results)
    return 'Upload failed'

if __name__ == '__main__':
    app.run(debug=True)