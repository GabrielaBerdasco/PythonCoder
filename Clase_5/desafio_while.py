num = 5

while num > 0 :
    print(f"{num}")
    num -= 1
else :
    print("Terminó el conteo!")


#Desafío genérico, NÚMEROS

num = 3
suma = 0

while num != 0 :
    num = int(input('Ingrese un número entre 0-9: '))
    print(f'El número ingresado es: {num}')
    suma += num
    
else : 
    print(f'La sumatoria de los números ingresados es: {suma}')
