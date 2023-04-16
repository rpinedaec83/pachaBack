CREATE TABLE alumnos(
	id serial primary key,
    nombre varchar(20) not null,
    dni varchar(20) not null,
    edad int not null,
	correo varchar(40) not null
);

CREATE TABLE profesores(
	id serial primary key,
    nombre varchar(20) not null,
    dni varchar(20) not null,
    edad int not null,
	correo varchar(40) not null
);

CREATE TABLE cursos(
	id serial primary key,
    nombre varchar(30) not null
);

CREATE TABLE bimestres(
	id serial primary key,
    nombre varchar(20) not null
);


CREATE TABLE cursosProfesores(
	id serial primary key,
    id_curso int not null,
    id_profesor int not null,
    FOREIGN KEY(id_curso) references cursos(id),
    FOREIGN KEY(id_profesor) references profesores(id)
);

CREATE TABLE salones(
	id serial primary key,
    seccion varchar(50) not null,
    id_alumno int not null,
    id_periodo int not null,
    id_profesor int not null,
    FOREIGN KEY(id_alumno) references alumnos(id),
    FOREIGN KEY(id_profesor) references profesores(id)
);

CREATE TABLE notas(
	id serial primary key,
    valor int not null,
    id_alumno int not null,
    id_curso int not null,
    id_bimestre int not null,
    FOREIGN KEY(id_alumno) references alumnos(id),
    FOREIGN KEY(id_curso) references cursos(id),
    FOREIGN KEY(id_bimestre) references bimestres(id)
);