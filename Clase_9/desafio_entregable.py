'''
Consigna: Realizar una función llamada año_bisiesto:
Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número debe indicar que se ingrese un número.

Información a tener en cuenta al realizar el entregable:

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo 
son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 
2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

'''
def calcular_anio_bisiesto(seleccion) :
        
    if seleccion[0] == '-' :
        seleccion = seleccion[1:]
    
    if ( seleccion.isdecimal() and seleccion != 's' ) :


        seleccion = int(seleccion)

        if  seleccion%4 == 0 and seleccion%100 != 0 or seleccion%400 == 0 :
            return True
        else :
            return False

    elif seleccion == 's' :
        return 's'

    else :
        print('Por favor, ingrese un número válido')




while True :

    seleccion = input('Por favor indique año: (s para salir) ')

    calculo = calcular_anio_bisiesto(seleccion)

    if calculo == 's' :
        print('Hasta luego!')
        break
    
    elif calculo :
        print(f'El año {seleccion} es bisiesto')
    
    elif calculo == False :
        print(f'El año {seleccion} no es bisiesto')
