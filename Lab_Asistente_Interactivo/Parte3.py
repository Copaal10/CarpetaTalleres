usuarios = {
    "Usuario1" : {
        "Nombre" : "ALberto",
        "Edad" : 30,
        "Color favorito" : "azul",
    },
    "Usuario2" : {
        "Nombre" : "Camila",
        "Edad" : 20,
        "Color favorito" : "rojo",
    },
    "Usuario3" : {
        "Nombre" : "andrea",
        "Edad" : 40,
        "Color favorito" : "rosa",
    },
    "Usuario4" : {
        "Nombre" : "ximena",
        "Edad" : 50,
        "Color favorito" : "purpura",
    },
}

def consultar_datos():
    print("usuarios disponibles")
    for usuario in usuarios:
        print(usuario)
        print("nombre" , usuarios[usuario]["Nombre"])
        print("edad", usuarios[usuario]["Edad"])
        print("color favorito" , usuarios[usuario]["Color favorito"])

def agregar_usuario():
    print("Agrege un nuevo usuario")
    nuevo_id = input(" agrege un nuevo usuario identificador ")
    nombre = input("nombre : ")
    edad = input("edad")
    color = input("Color favorito")

    usuarios[nuevo_id] = {
        "Nombre" : nombre,
        "Edad" : int(edad),
        "Color favorito" : color
    }

def eliminar_usuario():
    print("eliminar dato existente")
    usuario_id = input("ingrese el identificador Usuario2 y otro")
    dato = input("ingrese el nombre del dato a eliminar")

    del usuarios[usuario_id][dato]
    print("dato eliminado")
#debe ser mu especifico
while True:
    print("1. Consultar datos")
    print("2. Agregar Datos")
    print("3. Eliminar Datos")
    print("4. Salir del sistema")
    tipo_accion = input("¿que quieres realizar?")
    if tipo_accion == "1":
        print("ha seleccionado Consulta")
        consultar_datos()
    elif tipo_accion == "2":
        print("ha seleccionado Agregar")
        agregar_usuario()
    elif tipo_accion == "3":
        print("ha seleccionado Eliminar")
        eliminar_usuario()
    elif tipo_accion == "4":
        print("salir del sistema")
        break
    else:
        print("Opción inválida. Intente con 1, 2 o 3.")

