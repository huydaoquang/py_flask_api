from flask import Blueprint, request, jsonify
from app.log.models import insert_log

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/logs', methods=['POST'])
def log_message():
    data = request.get_json()  # Lấy dữ liệu JSON từ yêu cầu

    if not data or 'message' not in data:
        return jsonify({'error': 'Message is required'}), 400

    message = data['message']

    # Ghi log vào bảng
    insert_log(message)

    return jsonify({'status': 'success', 'message': 'Log recorded'}), 200