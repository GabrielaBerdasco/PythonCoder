import sys

if len(sys.argv) == 3 :
    nota_1 = int(sys.argv[1])
    nota_2 = int(sys.argv[2])

    if nota_1 >= 7 and nota_2 >= 7 :
        print('Promocionado')
    elif nota_1 >= 4 and nota_2 >= 4 :
        print('Aprobado, debe rendir final')
    elif nota_1 < 4 and nota_2 < 4 :
        print('Desaprobó ambos parciales, debe recursar.')
    elif nota_1 < 4 :
        print('Desaprobado, debe recuperar el primer parcial.')
    elif nota_2 < 4 :
        print('Desaprobado, debe recuperar el segundo parcial.')
else :
    print('Argumentos incorrectos.')

