import sys

print(sys.argv)

if sys.argv == 3 :

    for e in range(int(sys.argv[2])):
        print(sys.argv[1])

else :
    print('Introducir argumentos')