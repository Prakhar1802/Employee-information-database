# Importing module for the connection with Mysql
from mysql.connector import connect

Mysql_conn = connect(
    host="localhost",  # store about the location of the database
    user="root",  # store the user's name or id
    password="Jarvis#1802",  # store the passcode of the user for connection
    database="Employees"  # using database for creating table in it.
)


def delete_record():
    Mysql_conn.reconnect()
    cursor = Mysql_conn.cursor()  # It is used for executing the query in Python
    print("\n---------------------------------")
    print("Press 1 to delete specific data\nPress 2 to delete all data")
    print("---------------------------------\n")
    del_choice = int(input("Enter the choice:"))
    if del_choice == 1:
        print("You are able to remove the data related to given id")
        choice = input("Enter the id of the employee:")
        List = []
        cursor.execute("SELECT eid FROM employee_info")
        Result = cursor.fetchall()
        for x in str(Result):
            List.append(x)
        if choice in List:
            query = f"DELETE FROM employee_info where eid = %s"
            val = (choice,)
            cursor.execute(query, val)
            Mysql_conn.commit()
        elif choice not in List:
            print("Given id is not present in database.")
    elif del_choice == 2:
        print("You are able to remove all the data from table")
        query = f"DELETE FROM employee_info"
        cursor.execute(query)
        Mysql_conn.commit()

    cursor.close()  # Use for close the cursor
    Mysql_conn.close()  # Connection close
    print("Deletion Successful...")
