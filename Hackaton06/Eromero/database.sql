CREATE DATABASE a0973286;

\c a0973286;

CREATE TABLE alumnos (
    nombre TEXT,
    identificador INTEGER PRIMARY KEY,
    edad INTEGER,
    correo TEXT
);

CREATE TABLE salones (
    nombre TEXT PRIMARY KEY,
    anio_escolar INTEGER
);

CREATE TABLE cursos (
    nombre TEXT PRIMARY KEY,
    profesor TEXT
);

CREATE TABLE profesores (
    nombre TEXT,
    identificador INTEGER PRIMARY KEY,
    edad INTEGER,
    correo TEXT
);