CREATE DATABASE "a1703782"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


CREATE TABLE "Order" (
    "Order ID" integer PRIMARY KEY,
    "Order Date" date,
    "Ship Date" date,
    "Ship Mode" varchar(255),
    "Customer ID" integer,
    Sales decimal(10,2),
    Quantity integer,
    Discount decimal(10,2),
    Profit decimal(10,2)
);

CREATE TABLE Customer (
    "Customer ID" integer PRIMARY KEY,
    "Customer Name" varchar(255),
    Segment varchar(255),
    Country varchar(255),
    City varchar(255),
    State varchar(255),
    "Postal Code" varchar(255),
    "IdRegion" integer REFERENCES Region(IdRegion)
);

CREATE TABLE Product (
    "Product ID" integer PRIMARY KEY,
    "Product Name" varchar(255),
    "Sub-Category ID" integer REFERENCES "Sub-Category"("Sub-Category ID")
);

CREATE TABLE Category (
    "Category ID" integer PRIMARY KEY,
    Category varchar(255)
);

CREATE TABLE "Sub-Categories" (
    "Sub-Category ID" integer PRIMARY KEY,
    "Sub-Category" varchar(255),
    "Category ID" integer REFERENCES Category("Category ID")
);

CREATE TABLE Region (
    IdRegion integer PRIMARY KEY,
    Region varchar(255)
);

