# Important Commands

	SELECT - extracts data from a database
	UPDATE - updates data in a database
	DELETE - deletes data from a database
	INSERT INTO - inserts new data into a database
	CREATE DATABASE - creates a new database
	ALTER DATABASE - modifies a database
	CREATE TABLE - creates a new table
	ALTER TABLE - modifies a table
	DROP TABLE - deletes a table
	CREATE INDEX - creates an index (search key)
	DROP INDEX - deletes an index

# Other Command

	DISTINCT - selects all types of db but only one(no doubles)
	
	WHERE - specifies output by conditions
	'--> can be combined with AND, OR and NOT
	
	ORDER BY - orders columns by ASC or DESC
	
	INSERT - inserts new records in a table
	'--> Ex.: INSERT INTO Laptop (LaptopID, ProcessorType, GraphicCard, Price, Stock)
		  VALUES ('1022', 'AMD Ryzen 7', 'Nvidia GTX 3070', '1999$', '22');
	
	IS NULL - to search for NULL values in db
	IS NOT NULL - to search for NOT NULL values in db
	
	UPDATE - updates records of existing columns
	'--> Ex.: UPDATE Laptop SET Price = '499$' WHERE LaptopID = 1022;
	'--> if WHERE is omitted then all records in the table will be updated with value
	
	DELETE - deletes records from table
	'--> Ex.: DELETE FROM Laptop; # Deletes all records from Laptop table but attributes of table are still intact
	'--> Ex.: DELETE FROM Laptop WHERE LaptopID='1022'; # Deletes all records from table with value 1022 as ID
	
	Limiting output: 	
	MySQL Syntax: SELECT column FROM table WHERE condition LIMIT number;
	|SQL Server / MS Access Syntax: SELECT TOP number PERCENT column FROM table WHERE condition
	|'--> Ex.: SELECT TOP 50 PERCENT * FROM Laptop; # selects first 50% of Laptop tavle
	'---> Ex.: SELECT * FROM Laptop WHERE Price='499$' LIMIT 10;


# Some Functions:

	MIN/MAX output:
	SELECT MIN/MAX(column) FROM table WHERE condition;
	'--> Ex.: SELECT MIN(Price) FROM Laptop WHERE ProcessorType='Intel I5 5200U';
	'--> Ex.: SELECT MAX(Price) AS LargestPrice FROM Laptop;
	
	COUNT() - returns number of rows that maches a condition
	SELECT COUNT(column) FROM table WHERE condition;
	'--> Ex.: SELECT COUNT(LaptopID) FROM Laptop; # returns number of laptops in table Laptop

	AVG() - returns average value of numeric column
	SELECT AVG(column) FROM table WHERE condition;
	'--> Ex.: SELECT AVG(Price) FROM Laptop; # returns average price of laptops in table Laptop
	
	SUM() - returns total sum of a numeric column
	SELECT SUM(column) FROM table WHERE condition;
	'--> Ex.: SELECT SUM(Stock) FROM Laptop WHERE ProcessorType='AMD Ryzen 7'; # returns the number of Laptops available for processortype
	
	LIKE - is used to search for specific patterns in the WHERE clause
	SELECT column FROM table WHERE column (NOT) LIKE pattern;
	LIKE WILDCARDS:
	WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
        WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
	WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
    	WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
    	WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
    	WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
    	WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"
	
	IN - is used in a where clause to reduce multiple OR conditions
	SELECT column FROM table WHERE column (NOT) IN (value1, value2)
	SELCET column FROM table WHERE column IN (SELECT statement);
	SELECT Price FROM Laptop WHERE ProcessorType IN (AMD R7, INTEL I5)
	
	BETWEEN - is used in a where clause to select values within a given range
	SELECT column FROM table WHERE column (NOT) BETWEEN val1 AND val2;
	SELECT * FROM Laptop WHERE Price BETWEEN 500$ AND 1000$ ORDER BY ProcessorType;
	SELECT * FROM Laptop WHERE Price BETWEEN 100$ AND 200$ AND ProzessorType NOT IN (INTEL I7, INTEL I5);

	alias - is used to give table or column temporary name
	SELECT column AS alias_name FROM table;
	SELECT ProcessorType AS PT FROM Laptop;
	SELECT CustomerName, Address + ', ' + Postalcode + ', ' + City AS Address FROM Customers;
	MySQL Syntx: SELECT CustomerName, CONTACT(Address,', ',PostalCode,', ',City) AS Address FROM Customers;
	
	JOIN - is used to combine rows from two or more tables, based on related column between them
	INNER JOIN - returns records that have matching values in both tables
	LEFT JOIN - returns all records from left table and the matched records from the right table
	RIGHT JOIN - reverse LEFT JOIN
	FULL OUTER JOIN - returns all records when there is a match in either left or right table
	#Syntx
	SELECT column FROM table INNER JOIN table2 ON table.column = table2.column;
	SELECT column FROM table LEFT JOIN table2 ON table.column = table2.column;
	SELECT column FROM table FULL JOIN table2 ON table.column = table2.column; # FULL JOIN and FULL OUTER JOIN are the same
	# Self Join - regular join but table joines itself
	SELECT column table1 T1, table1 T2 WHERE condition # T1 and T2 are aliases for the same table
	SELECT A.CustomerName AS CN1, B.CustomerName AS CN2, A.City FROM Customers A, Customers B WHERE A.CustomerID <> B.CustomerID AND A.City = B.City;
	'--> Matches Customers that are from the same city
	
	UNION - is used to combine the result-set of two or more SELECT statements
	SELECT column FROM table UNION SELECT column FROM table2;
	# UNION selects only distinct values by default --> to allow duplicate values use UNION ALL
	
	GROUP BY - groups rows that have the same values into summary rows, like 'find the number of customer each country'
	SELECT column FROM table GROUP BY column
	SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country ORDER BY COUNT(CustomerID) DESC; # lists number of customers in each country, sorted high to low 
	
	HAVING - was added to SQL because WHERE cannot be used with aggregate function(COUNT; MIN; MAX);
	SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) > 5; # lists number of customers in each country where country have more than 5 customers 
	
	EXISTS - is used to test for the existence of any record in a subquery # returns TRUE if one or more records are found
	SELECT column FROM table WHERE EXISTS(SELECT column FROM table WHERE condition);
	SELECT SupplierName FROM Suppliers WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20); # returns TRUE and lists suppliers with product price less than 20
	
	ANY - means that the condition will be true if the oparation is true for any of the values in the range
	SELECT column FROM table WHERE column operator ANY (SELECT column FROM table WHERE condition);
	SELECT ProductName FROM Products WHERE ProductID = ANY(SELECT ProductID FROM OrderDetails WHERE Quantity = 10);
	'--> lists the ProductName if it finds ANY records in the OorderDetails table has Quantity equal to 10

	ALL - means that the condition will be true only if the oparation is true for all values in the range
	SELECT ALL column FROM table WHERE condition
	SELECT column FROM table WHERE column operator ALL (SELECT column FROM table WHERE condition)
	SELECT ProductName FROM Products WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);
	'--> lists the ProductName if ALL the records in the OrderDetails table has Quantity equal to 10 

	SELECT INTO - copies data from one table into a new table
	SELECT * INTO newtable [IN externaldb] FROM oldtable WHERE condition;
	SELECT * INTO CustomerBackup IN 'Backup.mdb' FROM Customers;
	
	INSERT INTO SELECT - copies data from one table and inserts it into another
	INSERT INTO table2 SELECT * FROM table1 WHERE condition;
	INSERT INTO Customers (CustomerName, City, Country) SELECT SupplierName, City, Country FROM Suppliers;
	
	CASE - goes through conditions and returns value if condition is true --> if nothin is true, else will be executed
	CASE
	    WHEN condition1 THEN result1
	    WHEN condition2 THEN result2
	    ELSE reuslt
	END;
	SELECT OrderID, Quantity, 
	CASE
	    WHEN Quantity > 30 THEN 'The quantity is geater than 30'
	    WHEN Quantity = 30 THEN 'The quantity is 30'
	    ELSE 'The Quantity is under 30'
	END AS QuantityText
	FROM OrderDetails;
	
	IFNULL()/COALESCE()/NVL()/ISNULL() - lets you return an alternative value if an expression is NULL
	SELECT ProductName, UnitPrice * (UnitInStock + IFNULL (unitsOnOrder, 0)) FROM Products;
	
	PROCEDURES - like functions in other languages 
	CREATE PROCEDURE name AS sql_statement GO;
	# executing
	EXEC name
	CREATE PROCEDURE SelectALLCustomers AS SELECT * FROM Customers GO;
	EXEC SelectAllCustomers
	
	Comments 
	--SingleLineComment
	/*MultilineComment*/	
	
	
# SQL Database
	
	# Database handling
	CREATE DATABASE name; - creates a database
	
	DROP DATABASE name; - drops an existing database
	
	BACKUP DATABASE name TO DISK = 'filepath'; - backups db
	BACKUP DATABASE name TO DISK = 'filepath' WITH DIFFERENTIAL; - backups the parts of db that have changed since last full db update
	
	# Table handling
	CREATE TABLE table (column1 datatype; column2 datatype; ...);
	CREATE TABLE Persons(PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255), City varchar(255));
	CREATE TABLE new-table-name AS SELECT column1, column2 FROM existing-table-name; - copies from other table
	
	TRUNCATE TABLE name - deletes all data inside table and not table itself;

	ALTER TABLE - used to add, delete or modify columns in existing tables 
	ALTER TABLE table ADD column datatype;
	ALTER TABLE Customers ADD Email varchar(255); - adds eimail-column to customers
	ALTER TABLE Customers DROP COLUMN Email; - drops column Email
	ALTER TABLE table MODIFY COLUMN column_name datatype; - modifies existing column
	
	
	# constraints - used to specify rules for data in a table 
	CREATE TABLE name (column1 datatype constrait, column2 datatype constraint, ...)
	constraints types:
	
	NOT NULL - enforces a column to NOT accept NULL values (by default a column can hold null values)
	ALTER TABLE Persons MODIFY Age int NOT NULL; 
	CREATE TABLE Perosns(ID int NOT NULL);
	
	UNIQUE - ensures that all values in a column are different
	SQL Server syntx: CREATE TABLE Persons(ID int NOT NULL UNIQUE, LastName varchar(255) NOT NULL);
	MySQL Syntx: CREATE TABLE Persons(ID int NOT NULL, LastName varchar(255) NOT NULL, UNIQUE(ID));
	Multiple Unique Constraint columns: CREATE TABLE Persons(ID int NOT NULL, LastName varchar(255), CONSTRAINT UC_PERSON UNIQUE (ID,LastName)
	ALTER TABLE Persons ADD UNIQUE(ID);
	ALTER TABLE persons ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);
	MySQL Syntx: ALTER TABLE Persons DROP INDEX UC_Person;
	SQL Server: ALTER TABLE Persons DROP CONSTRAINT UC_Person;
	
	PRIMARY KEY - uniquely identifies each record in table; must contain UNIQUE values and not NULL values; only one pk in a table
	MYSQL Syntx: CREATE TABLE Persons (ID int NOT NULL, Age int, PRIMARY KEY (ID));
	SQL Server: CREATE TABLE Perosns (ID int NOT NULL PRIMARY KEY, Age int);
	PK on multiple columns:CREATE TABLE Persons(ID int NOT NULL, LastName varchar(255) NOT NULL, CONSTRAIT PK_Person PRIMARY KEY (ID,LastName));
	'--> PK_Person is the ONLY primary key. The value of pk is made up of two columns
	ALTER TABLE Persons ADD PRIMARY KEY (ID);
	ALTER TABLE Persons ADD CONSTRAINT UC_Person PRIMARY KEY (ID,LastName)
	MYSQL Syntx: ALTER TABLE Persons DROP PRIMARY KEY;
	SQL Server Syntx: ALTER TABLE Persons DROP CONSTRAINT UC_Person; 

	FOREIGN KEY - used to prevent avtions that would destroy links between tables; refers to the PK in another table
	--> Table with FK = child table; table with referenced PK = parent table
	--> The FOREIGN KEY constraint prevents invalid data from being inserted into the foreign key column, because it has to be one of the values contained in the parent table
	MYSQL: CREATE TABLE Orders(OrderID int NOT NULL, PesonID int, PRIMARY KEY(OrderID), FOREIGN KEY(PersonID) REFERENCES Person(PersonID));
	SQL Server: CREATE TABLE Orders(OrderID int NOT NULL PRIMARY KEY, PersonID int FOREIGN KEY REFERENCES Persons(PersonID));
	FK CONSTRAINT: CREATE TABLE Orders(OrderID int NOT NULL, PersonID int, PRIMARY KEY (OrderID), CONSTRAINT FK_PersonOrder FOREIN KEY (PersonID) REFERENCES Person(PersonID));
	ALTER TABLE Orders ADD FOREIGN KEY (PersonID) REFERENCES Person(PersonID);
	ALTER TABLE Orders ADD CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID) REFERENCES Person(PersonID);
	MYSQL: ALTER TABLE Orders DROP FOREIGN KEY FK_PersonOrder;
	SQL Server: ALTER TABLE Orders DROP CONSTRAINT FK_PersonOrder;

	CHECK - used to limit the value range that can be placed in a column
	--> define a check constraint on a column it will allow only certain values for this column
	--> define a check constraint on a table it can limit the values in certain columns based on values in other columns in the row
	MySQL: CREATE TABLE Persons(ID int NOT NULL, Age int, CHECK(Age>=18)); - checks if age of Person is over 18
	SQL Server: CREATE TABLE Persons(ID int NOT NULL, Age int CHECK (Age>=18));
	CREATE TABLE Persons(ID int NOT NULL, Age int, City varchar(255), CONSTRAINT CHK_Person CHECK (Age>= AND City='Berlin')
	ALTER TABLE Persons ADD CHECK (Age>=18);
	ALTER TABLE Persons ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Berlin')
	MySQL: ALTER TABLE Persons DROP CHECK CHK_PersonAge;
	SQL Server: ALTER TABLE Persons DROP CONSTRAINT CHK_PersonAge;
	 
	DEFAULT - is used to set default value for a column
	CREATE TABLE Persons(ID int NOT NULL, Age int, City varchar(255) DEFAULT 'Berlin');
	CREATE TABLE Orders(ID int NOT NULL, OrderDate date DEFAULT GETDATE()); - can be used with functions like GETDATE()
	MySQL: ALTER TABLE Persons ALTER City SET DEFAULT 'Berlin';
	SQL Server: ALTER TABLE Persons ADD CONSTRAINT df_City DEFAULT 'Berlin' FOR City;
	MySQL: ALTER TABLE Persons ALTER City DROP DEFAULT;
	SQL Server: ALTER TABLE Persons ALTER COLUMN City DROP DEFAULT;
	
	CREATE INDEX - used to create indexes in tables 
	--> indexes are used to retrieve data from db more quickly
	CREATE INDEX idx_pname ON Persons (LastName, FirstName);
	SQL Server: DROP INDEX table_name.index_name
	MySQL: ALTER TABLE table_name DROP INDEX index_name
	
	AUTO_INCREMENT - used to generate unique number when a new record is inserted into a table 
	MySQL: CREATE TABLE Persons (PersonID int NOT NULL AUTO_INCREMENT, Age int, PRIMARY KEY (PersonID)); - Person ID is auto incremented and primary key
	ALTER TABLE Persons AUTO_INCREMENT=100; - starts incrementing at 100
	--> when adding new Person a PersonID has not to be specified because it will be added automatically
	SQL Server: CREATE TABLE Persons (PersonID int IDENTITY(1,1) PRIMARY KEY, Age int); IDENTITY performs auto increment starting at 1 and increments also 1
	
	DATE
	MySQL: DATE - format YYYY-MM-DD
	       DATETIME - format YYYY-MM-DD HH:MI:SS
	       TIMESTAMP - format YYYY-MM-DD HH:MI:SS
	       YEAR - format YYYY or YY
	SQL Server: DATE - format YYYY-MM-DD
		    DATETIME - format YYYY-MM-DD HH:MI:SS
		    SMALLDATETIME - format YYYY-MM-DD HH:MI:SS
		    TIMESTAMP - format: a unique number
	SELECT * FROM Orders WHERE OrderDate='2002-11-11'

	VIEW - is a virtual table based on the result-set of an SQL statement
	CREATE VIEW view_name AS SELECT column1, column2, ... FROM table_name;
	CREATE VIEW [Brazil Customers] AS SELECT CustomerName, ContactName FROM Customers WHERE Country = 'Brazil'
	'-> SELECT * FROM [Brazil Customers]
	Updating view:
	CREATE OR REPLACE VIEW view_name AS SELECT column1, column2 FROM table_name;
	DROP VIEW view_name;
	
	SQL datatypes: https://www.w3schools.com/sql/sql_datatypes.asp
	
