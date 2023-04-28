from pydantic import BaseModel

class Item(BaseModel):
    name: str
    email: str
    phone: str