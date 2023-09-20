# Importing module for the connection with Mysql
from mysql.connector import connect

Mysql_conn = connect(
    host="localhost",  # store about the location of the database
    user="root",  # store the user's name or id
    password="Jarvis#1802",  # store the passcode of the user for connection
    database="Employees"  # using database for creating table in it.
)


def add_one_record():
    Mysql_conn.reconnect()
    cursor = Mysql_conn.cursor()  # It is used for executing the query in Python

    query = "INSERT employee_info values(%s, %s, %s, %s, %s)"
    id = input("Enter the id of the employee:")
    name = input("Enter the name of the employee:")
    address = input("Enter the address of the employee:")
    phone = input("Enter the phone number of employee:")
    salary = input("Enter the salary of the employee:")

    values = (id, name, address, phone, salary)

    cursor.execute(query, values)  # It executes the query
    Mysql_conn.commit()  # It is use for committing the query or change that we do

    cursor.close()  # Use for close the cursor
    Mysql_conn.close()  # Connection close
    print("Insertion Successful...")


def add_many_record():
    list = []
    cursor = Mysql_conn.cursor()  # It is used for executing the query in Python
    query = "INSERT employee_info values(%s, %s, %s, %s, %s)"

    n = int(input("Enter the number of inputs you want:"))
    i = 1
    while i <= n:
        id = input("Enter the id of the employee:")
        name = input("Enter the name of the employee:")
        address = input("Enter the address of the employee:")
        phone = input("Enter the phone number of employee:")
        salary = input("Enter the salary of the employee:")
        print("----------------------------------------------\n")

        values = (id, name, address, phone, salary)
        list.append(values)
        i = i + 1

    cursor.executemany(query, list)  # It executes the query
    Mysql_conn.commit()  # It is use for committing the query or change that we do

    cursor.close()  # Use for close the cursor
    Mysql_conn.close()  # Connection close
    print("Insertion Successful...")

