import re # módulo de python para trabalhar com expressões regulares (regex)

def user_data_verification(payload):

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

    return len(errors) == 0, errors