from fastapi import APIRouter
from fastapi import HTTPException #é uma exceção de python normal com dados adicionais relevantes para APIs
from python_modules.userResponses import user_data_response
from python_modules.userDataVerification import user_data_verification
from python_modules.userSchemas import UserDataModel

router = APIRouter() #cria uma instância na memória para o APIRouter

@router.post("/")
async def root(payload: UserDataModel):

    isValid, message = user_data_verification(payload)

    if not isValid: # if está errado, perguntar se não é válido
        raise HTTPException(status_code=400, detail=message)# retorna uma exceção ("As exceções são eventos especiais – geralmente erros – que ocorrem em tempo de execução. Quando um erro desses ocorre, o Python cria um objeto do tipo Exception"), com o "raise" você pode definir qual tipo de erro você vai indicar e um texto para mostrar ao usuário
    
    return user_data_response(payload, message)