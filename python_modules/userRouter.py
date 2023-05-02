from fastapi import APIRouter
from fastapi import HTTPException #é uma exceção de python normal com dados adicionais relevantes para APIs
from python_modules.userResponses import userData_Response
from python_modules.userDataVerification import userData_Verification
from python_modules.userSchemas import UserDataModel

router = APIRouter() #cria uma instância na memória para o APIRouter

@router.post("/")
async def root(payload: UserDataModel):

    validation, message = userData_Verification(payload)

    if validation: 
        raise HTTPException(status_code=400, detail=message)# retorna uma exceção ("As exceções são eventos especiais – geralmente erros – que ocorrem em tempo de execução. Quando um erro desses ocorre, o Python cria um objeto do tipo Exception"), com o "raise" você pode definir qual tipo de erro você vai indicar e um texto para mostrar ao usuário
    else:
        return userData_Response(payload, message)
        
#@router.post("/test")
#async def root(payload: FormModel):
#    return {"userData": payload,
#            "message": "teste do router"}
