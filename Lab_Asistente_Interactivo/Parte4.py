import random

perfil = {
    "Nombre": "Alberto",
    "Edad": 30,
    "Color favorito": "azul"
}

respuestas_saludo = ["Hello", "Buenas", "Qué más"]

while True:
    mensaje = input("para iniciar conversacion escribe algo aca : ")

    if mensaje.lower() in ["hola", "buenas", "hello", "qué más"]:
        print(random.choice(respuestas_saludo))
    elif "nombre" in mensaje:
        print("Tu nombre es:", perfil["Nombre"])
    elif "edad" in mensaje:
        print("Tu edad es:", perfil["Edad"])
    elif "color favorito" in mensaje:
        print("Tu color favorito es:", perfil["Color favorito"])
    elif mensaje.lower() == "salir":
        print("¡Hasta pronto!")
        break
    else:
        print("No tengo información sobre eso aún.")
