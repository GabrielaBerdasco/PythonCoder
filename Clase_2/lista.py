#Desafío listas [] mutables

lista_1 = [1, 12, 123]

lista_2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista_1.append(1234)
lista_1.append('Hola')

print('#1', lista_1)

lista_2 += ["Adios"]
lista_2 += [1234]

print('#2', lista_2)

lista_3 = lista_1.copy()
lista_3.pop()
# O lista_3 = lista_1[:-1] porque .pop() directo a la lista 1 la modificaría

print('#3', lista_3)
print(lista_1)

lista_4 = lista_2.copy()
lista_4.pop()
lista_4.pop(0)
# O lista_4 = lista_1[1:-1]

print('#4', lista_4)

lista_5 = lista_4 + lista_3

print('#5', lista_5)

