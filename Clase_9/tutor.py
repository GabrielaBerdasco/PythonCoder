def validar_numero(entrada):
    """Valida si el parámetro recibido es un entero positivo o negativo.
    Puede recibir, por ej.: 2022, -2022"""
    validar_1 = entrada.isdecimal()       # si todos los caracteres son números
    validar_2 = entrada[0] in ("-")       # si el primer caracter es un -
    validar_3 = entrada[1:].isdecimal()   # si desde el segundo caracter en adelante son números
    if validar_1 or (validar_2 and validar_3):
        return True
    else:
        return False


def año_bisiesto(año):
    """Valida si el entero recibido es un año o bisiesto o no.
    Puede recibir positivos o negativos."""
    validar_1 = año % 4 == 0          # Es divisible por 4
    validar_2 = not (año % 100 == 0)  # No es divisible por 100
    validar_3 = año % 400 == 0        # Es divisible por 400
    if validar_1 and (validar_2 or validar_3):
        return True
    else:
        return False


def main():
    """Función principal"""
    while True:
        entrada = input("Ingrese un año (s: salir): ")
        if entrada == "s":
            break
        es_numero = validar_numero(entrada)
        if not es_numero:
            continue
        año = int(entrada)
        es_año_bisiesto = año_bisiesto(año)
        if es_año_bisiesto:
            print(f"El año {año} sí es bisiesto.")
        else:
            print(f"No es bisiesto.")


def testing_de_funciones():
    """Prueba las funciones con varios valores mediante la sentencia `assert`.
    El argumento de la función es el valor que se prueba, luego de `==` es el valor esperado."""
    assert validar_numero("2000") == True
    assert validar_numero("-2400") == True
    assert validar_numero("0") == True
    assert validar_numero("cadena") == False
    assert validar_numero("20aa") == False
    assert año_bisiesto(2020) == True
    assert año_bisiesto(2019) == False
    assert año_bisiesto(2000) == True
    assert año_bisiesto(1900) == False
    assert año_bisiesto(-2400) == True
    assert año_bisiesto(-2399) == False


testing_de_funciones()  # Si hay un error se detiene. Intentar cambiar ´or´ o ´and´ de ´año_bisiesto´
main()