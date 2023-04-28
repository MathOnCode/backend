from fastapi import HTTPException
import re

def rootForm_Verification(payload):

    errors = []

    regexName = r'^[A-Za-z]+(?:\s+[A-Za-z]+)*\s+[A-Za-z]+$';
    regexEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    regexPhone = r'^\(\d{2}\)\s\d{4,5}\-\d{4}$';

    if not re.match(regexName, payload.name):
        errors.append("nome inválido!")
    if not re.match(regexEmail, payload.email):
         errors.append("email inválido!")
    if not re.match(regexPhone, payload.phone):
        errors.append("telefone. inválido!")

    if len(errors) > 0:
        raise HTTPException(status_code=400, detail=errors)
    return len(errors) == 0