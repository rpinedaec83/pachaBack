
CREATE DATABASE "SV74090844"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table if not exists salones(
	id_ serial,
	nombre_ varchar(20),
	anio_ date,
	primary key (id_)
);
create table if not exists alumnos(
	id_ serial,
	nombre_ varchar(20),
	edad int, 
	correo varchar(20),
	notas int[],
	id_salon int,
	
	primary key (id_),
	foreign key(id_salon) references salones(id_) ON DELETE SET NULL
);

create table if not exists profesores(
	id_ serial,
	nombre_ varchar(20),
	edad int, 
	correo varchar(20),
	id_salon int,
	
	primary key(id_),
	foreign key(id_salon) references salones(id_) ON DELETE SET NULL
);

create table if not exists cursos(
	id_ serial,
	nombre varchar(20),
	id_profesor int,
	
	primary key(id_),
	foreign key(id_profesor) references profesores(id_) ON DELETE SET NULL
);



insert into salones
values
(1, 'A', '2020-5-1'),
(2, 'B', '2021-7-1'),
(3, 'C', '2022-10-1');


INSERT INTO alumnos (id_, nombre_, edad, correo, notas, id_salon) VALUES
    (1,'Jostin', 55, 'jostinori@gmail.com', ARRAY[20,20,20],(SELECT id_ from salones WHERE nombre_ ='A')),

    (2,'Calvin', 55, 'Calvin@gmail.com', ARRAY[10,10,10],(SELECT id_ from salones WHERE nombre_ ='B')),

	 (3,'Juan', 55, 'Juan@gmail.com', ARRAY[10,5,15],(SELECT id_ from salones WHERE nombre_ ='C')),

	 (4,'Lautaro', 55, 'Lautaro@gmail.com', ARRAY[3,13,15],(SELECT id_ from salones WHERE nombre_ ='B')),

	 (5,'Santiago', 55, 'Santiago@gmail.com', ARRAY[7,17,4],(SELECT id_ from salones WHERE nombre_ ='A')),

	 (6,'Pepe', 55, 'Pepe@gmail.com', ARRAY[8,18,4],(SELECT id_ from salones WHERE nombre_ ='C'));

-- insert into alumnos values (7, 'Corny', 22, 'Corny@gmail.com',ARRAY[0], (SELECT id_ from salones WHERE nombre_ ='C'));
-- cambiar notas -> update alumnos set notas = ARRAY[15,15,15] where id_ = 7
	 
	 

INSERT INTO profesores VALUES
    (1,'Prof1', 70, 'Prof1@gmail.com',(SELECT id_ from salones WHERE nombre_ ='A')),

    (2,'Prof2', 70, 'Prof2@gmail.com',(SELECT id_ from salones WHERE nombre_ ='B')),

	 (3,'Prof3', 70, 'Prof3@gmail.com',(SELECT id_ from salones WHERE nombre_ ='A')),

	 (4,'Prof4', 70, 'Prof4@gmail.com',(SELECT id_ from salones WHERE nombre_ ='B')),

	 (5,'Prof5', 70, 'Prof5@gmail.com',(SELECT id_ from salones WHERE nombre_ ='C')),
     
	 (6,'Prof6', 10, 'Prof6@gmail.com',(SELECT id_ from salones WHERE nombre_ ='C'));


INSERT INTO cursos VALUES
    (1,'Programacion',(SELECT id_ from profesores WHERE id_ ='1')),

    (2,'Finanzas',(SELECT id_ from profesores WHERE id_ ='3')),

	 (3,'Videojuegos',(SELECT id_ from profesores WHERE id_ ='5'));