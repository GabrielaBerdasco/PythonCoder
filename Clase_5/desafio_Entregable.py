#1

option = 1
number_1 = int(input('Ingresar primer número: '))
number_2 = int(input('Ingresar segundo número: '))

while option != 4 :
    option = int(input('Qué opción desea elegir : \n(1. Suma, 2. Resta, 3. Multiplicación, 4. Salir\n'))

    if option == 1 :
        print(number_1 + number_2)

    elif option == 2 :
        print(number_1 - number_2)
    
    elif option == 3 :
        print(number_1 * number_2)
    
    elif option == 4 :
        print('Ha seleccionado la opción de salir')
        break
    else :
        print('La opción no es correcta')
    

#2
odd_number = 2

while odd_number%2 == 0 :
    print('El número no es impar! ')
    odd_number = int(input('Ingrese un número impar: '))


#3
counter = 0

for number in range(1, 101, 2) :
    counter += number

print(f'La suma de los números impares entre 0 y 100 es : {counter}')

#4

user_amount = int(input('¿Cuántos números desea ingresar?: '))
count_1 = 0
average = user_amount

while user_amount != 0 :
    new_number = int(input('Ingresar número: '))
    count_1 += new_number
    user_amount -= 1
else :
    count_1 /= average
    print(f'La media es: {count_1}')


#5

numeros = [1, 3, 6, 9]
number_0 = int(input('Ingresar un número entre 0 y 9: '))


while number_0 >= 10 :
    print('El número ingresado está fuera de rango')
    number_0 = int(input('Ingresar un número entre 0 y 9: '))
else :
    counter_2 = numeros.count(number_0)
    if counter_2 > 0 :
        print('El número ingresado se encuentra en la lista')
       
    else :
        print('El número no está en la lista!')


#6

list_1= list(range(0, 11))
list_2 = list(range(-10, 1))
list_3 = list(range(0, 22, 2))
list_4 = list(range(-19, 1, 2))
list_5 = list(range(5, 51, 5))

print(list_5)

#7

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_12 = lista_1 + lista_2
lista_3 = []
     

for valor in lista_12 :
    count_exist = lista_12.count(valor)
    if count_exist > 1 :
        count_exist_2 = lista_3.count(valor)
        if count_exist_2 < 1 :
            lista_3.append(valor)    
        
print(lista_3)