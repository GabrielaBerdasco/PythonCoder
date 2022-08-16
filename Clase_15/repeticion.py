import sys


arg_list = len(sys.argv)

if arg_list == 3 :

    for e in range(arg_list):
        print(sys.argv[e])

else :
    print('Introducir argumentos')