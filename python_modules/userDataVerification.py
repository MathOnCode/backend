import re # módulo de python para trabalhar com expressões regulares (regex)

def userData_Verification(payload):

    errors = []
    #form_exception = HTTPException(status_code=400, detail=errors) // quando precisar chamar a mesma exceção mais de uma vez, atribui-la a uma variável (não é o caso)

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
        return True, errors 
    else:
        return False, "Sucesso ao executar a ação!"

#transformar em objeto e armazenar em uma propriedade
#como retornar duas coisas em uma mesma função (primeiro status, depois mensagem)
#primeiro verificação, depois inserção no banco de dados