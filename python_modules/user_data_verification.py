import re # módulo de python para trabalhar com expressões regulares (regex)

def user_data_verification(payload):

    errors = []

    regex_name = r'^[A-zÁ-õç]+(?:\s+[A-zÁ-õç]+)*\s+[A-zÁ-õç]+$';
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    regex_phone = r'^\(\d{2}\)\s\d{4,5}\-\d{4}$';

    if not re.match(regex_name, payload.name):
        errors.append("nome inválido!")
    if not re.match(regex_email, payload.email):
         errors.append("email inválido!")
    if not re.match(regex_phone, payload.phone):
        errors.append("telefone. inválido!")

    return len(errors) == 0, errors