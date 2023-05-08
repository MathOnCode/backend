import re # módulo de python para trabalhar com expressões regulares (regex)
from python_modules.regexs import regex_name, regex_email, regex_phone

def user_data_verification(payload):

    errors = []

    if not re.match(regex_name, payload.name): #tranformar em função
        errors.append("nome inválido!")
    if not re.match(regex_email, payload.email):
         errors.append("email inválido!")
    if not re.match(regex_phone, payload.phone):
        errors.append("telefone. inválido!")

    return len(errors) == 0, errors