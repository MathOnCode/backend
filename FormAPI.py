from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from python_modules.formResponse import Response

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
    Response(payload)