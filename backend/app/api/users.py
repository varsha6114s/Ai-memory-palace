from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
from ..models import db, User, MemoryPalace

users_bp = Blueprint('users', __name__)

class UpdateProfileSchema(Schema):
    username = fields.Str(validate=lambda x: len(x) >= 3)
    email = fields.Email()

@users_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get current user's profile."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Include memory palaces count
    profile = user.to_dict()
    profile['memory_palaces_count'] = len(user.memory_palaces)
    
    return jsonify({'user': profile}), 200

@users_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update current user's profile."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    schema = UpdateProfileSchema()
    
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    
    # Check for conflicts
    if 'email' in data and data['email'] != user.email:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already in use'}), 409
    
    if 'username' in data and data['username'] != user.username:
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Username already taken'}), 409
    
    # Update user
    for key, value in data.items():
        setattr(user, key, value)
    
    try:
        db.session.commit()
        return jsonify({
            'message': 'Profile updated successfully',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Update failed'}), 500

@users_bp.route('/memory-palaces', methods=['GET'])
@jwt_required()
def get_memory_palaces():
    """Get current user's memory palaces."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    palaces = [palace.to_dict() for palace in user.memory_palaces]
    
    return jsonify({'memory_palaces': palaces}), 200

@users_bp.route('/memory-palaces', methods=['POST'])
@jwt_required()
def create_memory_palace():
    """Create a new memory palace."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    palace = MemoryPalace(
        title=data['title'],
        description=data.get('description', ''),
        user_id=user_id
    )
    
    try:
        db.session.add(palace)
        db.session.commit()
        
        return jsonify({
            'message': 'Memory palace created successfully',
            'palace': palace.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Creation failed'}), 500