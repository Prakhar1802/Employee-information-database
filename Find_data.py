# Importing module for the connection with Mysql
from mysql.connector import connect

Mysql_conn = connect(
    host="localhost",  # store about the location of the database
    user="root",  # store the user's name or id
    password="Jarvis#1802",  # store the passcode of the user for connection
    database="Employees"  # using database for creating table in it.
)


def find_record():
    Mysql_conn.reconnect()
    cursor = Mysql_conn.cursor()  # It is used for executing the query in Python
    print("\n---------------------------------")
    print("Press 1 to find specific data\nPress 2 to find all data\nPress 3 to find n data from starting")
    print("---------------------------------\n")
    find_choice = int(input("Enter the choice:"))
    if find_choice == 1:
        print("You are able to select the data related to given id")
        choice = input("Enter the id of the employee:")
        cursor.execute("SELECT eid FROM employee_info")
        List = []
        Result = cursor.fetchall()
        for x in str(Result):
            List.append(x)
        if choice in List:
            query = "SELECT * FROM employee_info where eid = %s"
            val = (choice,)
            cursor.execute(query, val)
            rs = cursor.fetchall()
            print("=================================================================")
            print("eid      ename       eaddress        ephone           esalary")
            print("=================================================================")
            for i in rs:
                print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])
        elif choice not in List:
            print("Given id is not present in database.")
        print("Table selection successfully...")

    elif find_choice == 2:
        print("You are able to select all the data from table")
        query = "SELECT * FROM employee_info"
        cursor.execute(query)
        rs = cursor.fetchall()
        print("=================================================================")
        print("eid      ename       eaddress        ephone           esalary")
        print("=================================================================")
        for i in rs:
            print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])
        print("Table selection successfully...")

    elif find_choice == 3:
        print("You are able to select custom number of data from starting of table")
        query = f"SELECT * FROM employee_info"
        cursor.execute(query)
        n = int(input("Enter the number of record you want to see:"))
        rs = cursor.fetchmany(n)
        print("=================================================================")
        print("eid      ename       eaddress        ephone           esalary")
        print("=================================================================")
        for i in rs:
            print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])
        try:
            cursor.close()  # Use for close the cursor
        except Exception as e:
            print("Cursor have more data and not able to close right now...")
        print("Table selection successfully...")

    try:
        cursor.close()  # Use for close the cursor
    except Exception as e:
        print("Cursor have more data and not able to close right now...")
    Mysql_conn.close()  # Connection close


# find_record()