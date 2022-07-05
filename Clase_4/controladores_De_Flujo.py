edad = 24

if edad>= 18 :
    print("Es adulto")


# Mayoría de edad

age = int(input('Qué edad tienes?: '))

if age >= 18 :
    print("Eres mayor de edad")
else : 
    print('Eres menor')


# Marvel vs CapCom

nombre = input('Cómo te llamas?: ')
preferencia = input('Cuál es tu preferencia? (M o C): ')

condicion_1 = nombre <= "M" and preferencia.upper() == "M"
condicion_2 = nombre >= "N" and preferencia.upper() == "C"

if ((condicion_1) or (condicion_2)) :
    print("Tu grupo es A")
else :
    print("Tu grupo es B")