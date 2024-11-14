from flask import Flask, request, send_from_directory, jsonify
import os
import sqlite3

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads_node1'  # Use 'uploads_node2' for Node 2
DATABASE = 'files.db'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO files (filename) VALUES (?)', (filename,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'File uploaded', 'filename': filename})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/files', methods=['GET'])
def list_files():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT filename FROM files')
    files = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify(files)

if __name__ == '__main__':
    app.run(port=5001)  # Change to port 5002 for Node 2
