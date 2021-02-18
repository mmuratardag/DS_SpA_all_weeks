### Brief History of NoSQL Databases

1980s:

- SQL Relational Databases start dominating the Market 

1990s:

- Initial push for Object Databases. Why?
  - Object-Oriented Language like Python translate awkwardly to SQL Language (not a natural counterpart)
    - "Impedance Mismatch Problem"
  - In Relational Databases, data is across multiple tables, which sometimes means we need to disassemble and reassemble data from / to their aggregate forms. This means lots of joins, which can get tedious.
- SQL, however, continued to dominate. Relational DBs FTW!

2000s:

- Rise of Big (Internet) Data
  - Too much data -> difficult to partition / separate across multiple servers / clusters.
- Some big companies like Google and Amazon started making their own DBs that didn't follow the classic Relational / SQL schema.
- Other NoSQL databases start popping up: MongoDB, Redis, CouchDB
  - "cluster-friendly"
  - More suited to 21st century web data
  - mostly open-source
  - SCHEMA-LESS!!

Nowadays NoSQL databases are getting more popular. BUT SQL is still asked for more often in job ads. 

---

### MongoDB (2009) vs. PostGres (1996)

|                      | PostGres                                                     | MongoDB                                                      |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Server?              | Yes                                                          | Yes                                                          |
| Schema               | Organized into **Tables** (a collection of rows with standardized formats) | Organized into **Collections** (a collection of potentially unrelated JSON documents) |
| Data                 | Individual Unit is a **Row**                                 | Individual Unit is a **JSON Document**                       |
| Query Language       | SQL                                                          | MongoDB-specific language (looks like JavaScript / Python)   |
| Insert Query Example | ``INSERT INTO people (user_id, age, type) VALUES (1, 20, "A");`` | ``db.people.insertOne({user_id: 1, age: 20, type: "A"})``    |
| Filter Query Example | ``SELECT * FROM people WHERE age > 25;``                     | ``db.people.find({age: {$gt: 25}})``                         |
| GUI                  | PgAdmin, Postico, DBeaver                                    | Robo3t                                                       |
| Python Client        | SQLAlchemy                                                   | Pymongo                                                      |
| Cloud Option         | AWS RDS                                                      | Mongo Atlas                                                  |
| Documentation        | Old-School                                                   | Really nice modern documentation                             |
| CLI Client           | psql                                                         | mongo                                                        |


