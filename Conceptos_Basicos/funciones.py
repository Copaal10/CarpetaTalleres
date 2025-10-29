
#!funciones ---< bloque de codigo destinado a resolver 
# al en espeficifo

# funcion sin parametro

def saludar ():
    print("hola a todos")

saludar ()

# funcion con parametros


def saludarConParametro(nombre):
    return f"hola , {nombre}"

saludo = saludarConParametro ("ana")
print(saludo)
saludo = saludarConParametro("nico")
print(saludo)