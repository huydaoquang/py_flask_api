from flask import Blueprint, request, jsonify
from app.employee.models import (
    fetch_all_employees, add_employee, update_employee, delete_employee
)

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    records = fetch_all_employees()
    return jsonify(records)

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.json
    employee_id = add_employee(new_employee['name'], new_employee['salary'])
    return jsonify({"id": employee_id}), 201

@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee_route(id):
    updated_employee = request.json
    update_employee(id, updated_employee['name'], updated_employee['salary'])
    return jsonify({"id": id})

@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee_route(id):
    delete_employee(id)
    return jsonify({"id": id}), 200
