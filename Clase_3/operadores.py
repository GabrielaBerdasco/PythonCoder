# OPERADORES RELACIONALES

expresiones = [
    False == True,
    10 >= 2*4,
    33/3 == 11,
    True > False,
    True*5 == 2.5*2
]

result = [False, True, True, True, True]

print(expresiones)

print(result)

# OPERADORES LÓGICOS

expresiones_logicas = [not False, not 3 == 5, 33/3 == 11 and 5 < 2, True or False, True*5 == 2.5*2 or 123 >= 23, 12>7 and True < False]

result_logico = [True, True, False, True, True, False]

print(expresiones_logicas)

print(result_logico)

# EXPRESIONES ANIDADAS

nombre = input('Nombre: ')
edad = int(input('Edad: '))

validacion_1 = nombre != "****" 
validacion_2 = 10 < edad < 18 
validacion_3 = len(nombre) >= 3 and len(nombre) < 10 
validacion_4 = edad * 4 > 40

print(validacion_1, validacion_2, validacion_3, validacion_4)

result_validacion = validacion_1 and validacion_2 and validacion_3 and validacion_4

print(result_validacion)

