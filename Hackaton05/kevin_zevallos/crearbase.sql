
CREATE DATABASE "SV72844404"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;



-- Tabla "Orders"
CREATE TABLE Orders (
   Order_ID SERIAL PRIMARY KEY,
   Order_Date DATE,
   Ship_Date DATE,
   Ship_Mode TEXT,
   Customer_ID INTEGER REFERENCES Customers(Customer_ID)
);

-- Tabla "Customers"
CREATE TABLE Customers (
   Customer_ID SERIAL PRIMARY KEY,
   Customer_Name TEXT,
   Segment TEXT,
   Country TEXT,
   City TEXT,
   State TEXT,
   Postal_Code TEXT,
   Region TEXT
);

-- Tabla "Order Details"
CREATE TABLE Order_Details (
   Order_ID INTEGER REFERENCES Orders(Order_ID),
   Product_ID INTEGER REFERENCES Products(Product_ID),
   Category TEXT,
   Sub_Category TEXT,
   Product_Name TEXT,
   Sales NUMERIC,
   Quantity INTEGER,
   Discount NUMERIC,
   Profit NUMERIC,
   PRIMARY KEY (Order_ID, Product_ID)
);

-- Tabla "Products"
CREATE TABLE Products (
   Product_ID SERIAL PRIMARY KEY,
   Category TEXT,
   Sub_Category TEXT,
   Product_Name TEXT
);