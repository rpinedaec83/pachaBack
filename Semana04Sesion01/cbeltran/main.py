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

class Persona: 
    def __init__(self, nombre, apellido, dni, direccion = None, sexo = "Masculino"):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

class Propietario(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino", mascota = None):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.mascota = mascota

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino", licencia = "Medicina"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia

        def atenderCita(self , fecha):
            print(f"El medico {self.nombre} va a atenderte el día {fecha}")
            pass

class Enfermero(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino", licencia = "Enfermeria"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia




miMascota = Mascota("Selina", "Gato", "Hembra", 2)
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
