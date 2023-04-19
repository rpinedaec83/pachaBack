
--script de la base de datos bd_colegio
CREATE DATABASE sv70098291
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

Create table salon(
	idSalon serial primary key,
	nombre varchar(50),
	anioEscolar varchar(50)
);

create table alumno(
	idAlumno serial primary key,
	nombre varchar(50),
	dni varchar(8),
	edad int,
	email varchar(50),
	idSalon int,
	foreign key (idSalon) REFERENCES salon(idSalon)
);

create table profesor(
	idProfesor serial primary key,
	nombre varchar (50),
	dni varchar(8),
	edad int,
	email varchar(50)
);

create table curso(
	idCurso serial primary key,
	nombre varchar(50),
	idProfesor int,
	idAlumno int,
	foreign key (idProfesor) REFERENCES profesor(idProfesor),
	foreign key (idAlumno) REFERENCES alumno(idAlumno)
);

------------------------INSERTS------------------------------

insert into salon (nombre,anioEscolar) 
values('Primer Grado', 1),
('Segundo Grado', 2),
('Tercer Grado', 3),
('Cuarto Grado', 4),
('Quinto Grado', 5)
;

insert into alumno (nombre,dni,edad,email,idSalon)
values ('Carlos Guevara','87568475',11,'cguevara@email.com',1),
('Alvaro Paredes','93472364',12,'aparedes@email.com',2),
('Juan Pinto','94263745',13,'jpinto@email.com',3),
('José Beltran','19861933',14,'jbeltran@email.com',4),
('Alicia Peralta','93483726',15,'aperalta@email.com',5)

insert into profesor(nombre, dni, edad, email)
values ('Patricio Gimenez','84556786',35,'pgimenez@email.com'),
('Alexander Arriola','18237411',54,'aarriola@email.com'),
('Maynar keenan','22372611',45,'mkeenan@email.com'),
('Jason Becker','22334546',42,'pgimenez@email.com'),
('Berta Suarez','45743384',25,'bsuarez@email.com')

insert into curso (nombre,idProfesor,idAlumno)
values ('Álgebra 1',3,2),
('Aritmética 2',5,4),
('Trigonometría',1,5),
('Literatura 1',4,1),
('Química 1',2,3)