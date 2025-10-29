#3. Ciclos (mientras o repetir)
#a)Contador del 1 al 10: Imprime los números del 1 al 10 usando un ciclo.
#b)Suma hasta 'n': Pide un número n y suma todos los números desde 1 hasta n.
#c)Adivina el número: El usuario debe adivinar un número fijo (ej: 5). El programa dice "mayor" o "menor" hasta que acierte.


contador = 1
while contador <=10:
    print("contador", contador)
    contador += 1


n = int(input("ingrese un numero : "))
suma = 0
contador = 1

while contador <= n:
    suma += contador
    contador = contador + 1

print("la suma es :", suma)

#practicar mas este

import random
numero_secreto =random.randint(1,10)

adivinanza = int(input("ingrese un numero entre 1 y 10"))

while adivinanza != numero_secreto:
    if adivinanza > numero_secreto:
        print("el numero es mayor")
    else:
        print("el numero es menor")

    adivinanza =int(input("intenta de nuevo"))

print("Correcto adivinaste")

##practicar mas este