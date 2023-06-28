from pydantic import BaseModel

class User(BaseModel):
    firstName: str
    lastName: str
    age: int
    email: str
    country: str