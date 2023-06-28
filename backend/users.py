# Framework
from fastapi import APIRouter
# Models
from models.user_model import User
# Database functions
from db.database import fetch_table_data, insert_registry

# Router to Main
router = APIRouter()
# Get users from database
@router.get('/users')
async def get_users():
    data_to_serialize = fetch_table_data('Users')
    user_list = list()
    for i in data_to_serialize:
        data = {
            "id": i[0],
            "firstName": i[1],
            "lastName": i[2],
            "age": i[3],
            "email": i[4],
            "country": i[5]
        }
        user_list.append(data)
    return user_list
# Create user
@router.post('/users')
async def create_user(user_model: User):
    user_dict = user_model.dict()
    status = insert_registry('Users', user_dict)
    if status != 200:
        return {
            'message': 'Error ocurred while creating a new user',
            'content': user_dict
        }
    return {
        'message': 'User created succesfully',
        'newUser': user_dict
    }