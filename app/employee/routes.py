from flask import Blueprint, request, jsonify
from typing import Any, List, Dict
from app.employee.models import (
    fetch_all_employees, add_employee, update_employee, delete_employee,fetch_employees
)
from app.utils import token_required

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['GET'])
@token_required
def get_employees():
    records = fetch_all_employees()
    return jsonify(records)

@employee_bp.route('/employees-limit', methods=['GET'])
@token_required
def get_employees_limit():
    # Lấy tham số truy vấn
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=5, type=int)
    search = request.args.get('search', default='', type=str)

    records, total_records = fetch_employees(page, limit, search)

    data: List[Dict[str, Any]] = []

    for item in records:
        data.append({
            'id': item[0],   
            'name': item[1],
            'salary': item[2]
        })

    response = {
        'page': page,
        'limit': limit,
        'total_records': total_records,
        'total_pages': (total_records + limit - 1) // limit,
        'employees': data
    }

    return jsonify(response)

@employee_bp.route('/employees', methods=['POST'])
@token_required
def create_employee():
    new_employee = request.json
    employee_id = add_employee(new_employee['name'], new_employee['salary'])
    return jsonify({"id": employee_id}), 201

@employee_bp.route('/employees/<int:id>', methods=['PUT'])
@token_required
def update_employee_route(id):
    updated_employee = request.json
    update_employee(id, updated_employee['name'], updated_employee['salary'])
    return jsonify({"id": id})

@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
@token_required
def delete_employee_route(id):
    delete_employee(id)
    return jsonify({"id": id}), 200

