from models.persona import Persona


class Profesor(Persona):
    def __init__(self, id, nombre, dni, edad, correo):
        super().__init__(nombre, dni, edad, correo)
        self.id = id
