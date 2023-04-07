class Pet:
    __isActive = True  # variable privada __nameVariable

    # self define las key del objeto
    def __init__(self, name, specie, sex, age):
        self.name = name
        self.specie = specie
        self.sex = sex
        self.age = age

    # getters and setters
    def getIsActive(self):
        return self.__isActive

    def setIsActive(self, newValue):
        self.__isActive = newValue

    # getters and setters with property
    @property
    def pIsActive(self):
        return self.__isActive

    @pIsActive.setter
    def pIsActive(self, newValue):
        self.__isActive = newValue


class Person:
    def __init__(self, name, lastname, idCard, address=None, sex="male"):
        self.name = name
        self.lastname = lastname
        self.idCard = idCard
        self.address = address
        self.sex = sex


# Herencia:
# heredando person a owner
class Owner(Person):
    def __init__(self, name, lastname, idCard, address=None, sex="male", pet=None):
        super().__init__(name, lastname, idCard, address, sex)
        self.pet = pet


class Doctor(Person):
    def __init__(self, name, lastname, idCard, address=None, sex="male", license="vet"):
        super().__init__(name, lastname, idCard, address, sex)
        self.license = license

    def attendAppointment(self, date, pet=None):
        # se coloca self para indicar que viene de la clase padre (Doctor)
        if pet == None:
            print(f"El médico {self.name} atenderá el día: {date}")
        else:
            print(f"El médico {self.name} atenderá el día: {date} a tu mascota {pet}")

    def attendSurgery(self, information):
        print(
            f"El médico {self.name} realizará la cirugía a {information[0]} del tipo {information[2]}"
        )


class Nurse(Person):
    def __init__(
        self, name, lastname, idCard, address=None, sex="male", license="nurse"
    ):
        super().__init__(name, lastname, idCard, address, sex)
        self.license = license


myPet = Pet("Tom", "cat", "male", 1)
print(myPet.name)
print(myPet.specie)


yourPet = Pet("Pelusa", "cat", "female", 2)
print(yourPet.name)

# Obtner variable privada: con getters and setters
print(myPet.getIsActive())  # true
# cambiando estado de variable privada
myPet.setIsActive(False)
print(myPet.getIsActive())  # false


# Con decoradores
print(myPet.pIsActive)
myPet.pIsActive = True
print(myPet.pIsActive)

# Ingresando valores en forma genérica
doctor1 = Doctor("Roberto", "Pineda", "00012325656")
print(doctor1.name)
print(doctor1.license)
print(doctor1.address)
print(doctor1.idCard)

# Ingresando valores específicando el key
owner1 = Owner(
    pet=myPet,  # pasando dato de clase pet
    name="David",
    lastname="Lopez",
    idCard="154615486",
    address="123 avenue",
    sex="Male",
)
print(owner1.name)
print(owner1.pet.name)

nurse1 = Nurse(name="Juan", lastname="Perez", idCard="373737373")
print(nurse1.name)
print(nurse1.license)

doctor1.attendAppointment("31/03/2023")
doctor1.attendAppointment("31/03/2023", yourPet.name)


lst = [myPet.name, "28/02/2024", "Esterilización"]
doctor1.attendSurgery(lst)
