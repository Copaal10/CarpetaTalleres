
operacion_suma = "suma"
operacion_resta = "resta"
operacion_multpluicacion = "multiplicacion"
operacion_division = "division"

while True:
    print("1 . suma")
    print("2 . resta")
    print("3 . Multiplicacion")
    print("4 . Division")
    print("5 . salir del sistema")
    tipo_operacion = (input("Ingrese el tipo de operacion que requiere"))

    if tipo_operacion == "1":
        print("ha seleccionado Suma")
    elif tipo_operacion == "2":
        print("ha seleccionado resta")
    elif tipo_operacion == "3":
        print("ha seleccionado multiplicacion")
    elif tipo_operacion == "4":
        print("ha seleccionado division")
    elif tipo_operacion == "5":
        print("salir del sistema")
        break
    else:
        print("Opción inválida. Intente con 1, 2, 3, 4 o 5.")




