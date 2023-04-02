class Mascota:
    __EsActivo = True
    def __init__(self, nombre, especie, sexo, edad):
        self.nombre = nombre
        self.especie = especie
        self.sexo = sexo
        self.edad = edad
    
    def getEsActivo(self):
        return self.__EsActivo
    
    def setEsActivo(self, nuevo_valor):
        self.__EsActivo = nuevo_valor

    @property
    def pEsActivo(self):
        return self.__EsActivo
    
    @pEsActivo.setter
    def pEsActivo(self, nuevo_valor):
        self.__EsActivo = nuevo_valor

class Persona:
    def __init__(self, nombre, apellido, dni, direccion, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

class Propietario(Persona):
    def __init__(self, nombre, apellido, dni, direccion, sexo = "Masculino", mascota = None):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.mascota = mascota

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, direccion = None, sexo = "Masculino", licencia = "Veterinario"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia
        
    def atenderCita(self, fecha, mascota=None):
        if(mascota==None):
            print(f"El medico {self.nombre} va atenderte el dia {fecha}")
        else:
            print(f"El medico {self.nombre} va atenderte el dia {fecha} a tu mascota {mascota}")

    def atenderCirugia(self, datos):
        #for dato in datos:
           # print(dato)
        print(f"El medico {self.nombre} va a realizar una cirugia el {datos[1]} a la mascota {datos[0]} del tipo {datos[2]}  ")
        

class Enfermero(Persona):
    def __init__(self, nombre, apellido, dni, direccion = None, sexo = "Masculino", licencia = "enfermería"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia

miMascota = Mascota("Selina","Gato","Hembra",2)

print(miMascota.nombre)
print(miMascota.especie)
print(miMascota.sexo)

tuMascota = Mascota("Pancho", "Gato", "Macho", 1)
print(tuMascota.nombre)
print(tuMascota.especie)
print(tuMascota.sexo)

print(miMascota.getEsActivo())
miMascota.setEsActivo(False)
print(miMascota.getEsActivo())

print(miMascota.pEsActivo)
miMascota.pEsActivo = True
print(miMascota.pEsActivo)

medico1 = Medico("Herless", "Acuña", '41598947')
print(medico1.nombre)
print(medico1.apellido)
print(medico1.licencia)
print(medico1.sexo)
print(medico1.direccion)

propietario1=Propietario(nombre="Daniel", apellido= "Alvarez", dni="41598947", direccion="Lima", mascota=miMascota)
print(propietario1.nombre)
print(propietario1.mascota.nombre)

enfermero1 = Enfermero(nombre="Juan", apellido="Perez", dni="12546465")
print(enfermero1.nombre)
print(enfermero1.licencia)

medico1.atenderCita("28/03/2023")
medico1.atenderCita("28/03/2023", "Selina")

lst = ["Selina", "28/03/2023", "Esterilizacion"]
medico1.atenderCirugia(lst)

print(propietario1.mascota.nombre)