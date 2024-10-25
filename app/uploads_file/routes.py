from flask import Blueprint, request, jsonify
from flask import current_app
import os

uploads_bp = Blueprint('uploads', __name__)

@uploads_bp.route('/uploads', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('files') 
    
    if not files:
        return jsonify({'error': 'No selected files'}), 400

    uploaded_files = []
    for file in files:
        if file.filename == '':
            return jsonify({'error': 'One or more files have no filename'}), 400
        
        # Lưu file
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        uploaded_files.append(file.filename)

    return jsonify({'message': 'Files uploaded successfully!', 'files': uploaded_files}), 200