from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()

class Item(BaseModel):
    name: str
    email: str
    phone: str
    
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"]
)

@app.post("/")
async def root(payload: Item):
    
    regexName = r'^[A-Za-z]+(?:\s+[A-Za-z]+)*\s+[A-Za-z]+$'
    regexEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    regexPhone = r'^\(\d{2}\)\s\d{4,5}\-\d{4}$'
    
    errors = []
    
    if not re.match(regexName, payload.name):
        errors.append("nome inválido!")
    if not re.match(regexEmail, payload.email):
        errors.append("email inválido!")
    if not re.match(regexPhone, payload.phone):
        errors.append("telefone inválido!")
        
    if len(errors) == 0:    
        return {"userData": payload,
                "message":"Requisição enviada com sucesso!"}
    
    raise HTTPException(status_code=400, detail=errors)