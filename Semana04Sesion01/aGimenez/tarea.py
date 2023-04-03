'''Cajero Automatico en Python con POO'''

class Cajero:
    def __init__(self, codigo, direccion):
        self.codigo = codigo
        self.direccion = direccion

    def retirar(self, saldoCliente, saldoRetiro):
        saldoCliente = saldoCliente - saldoRetiro
        return saldoCliente

    def depositar(self, saldoCliente, saldoDeposito):
        saldoCliente = saldoCliente + saldoDeposito
        return saldoCliente

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Cliente(Persona):
    __saldo = 1000
    def __init__(self, nombre, apellido, dni, nroCuenta):
        super().__init__(nombre, apellido, dni)
        self.nroCuenta = nroCuenta

    @property
    def pSaldo(self):
        return self.__saldo

    @pSaldo.setter
    def pSaldo(self, nuevoValor):
        self.__saldo = nuevoValor

class Acreedor(Persona):
    __saldo = 1500
    def __init__(self, nombre, apellido, dni, nroCuenta):
        super().__init__(nombre, apellido, dni)
        self.nroCuenta = nroCuenta

    @property
    def pSaldo(self):
        return self.__saldo
    
    @pSaldo.setter
    def pSaldo(self, nuevoValor):
        self.__saldo = nuevoValor

cajero = Cajero(2342, "Verona 2131")
cliente = Cliente("Fulanito", "De Tal", 32131411, 12312)
acreedor = Acreedor("Perenganito", "Del Huerto", 34233413, 12123)

print("----------CLIENTE----------")
print("Saldo Anterior: s/", cliente.pSaldo)
clienteRetiro = cajero.retirar(cliente.pSaldo, 200)
cliente.pSaldo = clienteRetiro
print("Saldo Actual: s/", cliente.pSaldo)
print("----------------------------")
print("----------ACREEDOR----------")
print("Saldo Anterior: s/", acreedor.pSaldo)
acreedorDeposito = cajero.depositar(acreedor.pSaldo, 357)
acreedor.pSaldo = acreedorDeposito
print("Saldo Actual: s/", acreedor.pSaldo)