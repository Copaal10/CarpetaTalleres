
# Contador de 1 a 10000
numero = 1
while numero <=1000:
    print(numero)
    numero = numero + 1


# detectar multiplos de 3
if numero % 3 == 0:
    print("Fizz")


# detectar multilos de 5
if numero % 5 == 0:
    print("Buzz")

# Detectar multiplos de ambos 3 y 5
# en el if se usan conectores para evaluar varias condiciones
# se una "and" y se deeben cumplir ambas condiciones
# se una "or" y basta con que una condicion sea verdaderas
# se una "not" y niega una condicion - buscar mas ejemplos de este - 

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")