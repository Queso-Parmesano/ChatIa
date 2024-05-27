import google.generativeai as genai
from hashlib import sha256
from time import sleep
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

genai.configure(api_key='<API-KEY>')

model = genai.GenerativeModel('gemini-pro')

#Completa
def loading():
    print('Cargand, espere por favor.')
    sleep(0.5)
    system('cls')
    print('Cargand, espere por favor..')
    sleep(0.5)
    system('cls')
    print('Cargand, espere por favor...')
    sleep(0.5)
    system('cls')
    print('Cargand, espere por favor.')
    sleep(0.5)
    system('cls')
    print('Cargand, espere por favor..')
    sleep(0.5)
    system('cls')
    print('Cargand, espere por favor...')
    sleep(0.5)
    system('cls')

#Completa
def insertDB(request):
    sql.execute(request)
    db.commit

#Completa
def mensaje():
    msjUser = input('Send "Exit" to leave > ')
    if (msjUser.lower() != 'exit'):
        return msjUser
    else:
        return False        

#Completa
def sendMsj():
    msjUser = mensaje()
    if (isinstance(msjUser, str)):
        response = model.generate_content(msjUser)
        print ("IA: " + response.text)
        sendMsj()

#Completa
def seleccionDeChat():
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
    try:
        return int(opcion)
    except:
        return opcion


#Completa
def login():
    print("Inicio de sesion.")
    print('Ingrese sus credenciales')
    intentos = 0
    datos = [None, None]
    while(datos[0] == None or datos[1] == None and intentos < 3):
        try:
            username = input("Username > ")
            sql.execute(f'SELECT id FROM usuarios WHERE username = "{username}"')
            datos[0] = sql.fetchone()[0]
            password = input("Password > ")
            sql.execute(f'SELECT passw FROM usuarios WHERE id = 1')
            datos[1] = sql.fetchone()[0]
            if (datos[1] == sha256(password.encode('utf-8')).hexdigest()):
                pass
            else:
                datos[1] = None
                print('Try Again')
            intentos += 1
        except:
            print('Try Again')

#Completa
def register():
    confirmacion = 'no'
    print("Note: The username will be saved exactly as you type it.")
    while(confirmacion == 'no' or confirmacion == 0):
        username = input("Username > ")
        password = input("Password > ")
        confirmacion = input('Seguro que quiere que su nombre de usuario sea "'+username+'" y su contrasenia sea "'+password+'"? \n')
        system('cls')
    passwh = sha256(password.encode('utf-8')).hexdigest()
    insertDB(f'INSERT INTO usuarios (username, passw) values ("{username}","{passwh}")')
    loading()
    login()
