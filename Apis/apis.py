
#
#API --> Interfaz de programacion de aplicaciones
# reglas , punto de partida, endpoints
# metodos http, crud
# GET ---> obtener
# ? SOAP ---> XML
# ? Rest ---> JSON

import requests
import json

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

data = json.loads(response.content)
print(data)


