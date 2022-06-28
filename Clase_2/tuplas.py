#Tuplas  () inmutable

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

print('#1', tupla[-1])

print('#2', len(tupla))

print('#3', tupla.index(87))

lista = list(tupla)
print('#4', lista[-3:])

print('#5', tupla[8])

print('#6', tupla.count(7))
