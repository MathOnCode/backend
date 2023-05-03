from pydantic import BaseModel

class UserDataModel(BaseModel):
    name: str
    email: str
    phone: str