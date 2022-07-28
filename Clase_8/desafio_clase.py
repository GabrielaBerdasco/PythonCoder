f = open( 'my_file.txt', 'w' )

mascots_amount = int(input('Cantidad de mascotas a guardar: '))
data = {}

for x in range(mascots_amount):
    data['name'] = input('Nombre: ')
    data['type'] = input('Especie: ')
    data['age'] = input('Edad: ')
    f.write(f'{data["name"]}, {data["type"]}, {data["age"]} \n')

print("Archivo creado correctamente")

f.close()

f = open( 'my_file.txt', 'r' )

data_to_print = f.read()

print(f"Los datos ingresados son: \n{data_to_print}")

f.close()