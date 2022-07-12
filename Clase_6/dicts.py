#Inicialmente el diccionario es: animales = {"elefante": ""}

#Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”,  
# “Peepe” y “homero”
#Modificá las claves elefante y delfin con los valores 
# “Trompis”y “Manolo” respectivamente

animales = {'elefante': ''}

animales.update({'perro': 'Bobby', 'tigre': 'Pepe', 'mono': 'Homero'})

animales['elefante'] = 'Trompis'
animales['delfin'] = 'Manolo'

print(animales)