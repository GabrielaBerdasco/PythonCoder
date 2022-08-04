class Perro :
    especie= "Canis Familiaris"

    def __init__(self, nombre, raza) :
        self.nombre = nombre
        self.raza = raza

    def caminar(self) :
        print('El perro está caminando')

    def jugar(self) :
        print(f'{self.nombre} quiere jugar')

    def correr(self) :
        print(f'Los {self.especie} corren muy rápido')

perro1 = Perro('Chani', 'PP')


class Persona :

    clase = 'Mammalia'
    especie = 'Homo sapiens'

    def __init__(self, nombre, edad, mascota) :
        self.nombre = nombre
        self.edad = edad
        self. mascota = mascota

    def __str__(self) -> str:
        return f'{self.nombre} tiene {self.edad} años y su mascota se llama {self.mascota.nombre}'

    def jugar_con_mascota(self) :
        print(f'{self.nombre} juega con {self.mascota.nombre}')

    def edad_persona(self) :
        print(f'{self.nombre} tiene {self.edad} años.')

persona1 = Persona('Juana', 23, perro1)


print(persona1)

print(perro1.jugar())

print(persona1.jugar_con_mascota())