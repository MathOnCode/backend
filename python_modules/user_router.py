from fastapi import APIRouter
from fastapi import HTTPException #é uma exceção de python normal com dados adicionais relevantes para APIs
from python_modules.user_responses import user_data_response
from python_modules.user_data_verification import user_data_verification
from python_modules.user_database import User
from python_modules.user_schemas import UserDataModel

router = APIRouter() #cria uma instância na memória para o APIRouter

@router.post("/")
async def root(payload: UserDataModel):
    is_valid, message = user_data_verification(payload)

    if not is_valid: # if está errado, perguntar se não é válido
        raise HTTPException(status_code=400, detail=message)# retorna uma exceção ("As exceções são eventos especiais – geralmente erros – que ocorrem em tempo de execução. Quando um erro desses ocorre, o Python cria um objeto do tipo Exception"), com o "raise" você pode definir qual tipo de erro você vai indicar e um texto para mostrar ao usuário
    else:
        User.create(payload)
    return user_data_response(payload, message)