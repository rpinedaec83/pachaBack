CREATE DATABASE "Hackaton05"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table Region(
	IdRegion serial,
	Region varchar(50) not null,
	primary key(IdRegion)
)

## estado ciudad pais segmento producto categoria

create table customers(
	Idcustomers id,
	namec varchar(50) not null,
    country varchar(50) not null,
	primary key(Idcustomers)
)

create table Orders(
	IdOrders serial,
	Region varchar(50) not null,
	primary key(IdOrders)
)

create table Products(
	IdProducts serial,
	nombreProd varchar(50) not null,
	primary key(IdProducts)
)

create table categories(
	IdCategories serial,
	categoriaa varchar(50) not null,
	primary key(IdCategories)
)

create table Shipment(
	IdShipment serial,
	shipttm varchar(50) not null,
	primary key(IdShipment)
)

create table city(
	Idcity serial,
	city varchar(50) not null,
	primary key(Idcity)
)

create table Postal_code(
	IdPostal_code serial,
	Postal_code varchar(50) not null,
	primary key(IdPostal_code)
)

create table products_in_order(
	Idproducts_in_order serial,
    Idproducts_quality serial,
	products_in_order varchar(50) not null,
	primary key(Idproducts_in_order)
)