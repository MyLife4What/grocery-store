# Grocery Store  
Grocery store database contains an information of the product in a store and customer that bought a product.  
This is an example of the tables.
#### Product Table
| ID | Product | Price | Quantity |
|:--:|:-------:|:-----:|:--------:|
|  1 |   Fish  |  129  |    10    |
#### Customer Table
| ID | Name | Gender | Member Rank | Product ID(This is what customer bought) |
|:--:|:----:|:------:|:-----------:|:----------------------------------------:|
|  1 | Fish |   129  |     Gold    |                   20                     |

# Installation Instructions  
This is how i created a database.
### 1. Create a grocery_store.schema for create a database.
```
CREATE TABLE IF NOT EXISTS products (
    product_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    product       TEXT    DEFAULT '',
    price         INTEGER DEFAULT 0,
    quantity      INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS customers (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT    NOT NULL,
    gender         TEXT    NOT NULL,
    member_rank    TEXT    NOT NULL,
    product_id     INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);
```
### 2. Use a schema to create a grocery_store.db.
```python
sqlite3 grocery_store.db < grocery_store.schema
```
### 3. Open database file with sql command line.
```python
sqlite3 grocery_store.db
```
### 4. Import the data from csv files to the database.
```python
sqlite> .mode csv
sqlite> .import data/products.csv products
sqlite> .import data/customers.csv customers
```
