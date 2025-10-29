#Integradores
#a)Factorial de un número: Calcula el factorial de un número ingresado.
#b)Tabla de multiplicar: Pide un número y muestra su tabla de multiplicar del 1 al 10.
#c)Promedio de notas: Pide 3 notas y calcula el promedio. Luego, dice si está aprobado (>=60) o no.
d)Contador de pares/impares: Pide 5 números y cuenta cuántos son pares e impares.
e)Simulador de cajero básico:
I.Saldo inicial: $1000.
II.Pide al usuario si quiere "retirar" o "depositar".
III.Actualiza el saldo y muéstrelo



numero_fact = int(input("Escriba un numero para determinar su factorial : "))

factorial = 1
contador = 1

while contador <= numero_fact:
    factorial *= contador
    contador +=1

print("el factorial de" , numero_fact , "es" , factorial)


#practica mas este
tabla_multiplicar = int(input("Escribe un numero : "))

incremento = 1
while incremento <=10:
    print(tabla_multiplicar , " x " , incremento , "=" , incremento * tabla_multiplicar)
    incremento += 1

#practica mas este

#c)Promedio de notas: Pide 3 notas y calcula el promedio. Luego, dice si está aprobado (>=60) o no.

numero1 = int(input("ingrese la nota 1"))
numero2 = int(input("ingrese la nota 2"))
numero3 = int(input("ingrese la nota 3"))
promedio = (numero1 + numero2 + numero3) / 3
if promedio >= 60:
    print("aprobado")
else:
    print("reprobado")

print("el promedio es :" , promedio)

d)Contador de pares/impares: Pide 5 números y cuenta cuántos son pares e impares.

suma_pares = 0
suma_impares = 0


numero1 = int(input("ingrese el numero 1"))
numero2 = int(input("ingrese el numero 2"))
numero3 = int(input("ingrese el numero 3"))
numero4 = int(input("ingrese el numero 4"))
numero5 = int(input("ingrese el numero 5"))

if numero1 % 2 == 0:
    print("el ", numero1, "Es par")
    suma_pares += numero1
else:
    print("el", numero1, "Es impar")
    suma_impares += numero1

if numero2 % 2 == 0:
    print("el ", numero2, "Es par")
    suma_pares += numero2
else:
    print("el", numero2, "Es impar")
    suma_impares += numero2

print("el numero" , numero2 , "es" , numero2)

if numero3 % 2 == 0:
    print("el ", numero3, "Es par")
    suma_pares += numero3
else:
    print("el", numero3, "Es impar")
    suma_impares += numero3

print("el numero" , numero3 , "es" , numero3)

if numero4 % 2 == 0:
    print("el ", numero4, "Es par")
    suma_pares += numero4
else:
    print("el", numero4, "Es impar")
    suma_impares += numero4

print("el numero" , numero4 , "es" , numero4)

if numero5 % 2 == 0:
    print("el ", numero5, "Es par")
    suma_pares += numero5
else:
    print("el", numero5, "Es impar")
    suma_impares += numero5

print("el numero" , numero5 , "es" , numero5)



print("la suma de numeros pares es : ", suma_pares)
print("la suma de numeros impares es : ", suma_impares)

# investiga mas si hay formas mejores y eficientes de mejorar esto

saldo = 1000

operacion = input(" Si quiere retirar escriba - y si quiere depositar + ?:")
monto = float(input("ingrese el monto :"))

if operacion == "-":
    saldo -= monto
else:
    saldo += monto

print ("el saldo actual es de " , saldo)

#profe si estas leyendo esto gracias