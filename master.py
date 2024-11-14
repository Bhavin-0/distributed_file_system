from flask import Flask, request, send_from_directory, jsonify, redirect, render_template
import os

app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    # Display the upload page
    return render_template('upload.html')

@app.route('/file-list')
def file_list():
    # List files available in the upload directory
    try:
        files = os.listdir(UPLOAD_FOLDER)
        return render_template('download.html', files=files)
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve file list', 'details': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully!'})
    except Exception as e:
        return jsonify({'error': 'Failed to upload file', 'details': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Serve the requested file for download
    try:
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to download file', 'details': str(e)}), 500

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    # Delete the requested file
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify({'message': 'File deleted successfully'})
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to delete file', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
