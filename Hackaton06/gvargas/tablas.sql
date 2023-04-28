create table Alumnos(
	IdAlumno serial,
	Nombre varchar(250) not null,
	Edad int not null,
	Correo varchar(500),
	Salon varchar(100) not null,
	Notas double precision,
	primary key(IdAlumno)
)

create table Salon(
	Nombre varchar(100) not null,
	Año_escolar int not null,
	primary key(Nombre)
)

create table Cursos(
	Nombre varchar(100) not null,
	Profesor int,
	primary key(Nombre)
)

create table Profesor(
	IdProfesor serial,
	Nombre varchar(250) not null,
	Edad int not null,
	Correo varchar(500),
	Salon varchar (100),
	primary key(IdProfesor)
)
