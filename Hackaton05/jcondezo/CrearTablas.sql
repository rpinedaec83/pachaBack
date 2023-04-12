--create table Orders(
--	idOrderId serial,
--	orderId varchar (30) not null,
--	primary key (idOrderId)
--)
create table OrderDate(
	idOrderDate serial,
	Orderdate date not null,
	primary key (idOrderDate)
)

create table  ShipDate(
	idShipDate serial,
	ShipDate date not null,
	primary key (idShipDate)
)

create table ShipMode(
	idShipMode serial,
	ShipMode varchar (30) not null,
	primary key (idShipMode)
)

create table Segment(
	idSegment serial,
	Segment varchar (30) not null,
	primary key (idSegment)
)

create table Customer(
	Customer_ID serial,
	Customer varchar (30) not null,
	primary key (Customer_ID)
)

---
create table Product(
	idProduct serial,
	Product_ID varchar (30) not null,
	primary key (idProduct)
)

--
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


create table City(
	idCity serial,
	City varchar (30) not null,
	primary key (idCity)
)

create table ProductName(
	idProductName serial,
	ProductName varchar (30) not null,
	primary key (idProductName)
)