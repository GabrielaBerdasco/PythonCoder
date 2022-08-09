class Mamifero():
    def __init__(self, cantidad_mamas, esperanza_vida):
        self.cant_mamas = cantidad_mamas
        self.esperanza_vida = esperanza_vida
        
    def mamar(self):
        print(f'El animal se está alimentado.')

    def nacer(self):
        print(f'Nace un espécimen.')

class AnimalMarino():
    def __init__(self, tiene_branquias, especie):
        self.tiene_branquias = tiene_branquias
        self.especie = especie

    def nadar():
        print(f'El animal marino está nadando...')

class Cetaceo(Mamifero, AnimalMarino):
    def __init__(self, cantidad_mamas, esperanza_vida, tiene_branquias, especie, nombre_comun, notas, vive_en, peso):
        Mamifero.__init__(self, cantidad_mamas, esperanza_vida)
        AnimalMarino.__init__(self, tiene_branquias, especie)
        self.nombre_comun = nombre_comun
        self.notas = notas
        self.vive_en = vive_en
        self.peso = peso

    def __str__(self):
        return f'Notas sobre la especie: {self.notas}.'

    def nacer(self):
        print(f'Nace un espécimen de la especie {self.especie} y vive en: {self.vive_en}.')

    def nadar(self):
        print(f'La especie {self.especie} está nadando...')


cetaceo_1 = Cetaceo(
    cantidad_mamas = 0, 
    esperanza_vida = 20, 
    tiene_branquias = False, 
    especie = 'Phocoena sinus',
    nombre_comun = 'Vaquita Marina', 
    notas = 'Cetáceos más pequeños, en peligro de extinción', 
    vive_en = 'endémica de México', 
    peso = 45
)

cetaceo_2 = Cetaceo(4, 25, False, 'Delphinus Delphi', 'Delfín común', 'Es un delfín delgado, con un hocico más corto que el delfín común costero (Delphinus capensis).', 'aguas tropicales y subtropicales', 90)

cetaceo_1.nacer()
cetaceo_1.nadar()
print(cetaceo_1)

cetaceo_2.nacer()
print(cetaceo_2)