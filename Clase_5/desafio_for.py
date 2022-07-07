#Desafío genérico EJERCICIOS VARIOS

print('\n#1 Países\n')

paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']

#for value in paises:
for indice, valor in enumerate(paises) :
    print(f'País de la lista países: {valor}')



print('\n#2 Sumar pares entre 0 y 100\n')

num = 0
contador = 0

while num <= 100 :
    if num%2 == 0 :
        contador += num
    num+=1
else :
    print(f'La sumatoria es: {contador}')

contador_2 = 0

for par in range(0, 101, 2) :
    contador_2 += par
print(f'La sumatoria es: {contador_2}')



print('\n#3 Imprimir números del 1 al 10 al revés\n')

for num in range(10 , 0, -1) :
    print(f'Conteo: {num}')


print('\n#4 Pedir un número y devolver los dígitos totales\n')

num_5 = int(input('Ingresar número: '))
cantidad = 0

for x in range(len(str(num_5))):
    cantidad += 1
else:
    print(f'La cantidad de números es : {cantidad}')
