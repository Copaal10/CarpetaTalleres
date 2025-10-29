import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
data = json.loads(response.content)
print(response)

def mostrar_lista_pokemon():
    print("informacion pokemon")
    print(f"Nombre: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print("caracteristicas")
    for caracteristica in data['stats']:
        nombre = caracteristica['stat']['name'].capitalize()
        valor = caracteristica['base_stat']
        print(f" {nombre} : {valor}")

def mostrar_10_pokemon():
    url_lista = "https://pokeapi.co/api/v2/pokemon?limit=10"
    respuesta = requests.get(url_lista)
    if respuesta.status_code == 200:
        datos = json.loads(respuesta.content)
        lista = datos['results']
        print("Primeros 10 Pokémon:")
        for pokemon in lista:
            detalle = requests.get(pokemon['url']).json()
            nombre = detalle['name'].capitalize()
            id_pokemon = detalle['id']
            print(f"ID: {id_pokemon} - Nombre: {nombre}")
    else:
        print("Error al obtener la lista")

def consultar_dos_pokemon():
    pokemon1 = input("Escriba el nombre o ID del primer Pokémon: ")
    pokemon2 = input("Escriba el nombre o ID del segundo Pokémon: ")

    jugador1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon1.lower()}")
    jugador2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon2.lower()}")

    if jugador1.status_code == 200 and jugador2.status_code == 200:
        data1 = json.loads(jugador1.content)
        data2 = json.loads(jugador2.content)

        print(f"\nPrimer Pokémon: {data1['name'].capitalize()}")
        print(f"ID: {data1['id']}")
        print("Estadísticas:")
        total1 = 0
        for stat in data1['stats']:
            nombre = stat['stat']['name'].capitalize()
            valor = stat['base_stat']
            total1 += valor
            print(f" {nombre} : {valor}")

        print(f"\nSegundo Pokémon: {data2['name'].capitalize()}")
        print(f"ID: {data2['id']}")
        print("Estadísticas:")
        total2 = 0
        for stat in data2['stats']:
            nombre = stat['stat']['name'].capitalize()
            valor = stat['base_stat']
            total2 += valor
            print(f" {nombre} : {valor}")

        print("\nResultado del duelo:")
        print(f"Total de estadísticas de {data1['name'].capitalize()}: {total1}")
        print(f"Total de estadísticas de {data2['name'].capitalize()}: {total2}")

        if total1 > total2:
            print(f"\nGana {data1['name'].capitalize()} con {total1} puntos.")
        elif total2 > total1:
            print(f"\nGana {data2['name'].capitalize()} con {total2} puntos.")
        else:
            print("\nEmpate técnico. Ambos tienen la misma suma total de estadísticas.") 
    else:
        print("Uno de los Pokémon no fue encontrado.")
        



if response.status_code == 200:
    print("Conexion exitosa")
else:
    print("Error en la conexion")

while True:
    print("Hola entrenador como estas, que quieres hacer : ")
    print("1. Ver información de Pikachu")
    print("2. Ver los primeros 10 Pokémon")
    print("3. Salir")
    print("4. Comparar 2 Pokémon y ver quién gana")

    opcion = input(" escriba aca la opcion 1 , 2 , 3 o 4: ")

    if opcion == "1":
        mostrar_lista_pokemon()
    elif opcion == "2":
        mostrar_10_pokemon()
    elif opcion == "4":
        consultar_dos_pokemon()
    elif opcion == "3":
        print("Adios entrenador")
        break
    else:
        print("Opción no válida")