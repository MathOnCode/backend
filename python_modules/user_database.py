from python_modules.conn import connection

class User():
    def create(payload):
        cursor = connection.cursor() # A classe MySQLCursor instancia objetos que podem executar operações como instruções SQL. Os objetos Cursor interagem com o servidor MySQL usando um objeto MySQLConnection.

        command = f'INSERT INTO user_data (name, email, phone) VALUES ("{payload.name}", "{payload.email}", "{payload.phone}")'
        cursor.execute(command)
        connection.commit() # Este método envia uma instrução COMMIT para o servidor MySQL, confirmando a transação atual. Como por padrão o Connector/Python não faz confirmação automática, é importante chamar esse método após cada transação que modifica dados para tabelas que usam mecanismos de armazenamento transacional.

        cursor.close()
        connection.close()