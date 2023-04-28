CREATE DATABASE BD_COLEGIO

create table Alumno(
	codAlum serial,
  	nombre varchar(30),
  	identificador varchar(12),
	edad int,
	correo varchar(40),
	primary key (codAlum)
 );
 
 create table Curso(
	codCurso serial,
  	nombre varchar(30),
	primary key (codCurso)
 );
 
 create table Profesor(
	codProf serial,
  	nombre varchar(30),
  	identificador varchar(12),
	edad int,
	correo varchar(40),
	primary key (codProf)
 );
 
 create table cursoProfes(
	codigo serial,
	codProf INT,
	codCurso INT,
	primary key (codigo),
	CONSTRAINT fk_curso FOREIGN KEY(codCurso) REFERENCES Curso(codCurso)
 );
 
 ALTER TABLE cursoProfes
 ADD CONSTRAINT fk_profesor FOREIGN KEY(codProf) REFERENCES Profesor(codProf);
 
 create table Periodo(
	codPeriodo serial,
	nombre varchar(10),
  	Anio int,
  	Mes int,
	primary key (codPeriodo)
 );
 
 create table Salon(
	codSalon serial,
  	codPeriodo INT,
  	codigo int,
	primary key (codSalon),
	CONSTRAINT fk_PERIODO FOREIGN KEY(codPeriodo) REFERENCES Periodo(codPeriodo)
 );
 
 ALTER TABLE Salon
 ADD CONSTRAINT fk_CurProf FOREIGN KEY(codigo) REFERENCES cursoProfes(codigo);
 
 create table Notas(
	codAlum int,
  	Nota1 Numeric(2,2),
	Nota2 Numeric(2,2),
	Nota3 Numeric(2,2),
	Nota4 Numeric(2,2),
	Nota5 Numeric(2,2),
	Nota6 Numeric(2,2),
	CONSTRAINT fk_CodAlum FOREIGN KEY(codAlum) REFERENCES Alumno(codAlum)
 );
 
 