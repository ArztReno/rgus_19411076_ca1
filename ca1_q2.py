# date : 14/11/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question : 2a

# MySQL Connector module to work with MySQL
import mysql.connector

# Creating the Connection to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

# To create a database in MySQL, I use the "CREATE DATABASE" statement:
mycursor.execute("CREATE DATABASE mydatabase")

# a)
# To create a table in MySQL, I use the "CREATE TABLE" statement.
# Student Table (Primary Key)
mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, student_id VARCHAR(255), name VARCHAR(255), course VARCHAR(255), telephone INT(255))")

# Book table
# Student Table (Foreign Key)
mycursor.execute("CREATE TABLE book (id INT AUTO_INCREMENT FOREIGN KEY, isbn VARCHAR(255), title VARCHAR(255), authors VARCHAR(255), num_copies VARCHAR(255))")

# Loan Table
# Student Table (Foreign Key)
mycursor.execute("CREATE TABLE loan (id INT AUTO_INCREMENT FOREIGN KEY, date_borrowed VARCHAR(255), name VARCHAR(255), date_returned VARCHAR(255), charges VARCHAR(255))")

# b)
# Populating the student table with  5 students
sql = "INSERT INTO student (student_id, name, course, telephone) VALUES (%s, %s, %s, %s)"
val = [
  ('student01', 'name01', 'course01', '111-111-111'),
  ('student02', 'name01', 'course02', '222-222-222'),
  ('student03', 'name01', 'course03', '333-333-333'),
  ('student04', 'name01', 'course04', '444-444-444'),
  ('student05', 'name01', 'course05', '555-555-555')
]

# This required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(mycursor.rowcount, "Student records inserted.")

# Populating the book table with  10  books
sql = "INSERT INTO student (isbn, tilte, authors, num_copies) VALUES (%s, %s, %s, %s)"
val = [
  ('isbn01', 'title01', 'author01', '1copies'),
  ('isbn02', 'title02', 'author02', '2copies'),
  ('isbn03', 'title03', 'author03', '3copies'),
  ('isbn04', 'title04', 'author04', '4copies'),
  ('isbn05', 'title05', 'author05', '5copies'),
  ('isbn06', 'title06', 'author06', '6copies'),
  ('isbn07', 'title07', 'author07', '7copies'),
  ('isbn08', 'title08', 'author08', '8copies'),
  ('isbn09', 'title09', 'author09', '9copies'),
  ('isbn10', 'title10', 'author10', '10copies'),
]

mydb.commit()

print(mycursor.rowcount, "Book records inserted.")

# Populating the loan table with  3 students
sql = "INSERT INTO student (date_borrowed, name VARCHAR, date_returned, charges) VALUES (%s, %s, %s, %s)"
val = [
  ('01-01-01', 'name01', '04-04-04', '10EUR'),
  ('02-02-02', 'name02', '05-05-05', '20EUR'),
  ('03-03-03', 'name31', '06-06-06', '30EUR')
]

mydb.commit()

print(mycursor.rowcount, "Loan records inserted.")
