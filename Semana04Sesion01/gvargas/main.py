class Mascota:
    __EsActivo = True
    def __init__(self, nombre, especie, sexo, edad):
        self.nombre = nombre
        self.especie = especie
        self.sexo = sexo
        self.edad = edad
    
    def getEsActivo(self):
        return self.__EsActivo

    def setEsActivo(self, nuevoValor):
        self.__EsActivo = nuevoValor

    @property
    def pEsActivo(self):
        return self.__EsActivo
    
    @pEsActivo.setter
    def pEsActivo(self, nuevoValor):
        self.__EsActivo = nuevoValor

miMascota = Mascota("Selina","Gato","Hembra",2)

print(miMascota.nombre)
print(miMascota.especie)

tuMascota = Mascota("Pancho","Gato","Macho",1)

print(tuMascota.nombre)

print(miMascota.getEsActivo())
miMascota.setEsActivo(False)
print(miMascota.getEsActivo())

print(miMascota.pEsActivo)
miMascota.pEsActivo = True
print(miMascota.pEsActivo)
