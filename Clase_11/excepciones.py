lista = [10, 11, 12]

lista.pop(1)

print(lista)

def dividir( a: any, b: any ) -> float | None  :

    try :
        a = int(a)
        b = int(b)
        div = a/b

    except ZeroDivisionError:
        print('No se puede realizar la operación')
        
    
    except ValueError :
        print('Uno de los datos no es válido')

    else :
        print(div)
        


while True :

    divisor = input('Ingresar divisor: ')
    dividendo = input('Ingresar dividendo: ')

    dividir(divisor, dividendo)

    exit = input('Desea salir: (s)')

    if exit == 's' :
        break


dict_1 : dict[ str, str ]

dict_1 = { 'saludo': 'hola' }

list_1 : list[int]

list_1 = [3, 4, 'hola']

#try:
    #a = 10

#except Exception as e :
    #print(type(e).__name__) ## nombre de error
    #print(e) ## mensaje de error
#except ValueError :

#except ZeroDivisionError :

#except TypeError :

#else :

#finally :
