from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, static_folder='static')
SERVER_URL = 'http://localhost:5000'  # Master server URL

@app.route('/')
def index():
    response = requests.get(f'{SERVER_URL}/files')
    files = response.json()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        files = {'file': file.read()}
        response = requests.post(f'{SERVER_URL}/upload', files=files)
        if response.ok:
            return redirect(url_for('index'))
    return 'Failed to upload', 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    response = requests.get(f'{SERVER_URL}/file_location/{filename}')
    if response.ok:
        node_url = response.json()['node']
        return redirect(f'{node_url}/download/{filename}')
    return 'File not found', 404

if __name__ == '__main__':
    app.run(port=5001)
