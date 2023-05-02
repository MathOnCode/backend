from pydantic import BaseModel

class UserDataModel(BaseModel):
    name: str
    email: str
    phone: str

#class UserLoginModel(BaseModel):
#    login: str
#    password: str