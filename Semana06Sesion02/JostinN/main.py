from conexion import conexion
from clases import Alumno, Salon, Profesor, Curso
from utils import Menu
from tabulate import TableFormat, tabulate

#ctrl + k + C -> comentar
#ctrl + k + U -> descomentar

# conn = conexion()
# listClientes = []
# def cargaClientes():
#     resultado = conn.consultarBDD("Select * from alumnos;")
#     print(resultado)
#     #for jug in resultado:
#     #    #print(f"{jug[0]},  {jug[1]} , {jug[2]}")
#     #    cliente = Jugador(jug[0], jug[1], jug[2])
#     #    listClientes.append(cliente)


# cargaClientes()

# query = "insert into jugador values('10', 'nuevo', DATE '1995-05-09');"
# datos = conexion.consultarBDD(query)
# header = ['ID','Nombre','Cumple']

# print(tabulate(datos, headers=header, tablefmt='fancy_grid'))
# conexion.ejecutarBDD(query)


Alumno_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Profesor_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Salon_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
Cursos_op = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
MenuMain_op = {"Menu Alumnos":"1","Menu Profesores":"2","Menu Salones":"3","Menu Cursos":"4","Exit":"0"}



Menu_Alumno = Menu("ALUMNOS",Alumno_op)

Menu_Profesor = Menu("PROFESORES",Profesor_op)

Menu_Salon = Menu("SALONES",Salon_op)

Menu_Cursos = Menu("CURSOS",Cursos_op)

Menu_Main = Menu("MENU PRINCIPAL",MenuMain_op)



conn = conexion()

f = True
while f:
    ans = Menu_Main.show()

    if(ans == "0"):
        f = False

    if(ans.upper() == "1"):
        respuesta = Menu_Alumno.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            edad = input("edad: ")
            correo = input("correo: ")
            notas = input("notas:([15,15,15]): ")

            data = conn.consultarBDD("select * from salones")
            headers = ['ID', 'Nombre','Año']   
            print("----Salones actuales----") 
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
            salon_id = int(input("Id de salon del alumno: "))

            alumno = Alumno(nombre,edad,correo,notas,salon_id)
            last_index = int(conn.consultarBDD("SELECT id_ FROM alumnos ORDER BY id_ DESC LIMIT 1;")[0][0])
            query = f"insert into alumnos values ({last_index+1},'{alumno.nombre}', {alumno.edad}, '{alumno.correo}', ARRAY{alumno.notas}, {alumno.id_salon});"
            if(conn.ejecutarBDD(query)):
                print("Se creo el alumno correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("Id de alumno: "))

            query = f"SELECT * FROM alumnos WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Edad','correo','Notas','Salon']            
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de alumno para actualizar: "))
            query = f"SELECT * FROM alumnos WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Edad','correo','Notas','Salon'] 
            if(data):
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                nombre = input("Nombre: ")
                edad = input("edad: ")
                correo = input("correo: ")
                notas = input("notas:([15,15,15]): ")

                data = conn.consultarBDD("select * from salones")
                headers = ['ID', 'Nombre','Año']   
                print("----Salones actuales----") 
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                salon_id = int(input("Id de salon del alumno: "))


                query = f"update alumnos set nombre_ = '{nombre}', edad = 1, correo = '{correo}', notas = ARRAY{notas}, id_salon = {salon_id} where id_ = {id_} ;"
                if(conn.ejecutarBDD(query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de alumno para borrar: "))
            query = f"delete from alumnos WHERE id_ = {id_}"
            if(conn.ejecutarBDD(query)):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")

    if(ans.upper() == "2"):
        respuesta = Menu_Alumno.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            edad = input("edad: ")
            correo = input("correo: ")

            data = conn.consultarBDD("select * from salones")
            headers = ['ID', 'Nombre','Año']   
            print("----Salones actuales----") 
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
            salon_id = int(input("Id de salon del profesor: "))

            profesor = Profesor(nombre,edad,correo,salon_id)
            last_index = int(conn.consultarBDD("SELECT id_ FROM profesores ORDER BY id_ DESC LIMIT 1;")[0][0])
            query = f"insert into profesores values ({last_index+1},'{profesor.nombre}', {profesor.edad}, '{profesor.correo}', {profesor.id_salon});"
            if(conn.ejecutarBDD(query)):
                print("Se creo el profesor correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("Id de profesor: "))

            query = f"SELECT * FROM profesores WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Edad','correo','Salon']            
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de profesor para actualizar: "))
            query = f"SELECT * FROM profesores WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Edad','correo','Salon'] 
            if(data):
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                nombre = input("Nombre: ")
                edad = input("edad: ")
                correo = input("correo: ")

                data = conn.consultarBDD("select * from salones")
                headers = ['ID', 'Nombre','Año']  
                print("----Salones actuales----") 
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                salon_id = int(input("Id de salon del profesor: "))


                query = f"update profesores set nombre_ = '{nombre}', edad = 1, correo = '{correo}', id_salon = {salon_id} where id_ = {id_} ;"
                if(conn.ejecutarBDD(query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de profesor para borrar: "))
            query = f"delete from profesores WHERE id_ = {id_}"
            if(conn.ejecutarBDD(query)):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")


    if(ans.upper() == "3"):#3333333333
        respuesta = Menu_Salon.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")
            anio = input("Año(yy-mm-dd): ")
            salon = Salon(nombre, anio)

            last_index = int(conn.consultarBDD("SELECT id_ FROM salones ORDER BY id_ DESC LIMIT 1;")[0][0])

            query = f"insert into salones values ({last_index+1},'{salon.nombre}', '{salon.anio}');"
            if(conn.ejecutarBDD(query)):
                print("Se creo el salon correctamente")


        elif(respuesta.upper() =="2"):
            id_salon = int(input("Id de salon: "))

            query = f"SELECT * FROM salones WHERE id_ = {id_salon}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Año']  
            print("----Salones actuales----")           
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de salon para actualizar: "))
            query = f"SELECT * FROM salones WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','Año']  

            if(data):
                print("----Salones actuales----") 
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                nombre = input("Nombre: ")
                anio = input("Año(yy-mm-dd): ")
                salon = Salon(nombre, anio)
                query = f"update salones set nombre_ = '{nombre}' , anio_ = '{anio}' where id_ = {id_};"

                if(conn.ejecutarBDD(query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de salon para borrar: "))
            query = f"delete from salones WHERE id_ = {id_}"
            if(conn.ejecutarBDD(query)):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")

            
    if(ans.upper() == "4"):
        respuesta = Menu_Cursos.show()
        if(respuesta.upper() == "1"):
            nombre = input("Nombre: ")

            data = conn.consultarBDD("select * from profesores")
            headers = ['ID', 'Nombre','Edad', 'Correo', 'ID_Salon']   
            print("----Profesores actuales----") 
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
            profesor_id = int(input("Id de profesor del curso: "))

            curso = Curso(nombre,profesor_id)
            last_index = int(conn.consultarBDD("SELECT id_ FROM cursos ORDER BY id_ DESC LIMIT 1;")[0][0])
            query = f"insert into cursos values ({last_index+1},'{curso.nombre}', {curso.id_profesor});"
            if(conn.ejecutarBDD(query)):
                print("Se creo el curso correctamente")


        elif(respuesta.upper() =="2"):
            id_ = int(input("Id de curso: "))

            query = f"SELECT * FROM cursos WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','ID_Profesor']            
            print(tabulate(data, headers= headers, tablefmt='fancy_grid'))


        elif(respuesta.upper() =="3"):
            id_ = int(input("Id de curso para actualizar: "))
            query = f"SELECT * FROM cursos WHERE id_ = {id_}"

            data = conn.consultarBDD(query)
            headers = ['ID', 'Nombre','ID_Profesor'] 
            if(data):
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                nombre = input("Nombre: ")

                data = conn.consultarBDD("select * from profesores")
                headers = ['ID', 'Nombre','Edad', 'Correo', 'ID_Salon']   
                print("----Profesores actuales----") 
                print(tabulate(data, headers= headers, tablefmt='fancy_grid'))
                profesor_id = int(input("Id de profesor del curso: "))

                query = f"update cursos set nombre = '{nombre}', id_profesor = {profesor_id} where id_ = {id_ };"
                if(conn.ejecutarBDD(query)):
                    print("Se actualziaron correctamente")

        elif(respuesta.upper() =="4"):
            id_ = int(input("Id de curso para borrar: "))
            query = f"delete from cursos WHERE id_ = {id_}"
            if(conn.ejecutarBDD(query)):
                    print("Se borro correctamente")


        elif(respuesta.upper() =="0"):
            print("salir")

        input("Continuar")

    elif(ans == "0"):
        f = False

