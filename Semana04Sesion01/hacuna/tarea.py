'''Cajero automatico en Phyton con POO'''
##Alumno: Herless Acuña
class Cajero:
    def __init__(self, codigo, direccion = None):
        self.codigo = codigo
        self.direccion = direccion
    
    def retiro(self, cantidad_inicial, cantidad_retiro):
        return int(cantidad_inicial) - int(cantidad_retiro)
    
    def deposito(self, cantidad_inicial, cantidad_deposito):
        return int(cantidad_inicial) + int(cantidad_deposito)

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni        

class Cliente(Persona):
    _Saldo = 1000
    def __init__(self, nombre, apellido, dni, nroCuenta):
        super().__init__(nombre, apellido, dni)
        self.nroCuenta = nroCuenta

    def getSaldo(self):
        return self._Saldo
    
    def setSaldo(self, nuevo_saldo):
         self._Saldo = nuevo_saldo
       

class Acreedor(Cliente):
    _Saldo = 2000
    def __init__(self, nombre, apellido, dni, nroCuenta):
            super().__init__(nombre, apellido, dni, nroCuenta)
    
    def getSaldo(self):
        return self._Saldo
    
    def setSaldo(self, nuevo_saldo):
        self._Saldo = nuevo_saldo

cajero1 = Cajero("0004", "Av. Benavides 154 - Surco")

cliente1 = Cliente("Carlos", "lopez", "45687891", "00012546478")

acreedor1 = Acreedor("Arturo", "Perez", "48794454", "0002645587")

print("Bienvenido al cajero", cajero1.codigo)
print("Se encuentra en su cajero de", cajero1.direccion)
opcion = int(input("Ingrese 1 para retiro \nIngrese 2 para deposito\n"))

if opcion == 1:
    retiro1 = int(input("Ingrese el monto a retirar"))
    if retiro1 > cliente1.getSaldo():
        print("Ingrese un monto menor, cantidad insuficiente en su cuenta")
        quit()
    else:
        cliente1.setSaldo(Cajero(cliente1.nroCuenta).retiro(cliente1.getSaldo(),retiro1)) 
        print("Estimado Cliente su saldo disponible es: {}".format(cliente1.getSaldo()))

if opcion == 2:
    deposito1 = int(input("Ingrese el monto a depositar"))
    acreedor1.setSaldo(Cajero(acreedor1.nroCuenta).deposito(acreedor1.getSaldo(),deposito1))
    print("Estimado Cliente su saldo disponible es: {}".format(cliente1.getSaldo()))
    print("Estimado su saldo ahora es: {}".format(acreedor1.getSaldo()))



    

