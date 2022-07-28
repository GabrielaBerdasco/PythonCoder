print('Desafio entregable \n')
#1) Realiza una función llamada area_rectangulo() que devuelva el 
# área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura

print('\nÁREA DEL RECTÁNGULO')
print('========================')

def area_rectangulo() :
    base = 15
    altura = 10

    area = base * altura

    return area

resultado = area_rectangulo()
print(resultado)

#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a 
# partir de un radio. Calcula el área de un círculo de 5 de radio

#🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el 
# resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del 
# módulo math.

print('\nÁREA DEL CÍRCULO')
print('========================')

import math

def area_circulo() :

    radio = 5

    area = (radio ** 2) * math.pi

    return area

resultado_2 = area_circulo()
print(resultado_2)


#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.

#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

print('\nRELACIÓN ENTRE DOS NÚMEROS')
print('==============================')

def relacion(a, b) :
    
    if a > b :
        return 1

    elif a < b :
        return -1

    elif a == b :
        return 0

while True :

    try :
        num_1 = float(input('Ingresar primer número: '))
        num_2 = float(input('Ingresar segundo número: '))

        resultado_3 = relacion(num_1, num_2)

    except ValueError :
        print('Número inválido')

    else :
        print(resultado_3)

    exit = input('Desea salir: (s)')
    
    if exit == 's' :
        break


#4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su 
# punto intermedio:
#Ayuda: El número intermedio de dos números corresponde a la suma de los dos 
# números dividida entre 2

#Comprueba el punto intermedio entre -12 y 24

print('\nMEDIA DE DOS NÚMEROS')
print('========================')

def intermedio(a, b) :

    medio = (a + b) / 2

    return medio

while True :

    try :
        num_1 = float(input('Ingresar primer número: '))
        num_2 = float(input('Ingresar segundo número: '))

        resultado_3 = intermedio(num_1, num_2)

    except ValueError :
        print('Número inválido')

    else :
        print(resultado_3)

    exit = input('Desea salir: (s)')
    
    if exit == 's' :
        break

#5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el 
# número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
# La función tendrá que cumplir lo siguiente:

#Devolver el límite inferior si el número es menor que éste
#Devolver el límite superior si el número es mayor que éste.
#Devolver el número sin cambios si no se supera ningún límite.
#Comprueba el resultado de recortar 15 entre los límites 0 y 10

print('\nRECORTAR NÚMEROS')
print('========================')

def recortar(a, b, c) :
    if a < b :
        return b
    elif a > c:
        return c
    else :
        return a


while True:

    try :

        num_recortar = float(input('Ingresar número a recortar: '))
        lim_inferior = float(input('Ingresar límite inferior: '))
        lim_superior = float(input('Ingresar límite superior: '))

        resultado_3 = recortar(num_recortar, lim_inferior, lim_superior)

    except ValueError :
        print('Número inválido')

    else :
        print(resultado_3)
        break

#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos 
# listas ordenadas. La primera con los números pares, y la segunda con los números 
# impares:
# Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

print('\nRECORTAR NÚMEROS')
print('========================')

lista_1 = [3, 4, 8, 2, 9]

def separar(lista) :

    lista_par = []
    lista_impar = []
    lista.sort()
        
    for n in lista :
            
        if n%2 == 0 :
            lista_par.append(n)
        else :
            lista_impar.append(n)
    
    print(f'La lista de números pares es: {lista_par}')
    print(f'La lista de números impares es: {lista_impar}')

separar(lista_1)