from pydantic import BaseModel

class FormModel(BaseModel):
    name: str
    email: str
    phone: str