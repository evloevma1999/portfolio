from flask import Blueprint, jsonify, request
from models import get_all_users, get_user, update_user, delete_user

app_routes = Blueprint('app_routes', __name__)

# Route to get all users
@app_routes.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([dict(user) for user in users])

# Route to get a user by ID
@app_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(dict(user))
    return jsonify({'error': 'User not found'}), 404

# Route to update a user by ID
@app_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    update_user(user_id, name, email)
    return jsonify({'message': 'User updated successfully'})

# Route to delete a user by ID
@app_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'})
