
CREATE DATABASE "SV41930377"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table Orders(
	idOrderId serial,
	orderId varchar (30) not null,
	primary key (idOrderId)
)

create table ShipDate(
	idShipDate serial,
	ShipDate varchar (30) not null,
	primary key (idShipDate)
)


create table ShipDate(
	idShipDate serial,
	ShipDate varchar (30) not null,
	primary key (idShipDate)
)

create table ShipDate(
	idShipDate serial,
	ShipDate varchar (30) not null,
	primary key (idShipDate)
)

-- TABLA SEGMENT

create table Segment(
	idSegment serial,
	Segment varchar (30) not null,
	primary key (idSegment)
)

-- TABLA CUSTOMER

create table Customer(
	Customer_ID serial,
	Customer varchar (30) not null,
	primary key (Customer_ID)
)

--  TABLA  PRODUCT

create table Product(
	idProduct serial,
	Product_ID varchar (30) not null,
	primary key (idProduct)
)
create table SubCategory(
	idSubCategory serial,
	SubCategory varchar (30) not null,
	primary key (idSubCategory)
)

create table Category(
	idCategory serial,
	Category varchar (30) not null,
	primary key (idCategory)
)


create table State(
	idState serial,
	State varchar (30) not null,
	primary key (idState)
)


create table Region(
	idRegion serial,
	Region varchar (30) not null,
	primary key (idRegion)
)


create table PostalCode(
	idPostalCode serial,
	PostalCode varchar (30) not null,
	primary key (idPostalCode)
)

-- TABLA CITYclear

create table City(
	idCity serial,
	City varchar (30) not null,
	primary key (idCity)
)

--- TABLA PRODUCT NAME

create table ProductName(
	idProductName serial,
	ProductName varchar (30) not null,
	primary key (idProductName)
)