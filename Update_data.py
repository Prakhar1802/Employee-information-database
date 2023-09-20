# Importing module for the connection with Mysql
from mysql.connector import connect

Mysql_conn = connect(
    host="localhost",  # store about the location of the database
    user="root",  # store the user's name or id
    password="Jarvis#1802",  # store the passcode of the user for connection
    database="Employees"  # using database for creating table in it.
)


def update_record():
    while True:
        Mysql_conn.reconnect()
        choice = input("Enter the id of the employee:")
        cursor = Mysql_conn.cursor()  # It is used for executing the query in Python
        List = []
        cursor.execute("SELECT eid FROM employee_info")
        Result = cursor.fetchall()
        for x in str(Result):
            List.append(x)
        if choice in List:
            print("\n-----------------------------")
            print(
                "Press 1 to update id\nPress 2 to update name\nPress 3 to update address\n"
                "Press 4 to update phone\nPress 5 to update salary\nPress 6 to update all")
            print("-----------------------------\n")
            update_choice = int(input("Enter your choice:"))
            if update_choice == 1:
                id = input("Enter the id of the employee:")
                query = f"UPDATE employee_info SET eid = %s where eid = {choice}"
                values = (id,)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
            elif update_choice == 2:
                name = input("Enter the name of the employee:")
                query = f"UPDATE employee_info SET ename = %s where eid = {choice}"
                values = (name,)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
            elif update_choice == 3:
                address = input("Enter the address of the employee:")
                query = f"UPDATE employee_info SET eaddress = %s where eid = {choice}"
                values = (address,)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
            elif update_choice == 4:
                phone = input("Enter the phone of the employee:")
                query = f"UPDATE employee_info SET ephone = %s where eid = {choice}"
                values = (phone,)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
            elif update_choice == 5:
                salary = input("Enter the salary of the employee:")
                query = f"UPDATE employee_info SET esalary = %s where eid = {choice}"
                values = (salary,)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
            elif update_choice == 6:
                id = input("Enter the id of the employee:")
                name = input("Enter the name of the employee:")
                address = input("Enter the address of the employee:")
                phone = input("Enter the phone of the employee:")
                salary = input("Enter the salary of the employee:")
                query = f"UPDATE employee_info SET eid = %s, ename = %s, eaddress = %s, ephone = %s, esalary = %s where eid = {choice}"
                values = (id, name, address, phone, salary)
                cursor.execute(query, values)  # It executes the query
                Mysql_conn.commit()
                print("Updation Successful")
        elif choice not in List:
            print("Given id is not present in database.")
        choice = input("\nDo you want to update anything(yes/no):")
        if choice == "no":
            print("Ok, Bye!!")
            break



# update_record()