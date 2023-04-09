CREATE DATABASE "A0973286"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE Customers (
    CustomerID VARCHAR(10) NOT NULL,
    CustomerName VARCHAR(50) NOT NULL,
    PRIMARY KEY (CustomerID)
);

CREATE TABLE Locations (
    PostalCode INT NOT NULL,
    Country VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PRIMARY KEY (PostalCode)
);

CREATE TABLE Categories (
    CategoryID SERIAL,
    Category VARCHAR(50) NOT NULL,
    PRIMARY KEY (CategoryID)
);

CREATE TABLE SubCategories (
    SubCategoryID SERIAL,
    SubCategory VARCHAR(50) NOT NULL,
    CategoryID INT NOT NULL,
    PRIMARY KEY (SubCategoryID),
    FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
);

CREATE TABLE Products (
    ProductID VARCHAR(20) NOT NULL,
    SubCategoryID INT NOT NULL,
    ProductName VARCHAR(100) NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (SubCategoryID) REFERENCES SubCategories (SubCategoryID)
);

CREATE TABLE Orders (
    OrderID VARCHAR(20) NOT NULL,
    OrderDate DATE NOT NULL,
    ShipDate DATE NOT NULL,
    ShipMode VARCHAR(50) NOT NULL,
    CustomerID VARCHAR(10) NOT NULL,
    Segment VARCHAR(50) NOT NULL,
    IDRegion INT NOT NULL,
    PostalCode INT NOT NULL,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID),
    FOREIGN KEY (PostalCode) REFERENCES Locations (PostalCode)
);

CREATE TABLE Order_Details (
    RowID INT NOT NULL,
    OrderID VARCHAR(20) NOT NULL,
    ProductID VARCHAR(20) NOT NULL,
    Sales DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    Discount DECIMAL(4, 2) NOT NULL,
    Profit DECIMAL(10, 4) NOT NULL,
    PRIMARY KEY (RowID),
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
);
