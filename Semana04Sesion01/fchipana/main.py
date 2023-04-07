class Mascota:
    # Esta es una variable privada
    __EsActivo = True
    def __init__(self, nombre, especie, sexo, edad):
        # Estas son variables publicas
        self.nombre = nombre
        self.especie = especie
        self.sexo = sexo
        self.edad = edad

#Modificar Variable Privada con 'get' y 'set'
    def getEsActivo(self):
        return self.__EsActivo
    
    def setEsActivo(self, nuevoValor):
        self.__EsActivo = nuevoValor

#Modificar Variable Privada con 'property'
    @property
    def pEsActivo(self):
        return self.__EsActivo
    
    @pEsActivo.setter
    def pEsActivo(self,nuevoValor):
        self.__EsActivo = nuevoValor

# Crear una clase modelo (Persona)

class Persona:
    def __init__(self,nombre,apellido,dni,direccion=None,sexo="Masculino"):
        self.nombre = nombre
        self.apellido =apellido
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

# Reutilizar parametros de una clase (Persona)

class Propietario(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino",mascota=""):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.mascota = mascota

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino",licencia="Veterinario"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia

    def atenterCita(self, fecha, mascota =None):
        if (mascota==None):
            print(f"El medido {self.nombre} va a atenderte el dia {fecha}.")
        else:
            print(f"El medido {self.nombre} va a atenderte el dia {fecha} a tu mascota {mascota}.")

    def atenderCirugia(self,datos):
        print(f"El doctor {self.nombre} va a realizar una cirugia el {datos[1]} a la mascota {datos[0]} del tipo {datos[2]}.")
        # for dato in datos:
        #     print(dato)

class Enfermero(Persona):
    def __init__(self, nombre, apellido, dni, direccion=None, sexo="Masculino",licencia="Enfermera"):
        super().__init__(nombre, apellido, dni, direccion, sexo)
        self.licencia = licencia


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

medico1 = Medico("Roberto","Pineda","001575291")
print(medico1.nombre)
print(medico1.licencia)
print(medico1.direccion)
print(medico1.sexo)

propietario1 = Propietario(nombre="David",apellido="Lopez",dni="001575293",direccion="Direccion Aleatoria",mascota=miMascota)
print(propietario1.nombre)
print(propietario1.mascota.nombre)

enfermero1 = Enfermero(nombre="Juan", apellido="Perez", dni="373737373")
print(enfermero1.nombre)
print(enfermero1.licencia)

medico1.atenterCita("28/03/2023")
medico1.atenterCita("28/03/2023","Selina")


lst = ["Selina","28/03/2023","Esterilizacion"]

medico1.atenderCirugia(lst)

print(propietario1.mascota.nombre)