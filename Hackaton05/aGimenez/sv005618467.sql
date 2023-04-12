CREATE TABLE city (
    "IdCity" integer PRIMARY KEY NOT NULL,
    "city" character varying NOT NULL
);

CREATE TABLE country (
    "IdCountry" integer PRIMARY KEY NOT NULL,
    "country" character varying NOT NULL
);

CREATE TABLE state (
    "IdState" integer PRIMARY KEY NOT NULL,
    "state" character varying NOT NULL
);

CREATE TABLE region (
    "IdRegion" integer PRIMARY KEY NOT NULL,
    "region" character varying NOT NULL
);

CREATE TABLE customer (
    "idCustomer" character varying PRIMARY KEY NOT NULL,
    "customerName" character varying NOT NULL,
    "IdCountry" integer NOT NULL,
    "IdCity" integer NOT NULL,
    "IdState" integer NOT NULL,
    "postalCode" integer,
    "IdRegion" integer NOT NULL,
    "IdSegment" integer NOT NULL
);

CREATE TABLE "order" (
    "IdOrder" character varying PRIMARY KEY NOT NULL,
    "orderDate" date,
    "shipDate" date,
    "IdShipMode" integer,
    "IdCustomer" character varying
);

CREATE TABLE "orderDetail" (
    "IdOrderDetail" integer PRIMARY KEY NOT NULL,
    "IdOrder" character varying NOT NULL,
    "IdProduct" character varying NOT NULL,
    "quantity" integer NOT NULL,
    "discount" double precision NOT NULL,
    "profit" double precision NOT NULL
);

CREATE TABLE product (
    "IdProduct" character varying PRIMARY KEY NOT NULL,
    "productName" character varying NOT NULL,
    "IdCategory" integer NOT NULL,
    "IdSubCategory" integer NOT NULL,
    "sales" double precision NOT NULL
);

CREATE TABLE segment (
    "IdSegment" integer PRIMARY KEY NOT NULL,
    "segment" character varying NOT NULL
);

CREATE TABLE "shipMode" (
    "IdShipMode" integer PRIMARY KEY NOT NULL,
    "shipMode" character varying NOT NULL
);

CREATE TABLE category (
    "IdCategory" integer PRIMARY KEY NOT NULL,
    "category" character varying NOT NULL
);

CREATE TABLE subcategory (
    "IdSubCategory" integer PRIMARY KEY NOT NULL,
    "subcategory" character varying NOT NULL
);


ALTER TABLE "customer" ADD FOREIGN KEY ("IdCity") REFERENCES "city" ("IdCity");
ALTER TABLE "customer" ADD FOREIGN KEY ("IdCountry") REFERENCES "country" ("IdCountry");
ALTER TABLE "customer" ADD FOREIGN KEY ("IdState") REFERENCES "state" ("IdState");
ALTER TABLE "customer" ADD FOREIGN KEY ("IdRegion") REFERENCES "region" ("IdRegion");
ALTER TABLE "customer" ADD FOREIGN KEY ("IdSegment") REFERENCES "segment" ("IdSegment");

ALTER TABLE "order" ADD FOREIGN KEY ("IdShipMode") REFERENCES "shipMode" ("IdShipMode");
ALTER TABLE "order" ADD FOREIGN KEY ("IdCustomer") REFERENCES "customer" ("IdCustomer");

ALTER TABLE "orderDetail" ADD FOREIGN KEY ("IdOrder") REFERENCES "order" ("IdOrder");
ALTER TABLE "orderDetail" ADD FOREIGN KEY ("IdProduct") REFERENCES "product" ("IdProduct");

ALTER TABLE "orderDetail" ADD FOREIGN KEY ("IdCategory") REFERENCES "category" ("IdCategory");
ALTER TABLE "orderDetail" ADD FOREIGN KEY ("IdSubCategory") REFERENCES "subcategory" ("IdSubCategory");
