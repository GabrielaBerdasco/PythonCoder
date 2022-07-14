lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

#1 Borrar los elementos duplicados

lista_1 = list(set(lista))

print(f"Ejercicio 1: {lista_1}")

#2 Ordenar la lista de mayor a menor

lista_2 = lista_1.copy()
lista_2.sort(reverse=True)

print(f"Ejercicio 2: {lista_2}")

#3 Eliminar todos los números impares 
# (  for ---- if (%2==1) ---- pop, remove     )

lista_3 = []

for x in lista_1 :
    if x%2 == 0 :
        lista_3.append(x)

print(f"Ejercicio 3: {lista_3}")

#4 Realizar una suma de todos los números que quedan

lista_4 = sum(lista_3)

print(f"Ejercicio 4: {lista_4}")

#5 Añadir como primer elemento de la lista la suma realizada insert(0, suma)
lista_5 = lista_3.copy()

lista_5.insert(0, lista_4)

#6 Devolver la lista modificada

print(f"Ejercicio 5: {lista_5}")

#7 Finalmente, después de ejecutar la función, comprueba que la suma de todos 
# los números a partir del segundo, concuerda con el primer número de la lista

lista_7 = sum(lista_5, -lista_4)


print(f"Ejercicio 7: {lista_7}")