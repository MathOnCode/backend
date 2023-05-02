from fastapi import APIRouter
from python_modules.formResponse import rootForm_Response
from python_modules.formVerification import rootForm_Verification
from python_modules.formSchemas import FormModel

router = APIRouter() #cria uma instância na memória para o APIRouter

@router.post("/")
async def root(payload: FormModel):
    if rootForm_Verification(payload): 
        return rootForm_Response(payload)
        
#@router.post("/test")
#async def root(payload: FormModel):
#    return {"userData": payload,
#            "message": "teste do router"}
