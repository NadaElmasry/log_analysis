# Logs Project

### Description:
The aim of this project is to create a reporting tool that answers three questions from the news database:

1. What are the most popular three articles of all time?
2. What are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The reporting tool used is a `python 3` prgoram that uses  `psycopg2` database system to connect to the database.

### Requirements:
To be able to run this program the following should be downloaded on your machine:

1. [python 3.5](https://www.python.org/downloads/)

2. [Vagrant](https://www.vagrantup.com/)

3. VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
To bring the virtual machine online use `vagrant up` and to login use `vagrant ssh`.

4. The data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be placed inside the Vagrant folder.

### How to run the program:
1. Bring the virtual machine online using `vagrant up`.

2. Login using `vagrant ssh`.

3. Load the database using `psql -d news -f newsdata.sql`.

4. Connect to the database using `psql -d news`.

5. Create the views for questions 3.

6. Exit using psql by pressing `\q`.

7. Execute the python program using `python3 logs_analysis.py`.


### Views for question 3:
1.

```sql
CREATE VIEW right_entries AS 
SELECT to_char(time , 'DD-MON-YYYY') AS rightdate, count(*) AS rightentries 
FROM log 
WHERE status = '200 OK'
GROUP BY rightdate;

``` 
2.

```sql
CREATE VIEW errors_entries AS 
SELECT to_char(time , 'DD-MON-YYYY') AS errordate, count(*) AS errorentries 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY errordate;

```