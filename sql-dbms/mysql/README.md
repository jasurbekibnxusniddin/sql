![alt text](images/image.png)

# What is MySQL

MySQL? What’s in a name?

MySQL got its name from the daughter of one of its co-founders, Monty Widenius, whose name is My. Combining ‘My’ with ‘SQL,’ we get MySQL.

MySQL is a robust database management system designed for managing relational databases. It is open-source software supported by Oracle, meaning that you can use MySQL without any cost. Additionally, you will have the flexibility to modify its source code to tailor it to your specific requirements.

Despite being open-source software, you also have the option to purchase a commercial license from Oracle, which provides access to premium support services.

When compared to other database software like Oracle Database or Microsoft SQL Server, MySQL is relatively easy to master.

MySQL is versatile and can run on various platforms, including UNIX, Linux, and Windows. You can install it on a server or even on a desktop. What’s more, MySQL is renowned for its reliability, scalability, and speed.

>The official way to pronounce MySQL is My Ess Que Ell, not My Sequel. Nevertheless, you can pronounce it as you prefer; it’s a matter of personal choice.

If you’re a web developer, MySQL is a great choice. It’s a key component of the LAMP stack, which consists of Linux, Apache, MySQL, and PHP.

# install MySQL

## Install MySQL on Ubuntu
> Before you begin, ensure you have root or sudo privileges on your Ubuntu system.

### Step 1. Update APT Package List
Update the APT package list to ensure that you have the latest information about available packages:

```sh
sudo apt update
```
### Step 2. Install MySQL Server
To install MySQL, use the `apt` package manager. You can install MySQL using the `apt` package manager by running the following command:

```sh
sudo apt install mysql-server
```

### Step 3. Enable MySQL service to auto-start on reboot
```sh
sudo systemctl enable mysql.service
```

### Step 4. Start MySQL Service
```sh
sudo systemctl start mysql.service
```
### Step 5. Check the status of MySQL Service
```sh
systemctl status mysql.service
```

> Note that you can press q to exit the message.

### Step 6. Log in to MySQL and change the root’s password
First, log in to the MySQL server using the following command:

```sh
sudo mysql
```

It’ll take you to the mysql command line:

Second, change the password of the root’s account:

```sql
ALTER USER root@localhost 
IDENTIFIED WITH mysql_native_password  
BY '<YOUR_PASSWORD>';
```

You should store the password in a secure place for logging in to the MySQL server later.

Third, exit the MySQL database server:

```sh
exit
```
Fourth, attempt to log in to the MySQL database server with the new password:
```sh
mysql -u root -p
```

It’ll prompt you to enter a password. Please use the password that you entered in the previous step:

> Enter password:

If you enter the password correctly, you’ll be logged in to the MySQL database server.

```sh
mysql>
```

Before going to the next step, exit the mysql client tool:

```sh
exit
```

### Step 7. Secure the MySQL installation
Execute the following command to adjust the security of the MySQL Server:

```sh
sudo mysql_secure_installation
```
It’ll prompt you to enter the root’s password. After you enter the password correctly, you will be asked a series of questions. Press ‘Y’ or ‘N’ for the various security questions.



Once you have the MySQL Server installed, you can connect to it using any client program such as mysql command-line client and MySQL workbench.

# Connect to MySQL Server

## Connect to MySQL Using mysql command-line client

The mysql is a command-line client program that allows you to interact with MySQL in interactive and non-interactive modes.

To connect to the MySQL Server, you type this command on Command Prompt:

```sh
mysql -u root -p
```

In this command:

`-u root` means that you connect to the MySQL Server using the user root.

`-p` instructs mysql to prompt for a password.

You type the password for the root user and press Enter:
```
Enter password: ********
```
If everything is OK, you will connect to the MySQL Server and see the following command:

```sh
mysql>
```

To display available databases in the current server, you enter the `SHOW DATABASES` statement terminated by a semicolon (;) and press the Enter key:

```sql
show databases;
```

The mysql program will return the following output:

```txt
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
```

Here are the steps that occur behind the scenes:

- First, the mysql command-line client sends the query to the MySQL Server.
- Second, the MySQL server executes the query and sends the result back.
- Third, the mysql command-line client displays the result.



# Managing Databases
## Selecting a MySQL database using the mysql client tool
When you log in to a MySQL database server using the mysql client tool without specifying a database name, MySQL server will set the current database to NULL.

First, log in to MySQL using the root user account:

```sh
mysql -u root -p
```

MySQL will prompt you for a password:
> Enter password:

To log in, you need to provide the correct password of the root user account and press Enter. To display the current database, you use the following statement:

```sql
SELECT database();
```

It’ll return the following:

```txt
+------------+
| database() |
+------------+
| NULL       |
+------------+
1 row in set (0.00 sec)
```
It means the current database is not set. If you issue a statement, MySQL will issue an error.

For example:
```sql
SELECT * FROM t;
```
Code language: SQL (Structured Query Language) (sql)

Error:
```err
ERROR 1046 (3D000): No database selected
```

#### the `USE` statement
To select a database to work with, you use the `USE` statement:

```sql
USE database_name;
```

For example, the following statement uses the USE statement to set the current database to classicmodels:

```sql
USE classicmodels;
```

If you see the following message, it means that you have changed the database to classicmodels successfully:

```msg
Database changed
```

To verify it, you can use the select database() statement:

```sql
SELECT database();
```

It’ll return something like:

```txt
+---------------+
| database()    |
+---------------+
| classicmodels |
+---------------+
1 row in set (0.00 sec)
```

If the classicmodels database doesn’t exist, you’ll get the following error after executing the USE statement:

```err
ERROR 1049 (42000): Unknown database 'classicmodels'
```
#### the `SHOW` statement
In this case, you need to find which databases are available on your server by using the show databases statement:

```sql
SHOW DATABASES;
```

The output may look like the following:
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.02 sec)
```

### Selecting a database when you login
If you know which database you want to work with before you log in, you can use the -D flag. For example, the following command connects to the classicmodels database with the user account root:

```sh
mysql -u root -D classicmodels -p
```

In this command, we specify the database classicmodels after the -D flag.

After entering the password and logging in successfully, you can check the current database:

```sql
SELECT database();
```
Output:
```txt
+---------------+
| database()    |
+---------------+
| classicmodels |
+---------------+
1 row in set (0.00 sec)
```

## MySQL CREATE DATABASE
### Introduction to the MySQL `CREATE DATABASE` statement

To create a new database in MySQL, you use the CREATE DATABASE statement. The following illustrates the basic syntax of the `CREATE DATABASE` statement:

```sql
CREATE DATABASE [IF NOT EXISTS] database_name
[CHARACTER SET charset_name]
[COLLATE collation_name];
```

In this syntax:

- First, specify the name of the database after the CREATE DATABASE keywords. The database name must be unique within a MySQL server instance. If you attempt to create a database with an existing name, MySQL will issue an error.
- Second, use the IF NOT EXISTS option to create a database if it doesn’t exist conditionally.
- Third, specify the character set and collation for the new database. If you skip the CHARACTER SET and COLLATE clauses, MySQL will use the default character set and collation for the new database.

### Creating a new database using the mysql client tool
To create a new database via the mysql client tool, you follow these steps:

First, log in to the MySQL server using a user account that has the CREATE DATABASE privilege:

```sh
mysql -u root -p
```
It’ll prompt you to enter a password. To authenticate, you need to type the password for the root user account and press the Enter key:
> Enter password: ********

Next, display the databases available on the server using the SHOW DATABASES statement. This step is optional.

```sql
SHOW DATABASES;
```

Output:

```text
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```
Then, execute the CREATE DATABASE statement to create the testdb database and press Enter:

```sql
CREATE DATABASE testdb;
```

It’ll return the following:

```
Query OK, 1 row affected (0.02 sec)
```

After that, use the SHOW CREATE DATABASE command to review the created database:

```sql
SHOW CREATE DATABASE testdb;
```
MySQL returns the database name and the character set and collation of the database:

```txt
+----------+----------------------------------------------------------------------------------------------------------------------------------+
| Database | Create Database                                                                                                                  |
+----------+----------------------------------------------------------------------------------------------------------------------------------+
| testdb   | CREATE DATABASE `testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */ |
+----------+----------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.01 sec)
```

Finally, select the newly created database to work with by using the USE statement:

```sql
USE testdb;
```

Output:

```
Database changed
```

Now, you can start creating tables and other database objects within the  testdb database.

To quit the mysql program, type exit command:

```sh
exit
```

Output:

```sh
Bye
```
After creating a database, you can create a user account and grant privileges to the database.

## MySQL DROP DATABASE
### Introduction to the MySQL DROP DATABASE statement

The DROP DATABASE statement drops all tables in the database and deletes the database permanently. Therefore, you need to be very careful when using this statement.

The following shows the syntax of the DROP DATABASE statement:

```sql
DROP DATABASE [IF EXISTS] database_name;
```

In this statement, you specify the name of the database which you want to delete after the DROP DATABASE keywords.

If you drop a database that does not exist, MySQL will issue an error.

To prevent an error from occurring if you delete a non-existing database, you can use the IF EXISTS option. In this case, MySQL will terminate the statement without issuing any error.

The DROP DATABASE statement returns the number of tables it deleted.

In MySQL, the schema is the synonym for the database. Therefore, you can use them interchangeably:

```sql
DROP SCHEMA [IF EXISTS] database_name;
```

### MySQL DROP DATABASE using mysql program example

display all the databases using the SHOW DATABASES statement:
```sql
SHOW DATABASES;
```

Output:
```txt
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| testdb             |
| testdb2            |
+--------------------+
7 rows in set (0.00 sec)
```
and, drop the testdb database by issuing the DROP DATABASE statement:

```sql
DROP DATABASE testdb;
```

Output:

```
Query OK, 0 rows affected (0.03 sec)
```
MySQL returned zero affected rows indicating that the testdb database has no tables.

# Managing Tables

## MySQL CREATE TABLE
### Introduction to MySQL `CREATE TABLE` statement

The CREATE TABLE statement allows you to create a new table in a database.

The following illustrates the basic syntax of the CREATE TABLE  statement:

```sh
CREATE TABLE [IF NOT EXISTS] table_name(
   column1 datatype constraints,
   column2 datatype constraints,
   ...
) ENGINE=storage_engine;
```

In this syntax:

- table_name: This is the name of the table that you want to create.
- column1, column2, etc.: The names of the columns in the table.
- datatype: the data of each column such as INT, VARCHAR, DATE, etc.
- constraints: These are optional constraints such as NOT NULL, UNIQUE, PRIMARY KEY, and FOREIGN KEY.

If you create a table with a name that already exists in the database, you’ll get an error. To avoid the error, you can use the IF NOT EXISTS option.

In MySQL, each table has a storage engine such as InnoDB or MyISAM. The ENGINE clause allows you to specify the storage engine of the table.

If you don’t explicitly specify a storage engine, MySQL will use the default storage engine which is InnoDB.

> InnoDB became the default storage engine starting with MySQL version 5.5. The InnoDB storage engine offers several advantages of a relational database management system, including ACID transaction support, referential integrity, and crash recovery. In earlier versions, MySQL used MyISAM as the default storage engine.

### MySQL CREATE TABLE statement examples
Let’s take some examples of creating new tables.

#### 1) Basic CREATE TABLE statement example
The following example uses the CREATE TABLE statement to create a new table called tasks:

```sql
CREATE TABLE tasks (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE
);
```

The tasks table has four columns:

* The id is an INT column and serves as the primary key column.
* The title is a VARCHAR column and cannot be NULL.
* The start_date and end_date are the DATE column and can be NULL.

After that, execute the CREATE TABLE statement. list all tables in the test database:

```sql
SHOW TABLES;
```

Output:
```
+----------------+
| Tables_in_test |
+----------------+
| tasks          |
+----------------+
1 row in set (0.00 sec)
```

It shows the table tasks that we have created.

#### 2) Creating a table with a foreign key example

Suppose each task has a checklist. To store the checklists of tasks, you can create a new table called checklists as follows:

```sql
CREATE TABLE checklists(
  id INT, 
  task_id INT, 
  title VARCHAR(255) NOT NULL, 
  is_completed BOOLEAN NOT NULL DEFAULT FALSE, 
  PRIMARY KEY (id, task_id), 
  FOREIGN KEY (task_id) 
      REFERENCES tasks (id) 
      ON UPDATE RESTRICT 
      ON DELETE CASCADE
);
```

The table checklists has a primary key that consists of two columns. Therefore, we need to use a table constraint to define the primary key:
```sql
PRIMARY KEY (id, task_id)
```

In addition, the task_id is the foreign key column that references the id column of the tasks table, therefore, we use a foreign key constraint to establish this relationship:

```sql
FOREIGN KEY (task_id) 
    REFERENCES tasks (id) 
    ON UPDATE RESTRICT 
    ON DELETE CASCADE
```

## MySQL AUTO_INCREMENT
### Introduction to MySQL `AUTO_INCREMENT` attribute

In MySQL, you use the AUTO_INCREMENT attribute to automatically generate unique integer values for a column whenever you insert a new row into the table.

Typically, you use the AUTO_INCREMENT attribute for the primary key column to ensure each row has a unique identifier.



### Creating a table with MySQL AUTO_INCREMENT column

To create a table with an auto-increment column, you use the AUTO_INCREMENT attribute:

```sql
CREATE TABLE table_name(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ...
);
```

For example, the following statement creates a table called contacts to store contact data:

```sql
CREATE TABLE contacts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(320) NOT NULL
);
```

In this example, we assign the AUTO_INCREMENT attribute to the id column to set it as an auto-increment primary key.

This means that when you insert a new row into the contacts table without providing a value for the id column, MySQL will automatically generate a unique number.

