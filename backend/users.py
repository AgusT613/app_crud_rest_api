# Framework
from fastapi import APIRouter
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
# Create user
@router.post('/users')
async def create_user(user_model: User):
    user_dict = user_model.dict()
    return {
        'message': f'{users.insert_registry(user_dict)}',
        'content': user_dict
    }