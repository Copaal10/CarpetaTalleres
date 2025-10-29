#Condiciones (si-entonces)
#a)Mayor de edad: Pide la edad del usuario y dice si es mayor o menor de 18 años.
#b)Número positivo/negativo/cero: Pide un número y clasificarlo.
#c)Aprobado o reprobado: Pide una nota (0-10) y muestra "Aprobado" si es >=6.
#d)Día de la semana: Pide un número del 1 al 7 y muestra el día correspondiente.
#a
edad = int(input("Hola ¿ como estas ?, escribe aca tu edad :"))
if edad >= 18:
    print("Eres mayor de edad y tienes 18 años o mas ")
else: print("Tienes menos de 18 años, eres menor de edad")
#B
numero = float(input("Ingrese aca un numero no entero (Positivo/Negativo)"))
if numero == 0:
    print("El numero es cero")
elif numero > 0: 
    print("el numero es positivo")
else:
    print("el numero es negativo")

# explicacion basica b
# solicita el numero
# evalua si es cero
# evalua si es mayor a 0 es decir positivo
# si no cumple la primera y la segunda es negativo, No es necesario que evalue el 0
# con las validaciones anteriores despejo esas opciones, asi que es una opcion logica
# C
numero2 =float(input("Ingrese su calificacion de 0 a 10"))
if numero2 >=6:
    print("aprobado")
else:("Reprobado")
# explicacion c
# se deberia colocar un validador para que las notas ingresadas sean correctas en el rango?
# es decir entre 0 y 10 

numero3 = int(input("Ingrese un numero de 1 a 7"))
if numero3 == 1:
    print("el dia 1 es lunes")
elif numero3 ==2:
    print("el dia 2 es martes")
elif numero3 ==3:
    print(" el numero 3 es miercoles")
elif numero3 == 4:
    print("el numero 4 es jueves")
elif numero3 == 5:
    print("el numero 5 es Viernes")
elif numero3 == 6:
    print("el numero 6 es Sabado")
elif numero3 == 7:
    print("el numero es domingo")

#se puede cerrar un if son un Elif sin necesidad del Else, se podria usar el else para validar condiciones

