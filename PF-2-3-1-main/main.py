
# Detectar multiplos de ambos 3 y 5
# en el if se usan conectores para evaluar varias condiciones
# se una "and" y se deeben cumplir ambas condiciones
# se una "or" y basta con que una condicion sea verdaderas
# se una "not" y niega una condicion - buscar mas ejemplos de este - 

#    definir variable
#    Establecer contador inicio  while
#    agregar condicionales if inicio
#    agregar condicional  3 y 5
#    agregar condicional 3
#    agrgar condicional  5
#    agregar cierre del if
#    establecer incremento para el cierre del ciclo



numero = 1
while numero <= 1000:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

    numero = numero + 1