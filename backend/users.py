# Framework
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
# Models
from models.user_model import User
# Database functions
from db.tables import Table

# Users Table
users = Table('Users')
# Router to Main
router = APIRouter()
# Get users from database
@router.get('/users')
async def get_users():
    return users.select_everything_from()
# Get user by id and first_name
@router.get('/user')
async def get_user(id: int, first_name: str):
    for user in users.select_everything_from():
        if user['id'] == id and user['firstName'] == first_name:
            user = users.select_from_where(id, first_name)[0]
            return user
    return {'message': f'No user named {first_name}'}
# Create user
@router.post('/user')
async def create_user(user_model: User):
    user_dict = user_model.dict()
    return {
        'message': f'{users.insert_registry(user_dict)}',
        'content': user_dict
    }
# Update user by id or first_name
@router.put('/user')
async def update_user(id: int, first_name: str, user_model: User):
    user_dict = user_model.dict()
    return users.update(id, first_name, user_dict)

@router.delete('/user')
async def delete_user(id: int, first_name: str):
    return users.delete_from_where(id, first_name)