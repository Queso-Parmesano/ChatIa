import mysql.connector
from os import system

system('cls')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chatia"
)

sql = db.cursor()


def mostrarChatsExistentes():
    sql.execute('SELECT DISTINCT idChat, name FROM chats INNER JOIN usuarios ON idUser = 3')
    datos = sql.fetchall()

    print("Estos son tus chats:")
    for i in range(len(datos)):
        y = list(datos[i])
        y.append(i+1)
        datos[i] = tuple(y)
        print("Chat:",datos[i][2],"| Nombre:",datos[i][1])

    print("Seleccione su chat (Si escribe el nombre, escribalo identicamente porfavor):")
    opcion = input('>')

    for valor in datos:
        if(valor[2] == int(opcion)):
            print('Chat existente')









