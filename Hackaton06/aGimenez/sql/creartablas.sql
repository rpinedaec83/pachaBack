create table if not exists Alumno(
    identAlumno varchar(15) primary key ,
    nombreAlumno varchar(30) not null,
    edad int not null,
    correo varchar(30) not null
);

create table if not exists Profesor(
    identProfesor varchar(15) primary key,
    nombreProfesor varchar(30) not null,
    edad int not null,
    correo varchar(30) not null
);

create table if not exists Curso(
    IdCurso serial primary key,
    nombreCurso varchar(30) not null
);

create table if not exists Salon(
    IdSalon serial primary key,
    nombreSalon varchar(25) not null
);

create table if not exists CursoProfesor(
	IdCursoProfesor serial primary key,
	IdCurso serial,
	IdentProfesor varchar(15),
	foreign key (IdCurso) references Curso(IdCurso),
	foreign key (IdentProfesor) references Profesor(IdentProfesor)
);

create table if not exists SalonAlumno(
	IdSalonAlumno serial primary key,
	IdSalon serial,
	IdentAlumno varchar(15),
	foreign key (IdSalon) references Salon(IdSalon),
	foreign key (IdentAlumno) references Alumno(IdentAlumno)
);

create table if not exists SalonProfesor(
	IdSalonProfesor serial primary key,
	IdSalon serial,
	IdentProfesor varchar(15),
	foreign key (IdSalon) references Salon(IdSalon),
	foreign key (IdentProfesor) references Profesor(IdentProfesor)
);

create table if not exists NotaBimestral(
	idNotaBimestral serial primary key,
	identAlumno varchar(15),
	nota decimal(18,2) not null,
	anioEscolar int not null,
	bimestre varchar(10) not null,
	foreign key (IdentAlumno) references Alumno(IdentAlumno)
);