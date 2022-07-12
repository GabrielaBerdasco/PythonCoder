# CONJUNTO O SET

grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}

usuarios = ['Ana', 'Ramón', 'Marta', 'Eric', 'David']

usuarios2 = ['Mario', 'Miguel', 'Esteban']

grupo.update(usuarios)

print(grupo)

#grupo.remove(usuarios2[0])
#grupo.remove(usuarios2[1])
#grupo.discard(usuarios2[2])

for u in usuarios2 :
    grupo.discard(u)

print(grupo)