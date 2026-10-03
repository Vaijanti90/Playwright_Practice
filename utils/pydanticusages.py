
# pip install pydantic 
from pydantic import BaseModel,ValidationError

class User(BaseModel):
    username : str
    password : str