# Creación de la base de datos.

CREATE DATABASE "SV70098291"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table Region(
	idRegion serial,
	region varchar(50) not null,
	primary key (idRegion)
);

create table State(
	idState serial,
	nameState varchar(50),
	foreign key idRegion REFERENCES Region(idRegion),
	primary key (idState)
);
create table City(
	idCity serial,
	nameCity varchar(50),
	postalCode varchar(5),
	idState integer REFERENCES State(idState),
	primary key (idCity)
);

create table Customer  (
	idCustomer serial,
	nameCustomer varchar(225),
	codeCustomer varchar(50),
	foreign key idCity integer REFERENCES City(idCity),
	primary key (idCustomer)
);

create table Ship (
	idShip serial,
	shipMode varchar(50),
	shipDate date,
	primary key (idShip)
);

create table Orden (
	idOrden serial,
	orderCode varchar(50),
	orderDate date,
	primary key (idOrden)
);

create table Category(
	idCategory serial,
	categoryName varchar (50),
	primary key (idCategory)
);

create  table SubCategory(
	idSubcategory serial,
	subCategoryName varchar(50),
	primary key (idSubcategory)
);

create table Product (
	idProduct serial,
	productCode varchar(50),
	productName varchar (225),
	foreign key idCategory integer REFERENCES Category(idCategory),
	foreign key idSubCategory integer REFERENCES SubCategory(idSubCategory),
	primary key (idProduct)
);
