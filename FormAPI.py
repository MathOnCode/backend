from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from python_modules.formResponse import rootForm_Response
from python_modules.verificationBackend import rootForm_Verification
from python_modules.item_schemas import Item

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"]
)

@app.post("/")
async def root(payload: Item):
        if rootForm_Verification(payload):
            return rootForm_Response(payload)

