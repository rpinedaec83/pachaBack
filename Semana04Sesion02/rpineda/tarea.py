import os
import time
import utils
import json


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
#----------------------------------------------------------------------------------

class Persona:
    def __init__(self, nombre, apellido, edad, id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.id = id

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, id, codigoCliente):
        super().__init__(nombre, apellido, edad, id)
        self.codigoCliente = codigoCliente

    def toDic(self):
        d = {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad":self.edad,
            "id":self.edad,
            "codigoCliente":self.codigoCliente
        }
        return d
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, id, codigoEmpleado, area):
        super().__init__(nombre, apellido, edad, id)
        self.codigoEmpleado = codigoEmpleado
        self.area = area

class Producto:
    def __init__(self,nombre, precio, fechaCaducidad, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.fechaCaducidad = fechaCaducidad
        self.cantidad = cantidad

class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("\n")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.nombreMenu.upper()+"::::::::::::::::::::"+color.END)   
            print("\n")
            for (key, value) in self.listaOpciones.items():
                print(key+color.GREEN+" → "+color.END+value)
            print("\n")
            ans = input(color.YELLOW+"Por favor, ingrese su opción: "+color.END)
            print("\n")
            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break
            b = 0
            for (key, value) in self.listaOpciones.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                time.sleep(3)
        return ans             


    def limpiarPantalla(self):
        def clear():
                #return os.system('cls')
            return os.system('clear')
        clear()        


Home_op = {"Clientes":"1","Empleados":"2","Exit":"0"}
Main_menu = Menu("home",Home_op)

Client_op = {"Agregar cliente":"1","Lista de clientes":"2","Remover cliente":"3","Exit":"0"}
Menu_client = Menu("cliente",Client_op)

Employee_op = {"Horas de trabajo":"1","Inventario":"2","Exit":"0"}
Menu_Employee = Menu("trabajador",Employee_op)

Inventory_op = {"Agregar producto":"1","Consulta":"2","Remover producto":"3","Exit":"0"}
Menu_Inventory = Menu("inventario",Inventory_op)

Inventory_consult_op = {"Buscar producto":"1","Contar items":"2","Calcular valor del inventario":"3","Exit":"0"}
Consult_inv = Menu("consulta de inventario",Inventory_consult_op)

Working_hrs_op = {"Check-in":"1","Check-out":"2","Exit":"0"}
Working_hrs = Menu("horas trabajadas",Working_hrs_op)



client_list = []
product_list = []
client_listDic = []

fileCliente = utils.fileManager("cliente.txt")


def cargainicial():
    res = fileCliente.leerArchivo()
    print(res)
    if(res != ""):
        listTempCliente = json.loads(res)
        for dic in listTempCliente:
            newCliente = Cliente(dic["nombre"],dic["apellido"],dic["edad"],dic["id"], dic["codigoCliente"])
            client_listDic.append(newCliente.toDic())
            client_list.append(newCliente)

cargainicial()

f = True
while f:
    ans = Main_menu.show()
    print(ans)
    if(ans.upper() == "1"):
        ans = Menu_client.show()
        if(ans.upper() == "1"):
            print("Ingrese la información del cliente:")
            nombre = input("Nombre del cliente     : ")
            apellido = input("Apellido del cliente: ")
            edad = input("Edad del cliente:")
            id = input("DNI del cliente:")
            codigoCliente = input("Código del cliente     :")
            print("")
            o = True
            while o:
                print(f"Esta seguro que desea agregar al cliente {nombre} a lista de clientes? (Y/N)")
                ans = input(color.YELLOW+"Answer: "+color.END)
                if(ans.upper() =="Y"):
                    client_n = Cliente(nombre,apellido,edad,id,codigoCliente)
                    client_list.append(client_n)
                    print("")
                    print(color.GREEN+f"{nombre} fue agregado ☑"+color.END)
                    client_listDic.append(client_n.toDic())
                    jsonString = json.dumps(client_listDic)
                    fileCliente.borrarArchivo()

                    fileCliente.escribirArchivo(jsonString)
                    break
                elif(ans.upper() =="N"):                  
                    print("")
                    break
                else:
                    print("")
                    print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                    print("")
        elif(ans.upper() =="2"):
            print(color.GREEN+"Esta es la lista de clientes ☑:"+color.END)
            for client in client_list:
                print(f"|{client.nombre}|{client.apellido}|{client.edad}|{client.id}|{client.codigoCliente}|")
            g = True
            while g:
                print("")
                print("Desea ir al menu o salir del programa? (M/0)")
                ans = input(color.YELLOW+"Answer: "+color.END)
                if(ans.upper() =="M"):
                    g = False
                    break
                elif(ans.upper() =="0"):
                    g = False
                    f = False
                    break
                else:
                    print("")
                    print(color.RED+"Opción no valida, escoja una opción valida"+color.END)
                    print("")

    elif(ans == "2"):
        ans = Menu_Employee.show()
    