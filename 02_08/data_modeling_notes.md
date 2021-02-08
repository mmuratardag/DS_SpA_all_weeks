# Data Modeling

```python
a = 2 
#dynamic typing when declaring vars in Python
```

```c
int a;
a = 2; 
// static typing when declaring vars in C
```

SQL, just like C (and unlike Python), is an example of a "lower-level", statically typed language. This means that when we declare variables (i.e. create data), we need to be explicit about the data types.

Before we insert data into a PostGres database, we need to define the schema of the data, i.e. we need to create the table / template for the data to fit in. We use the `CREATE TABLE` command, followed by the name of the table, then in parentheses we specify the columns and their respective data types:

```sql
CREATE TABLE countries (
  capital VARCHAR(50),
  country_code CHAR(2),
  population INTEGER,
  birth_rate REAL,
  country_name VARCHAR(50)
);
```

There are TONS of different data types in PostGres, and they can get very oddly specific! Pick a suitable data type for your use case. On a high level, though, here are some of the categories:

Integer Types:

- `SMALLINT` -> 16bits (2 bytes)
  - 2^16 (-32, 678 <-> 32,767)
- `INTEGER` -> 32 bits

Floating Point Types:

- `REAL` -> up to 6 decimal places

Text Types:

- `CHAR(N)`
- `VARCHAR(N)`
- `TEXT`

Numeric:

- Datetimes
- Currencies
- lots of others...google "postgres data types"

Binary:

- images, etc.

---



## Inserting Data

```sql
INSERT INTO countries VALUES ('Berlin', 'DE', 80000000, 1.5, 'Germany');
```

```sql
INSERT INTO <tablename> (cols) VALUES (...,...); 
```

## Selecting Data

```sql
SELECT * FROM countries;
-- select all the data from all the columns (*) from the table
```

## Other Constraints:

Defining data types is an example of creating **constraints** in Data Modeling. There are other ways to create constraints, though. These include:

- `NOT NULL`, i.e. adding a null constraint so that data for the column CANNOT be missing:

```sql
CREATE TABLE countries (
capital VARCHAR(50) NOT NULL,
country_code CHAR(2),
population INTEGER,
birth_rate REAL,
country_name VARCHAR(50) 
);
```

- Duplicates
  - SERIAL is a data type that auto-increments (so you don't have to explicity insert it every time)
  - `PRIMARY KEY` is a useful constraint that makes the column unique
    - typically (and its GOOD PRACTICE TO DO SO) every table will always have a column called id and it will be a primary key.
    - A Primary key also creates an "index" for you behind the scenes, which is a mechanism that makes querying A LOT faster. A bit out of scope for now, though.
  - the `UNIQUE` argument is something you can also include for columns that are not primary keys but should also be unique, e.g. email addresses.

```sql
CREATE TABLE countries (
id SERIAL PRIMARY KEY, 
capital VARCHAR(50) NOT NULL,
country_code CHAR(2) UNIQUE,
population INTEGER NOT NULL,
birth_rate REAL,
country_name VARCHAR(50) NOT NULL
);
```

- `FOREIGN KEYS`
  - don't worry about Foreign Keys for now. This will be covered on Thursday.
  - For the Northwind data, you do not need to create foreign keys now. You can always add these constraints in later.

---

## Modifying Tables

If you want to modify data types or constraints (or add or remove columns) later on, there is the `ALTER TABLE` command.

Here's the documentation for PostGres: https://www.postgresql.org/docs/current/sql-altertable.html

But to be honest, I prefer to google the questions and end up on Stackoverflow (solves 99% of your PostGres issues). The PostGres documentation can be a bit dense. 