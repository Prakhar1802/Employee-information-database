"""
Project Name: Employee  Information System
Project Description: In this Project, I am going to use the Mysql and Python for handling a database, and also we put some
features like adding data, updating data, seeing all records and seeing specific record.
Project Developer: Prakhar Tripathi
Project Version: 0.1

"""
# import all modules related to the given project
from Add_data import add_one_record, add_many_record
from Delete_data import delete_record
from Update_data import update_record
from Find_data import find_record


def main():
    print("======================================================")
    print("\t\t\tEmployee Information System")
    print("======================================================\n")
    while True:
        print("-----------------------------")
        print(
            "Press 1 to insert the record\nPress 2 to update the record\nPress 3 to Delete the record\n"
            "Press 4 to find the record")
        print("-----------------------------\n")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            print("Press 1 to insert one record\nPress 2 to to insert multiple record")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                add_one_record()
            elif choice == 2:
                add_many_record()
        elif choice == 2:
            print("You are able to update id, name, address, phone, salary of Employee")
            update_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            find_record()
        choice = input("\nDo you want to continue(yes/no):")
        if choice == "no":
            print("Ok, Bye!!")
            exit()


main()
