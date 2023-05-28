CREATE TABLE Alumnos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    identificador VARCHAR(20),
    edad INT,
    correo VARCHAR(50),
    salon_id INT,
    FOREIGN KEY (salon_id) REFERENCES Salon(id)
);

CREATE TABLE Salon (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    anio_escolar VARCHAR(10)
);

CREATE TABLE Cursos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    profesor_id INT,
    salon_id INT,
    FOREIGN KEY (profesor_id) REFERENCES Profesores(id),
    FOREIGN KEY (salon_id) REFERENCES Salon(id)
);

CREATE TABLE Profesores (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    identificador VARCHAR(20),
    edad INT,
    correo VARCHAR(50)
);