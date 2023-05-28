CREATE DATABASE "SV73030216"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table Region(
	IdRegion serial,
	Region varchar(50) not null,
	primary key(IdRegion)
)

create table Segment(
	IdSegment serial,
	Segment varchar(50) not null,
	primary key(IdSegment)
)

create table Customer(
	CustomerID varchar(50),
	Customer_name varchar(100) not null,
	IdSegment int,
	primary key(CustomerID)
)

create table ship_mode(
	IdShip_mode serial,
	ship_mode varchar(50) not null,
	primary key(IdShip_mode)
)

create table Orders(
	IdOrder varchar(100),
	order_date date,
	ship_date date,
	ship_mode int,
	customer varchar(100),
	primary key(IdOrder)
)

create table Place(
	IdPlace serial,
	country varchar(100),
	city varchar(100),
	postal_code int,
	primary key(IdPlace)
)

create table Product(
	IdProduct varchar(100),
	Category varchar(100),
	Sub_category varchar(100),
	Product_name varchar(500),
	primary key(IdProduct)
)
