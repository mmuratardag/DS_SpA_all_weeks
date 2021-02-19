CREATE TABLE products (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	productID INTEGER NOT NULL,
	productName VARCHAR(256),
	supplierID INTEGER,
	categoryID INTEGER,
	quantityPerUnit VARCHAR(256),
	unitPrice REAL,
	unitsInStock INTEGER,
	unitsOnOrder INTEGER,
	reorderLevel INTEGER,
	discontinued BOOLEAN
	);
CREATE TABLE territories (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	territoryID INTEGER,
	territoryDescription VARCHAR(256),
	regionID INTEGER
	);
CREATE TABLE customers (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	customerID VARCHAR(256),
	companyName VARCHAR(256),
	contactName VARCHAR(256),
	contactTitle VARCHAR(256),
	address VARCHAR(256),
	city VARCHAR(256),
	region VARCHAR(256),
	postalCode VARCHAR(256),
	country VARCHAR(256),
	phone VARCHAR(256),
	fax VARCHAR(256)
	);
CREATE TABLE shippers (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	shipperID INTEGER,
	companyName VARCHAR(256),
	phone VARCHAR(256)
	);
CREATE TABLE order_details (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	orderID INTEGER,
	productID INTEGER,
	unitPrice REAL,
	quantity INTEGER,
	discount REAL
	);
CREATE TABLE employees (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	employeeID INTEGER,
	lastName VARCHAR(256),
	firstName VARCHAR(256),
	title VARCHAR(256),
	titleOfCourtesy VARCHAR(256),
	birthDate TIMESTAMP,
	hireDate TIMESTAMP,
	address VARCHAR(256),
	city VARCHAR(256),
	region VARCHAR(256),
	postalCode VARCHAR(256),
	country VARCHAR(256),
	homePhone VARCHAR(256),
	extension VARCHAR(256),
	photo BYTEA,
	notes TEXT,
	reportsTo REAL,
	photoPath TEXT
	);
CREATE TABLE suppliers (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	supplierID INTEGER,
	companyName VARCHAR(256),
	contactName VARCHAR(256),
	contactTitle VARCHAR(256),
	address VARCHAR(256),
	city VARCHAR(256),
	region VARCHAR(256),
	postalCode VARCHAR(256),
	country VARCHAR(256),
	phone VARCHAR(256),
	fax VARCHAR(256),
	homePage VARCHAR(256)
	);
CREATE TABLE orders (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	orderID INTEGER,
	customerID VARCHAR(256),
	employeeID INTEGER,
	orderDate TIMESTAMP,
	requiredDate TIMESTAMP,
	shippedDate TIMESTAMP,
	shipVia INTEGER,
	freight REAL,
	shipName VARCHAR(256),
	shipAddress VARCHAR(256),
	shipCity VARCHAR(256),
	shipRegion VARCHAR(256),
	shipPostalCode VARCHAR(256),
	shipCountry VARCHAR(256)
	);
CREATE TABLE employee_territories (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	employeeID INTEGER,
	territoryID INTEGER
	);
CREATE TABLE categories (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	categoryID INTEGER,
	categoryName VARCHAR(256),
	description TEXT,
	picture BYTEA
	);
CREATE TABLE regions (
	id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	regionID INTEGER,
	regionDescription VARCHAR(256)
	);
