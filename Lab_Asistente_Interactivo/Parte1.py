#definir usuario y clace
user = "Copaal10"
password = "2205"
intentos = 0
#Solicitua usuario y password
#

while intentos < 3:
    user_ingreso = input("Ingrese su usuario")
    password_ingreso = input("ingrese su contraseña")
    if user_ingreso == user and password_ingreso == password:
        print("Acceso concedido")
        break
    else:
        print("Acceso denegado")
        intentos += 1

if intentos == 3:
    print("Sistema bloqueado por intentos fallidos")