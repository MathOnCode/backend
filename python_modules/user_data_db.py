import mysql.connector

async def user_data_insertion(payload):
    conection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Senh@123',
        database = 'project_db'
    )

    cursor = conection.cursor()

    command = f'INSERT INTO user_data (name, email, phone) VALUES ("{payload.name}", "{payload.email}", "{payload.phone}")'
    cursor.execute(command)
    conection.commit() # para edição do banco de dados

    cursor.close()
    conection.close()