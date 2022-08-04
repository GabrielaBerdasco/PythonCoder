class Atleta :

    def __init__(self, nombre, apellido, altura, peso, telefono) :
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.__telefono = telefono

    def set_imc(self) :
        self.imc = self.peso / (self.altura * self.altura)

    def get_datos_atleta(self) :
        return f'El atleta {self.nombre} {self.apellido} tiene un imc de: {self.imc}'

atleta1 = Atleta('Julián', 'Gonzalez', 1.93, 75, 263522524)

atleta1.set_imc()

print(atleta1.get_datos_atleta())