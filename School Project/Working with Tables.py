#To use right modules. Run the following command in windows terminal/command prompt.
#python -m pip install mysql-connector-python prettytable

import mysql.connector as mysql
from prettytable import PrettyTable,from_db_cursor

password=input("Enter your MySQL password:")

try:
    mydb = mysql.connect(host="localhost", user="root", passwd=f"{password}", database="Secret_Services")
    cursor = mydb.cursor()
    print("Connection Established Successfully.")
except:
    print("Failed to establish connection.")
    exit()

def Table_Agents():

    def Add():
        Agent_ID=int(input("Enter Agent ID:"))
        Code_Name=input("Enter Agent's Code Name:")
        Agent_Name=input("Enter Agent's Name:")
        Division=input("Enter Their Respected Division:")
        Date_of_Joining=input("Enter Date of Joining[yyyy-mm-dd]:")
        Cases_Solved=int(input("Enter Total Cases Solved:"))
        try:
            cursor.execute(f"Insert into Agents values({Agent_ID},'{Code_Name}','{Agent_Name}','{Division}','{Date_of_Joining}',{Cases_Solved})")
            mydb.commit()
            print("Data Added Successfully.")
        except:
            print("Failed to Add Data.")
    
    def Display():
        try:
            cursor.execute("Select * from Agents")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Unable to fetch Data.")

    def Update():
        Old_Agent_ID=int(input("Enter Current Agent ID:"))
        New_Agent_ID=int(input("Enter New Agent ID:"))
        Code_Name=input("Enter Agent's Code Name:")
        Agent_Name=input("Enter Agent's Name:")
        Division=input("Enter Their Respected Division:")
        Date_of_Joining=input("Enter Date of Joining[yyyy-mm-dd]:")
        Cases_Solved=int(input("Enter Total Cases Solved:"))
        try:
            cursor.execute(f"Update Agents set Agent_ID={New_Agent_ID}, Code_Name='{Code_Name}', Agent_Name='{Agent_Name}', Division='{Division}', Date_of_Joining='{Date_of_Joining}', Cases_Solved={Cases_Solved} where Agent_ID={Old_Agent_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except:
            print("Failed to Update Data.")

    def Search():
        Agent_ID=int(input("Enter Agent ID to Search:"))
        try:
            cursor.execute(f"Select * from Agents where Agent_ID={Agent_ID}")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Failed to Search Data.")
    
    def Delete():
        print("Proceed with caution.")
        Agent_ID=int(input("Enter Agent ID to Delete:"))
        try:
            cursor.execute(f"delete from Agents where Agent_ID={Agent_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except:
            print("Unable to Delete Data.")

    while True:
        print(' ----------------------------- ')
        print('|        A:Add                |')
        print('|        D:Display            |')
        print('|        U:Update             |')
        print('|        S:Search             |')
        print('|        X:Delete             |')
        print('|        E:Exit               |')
        print(' ----------------------------- ')
        print('                               ')
        choice=input('Enter the function to perform: ')
        print('                               ')
        if choice in "Aa":
            Add()
        elif choice in "Dd":
            Display()
        elif choice in "Uu":
            Update()
        elif choice in "Ss":
            Search()
        elif choice in "Xx":
            Delete()
        else:
            break

def Table_Criminals():

    def Add():
        Criminal_ID=int(input("Enter Criminal ID:"))
        Code_Name=input("Enter Criminal's Code Name:")
        Criminal_Name=input("Enter Criminal's Name:")
        City=input("Enter City:")
        Country=input("Enter Country:")
        try:
            cursor.execute(f"Insert into Criminals values({Criminal_ID},'{Code_Name}','{Criminal_Name}','{City}','{Country}')")
            mydb.commit()
            print("Data Added Successfully.")
        except:
            print("Failed to Add Data.")
    
    def Display():
        try:
            cursor.execute("Select * from Criminals")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Unable to fetch Data.")

    def Update():
        Old_Criminal_ID=int(input("Enter Current Criminal ID:"))
        New_Criminal_ID=int(input("Enter New Criminal ID:"))
        Code_Name=input("Enter Criminal's Code Name:")
        Criminal_Name=input("Enter Criminal's Name:")
        City=input("Enter City:")
        Country=input("Enter Country:")
        try:
            cursor.execute(f"Update Criminals set Criminal_ID={New_Criminal_ID}, Code_Name='{Code_Name}', Criminal_Name='{Criminal_Name}', City='{City}', Country='{Country}' where Criminal_ID={Old_Criminal_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except:
            print("Failed to Update Data.")

    def Search():
        Criminal_ID=int(input("Enter Criminal ID to Search:"))
        try:
            cursor.execute(f"Select * from Criminals where Criminal_ID={Criminal_ID}")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Failed to Search Data.")
    
    def Delete():
        print("Proceed with caution.")
        Criminal_ID=int(input("Enter Criminal ID to Delete:"))
        try:
            cursor.execute(f"delete from Criminals where Criminal_ID={Criminal_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except:
            print("Unable to Delete Data.")

    while True:
        print(' ----------------------------- ')
        print('|        A:Add                |')
        print('|        D:Display            |')
        print('|        U:Update             |')
        print('|        S:Search             |')
        print('|        X:Delete             |')
        print('|        E:Exit               |')
        print(' ----------------------------- ')
        print('                               ')
        choice=input('Enter the function to perform: ')
        print('                               ')
        if choice in "Aa":
            Add()
        elif choice in "Dd":
            Display()
        elif choice in "Uu":
            Update()
        elif choice in "Ss":
            Search()
        elif choice in "Xx":
            Delete()
        else:
            break

def Table_Safe_Houses():

    def Add():
        Place_ID=int(input("Enter Place ID:"))
        Code_Word=input("Enter Place's Code Word:")
        Address=input("Enter Address:")
        City=input("Enter City:")
        Country=input("Enter Country:")
        Operated_by=input("Enter Code Word of the Agent operating the place:")
        try:
            cursor.execute(f"Insert into Safe_Houses values({Place_ID},'{Code_Word}','{Address}','{City}','{Country}','{Operated_by}')")
            mydb.commit()
            print("Data Added Successfully.")
        except:
            print("Failed to Add Data.")
    
    def Display():
        try:
            cursor.execute("Select * from Safe_Houses")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Unable to fetch Data.")

    def Update():
        Old_Place_ID=int(input("Enter Current Place ID:"))
        New_Place_ID=int(input("Enter New Place ID:"))
        Code_Word=input("Enter Place's Code Word:")
        Address=input("Enter Address:")
        City=input("Enter City:")
        Country=input("Enter Country:")
        Operated_by=input("Enter Code Word of the Agent operating the place:")
        try:
            cursor.execute(f"Update Safe_Houses set Place_ID={New_Place_ID}, Code_Word='{Code_Word}', Address='{Address}', City='{City}', Country='{Country}', Operated_by='{Operated_by}' where Place_ID={Old_Place_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except:
            print("Failed to Update Data.")

    def Search():
        Place_ID=int(input("Enter Place ID to Search:"))
        try:
            cursor.execute(f"Select * from Safe_Houses where Place_ID={Place_ID}")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Failed to Search Data.")
    
    def Delete():
        print("Proceed with caution.")
        Place_ID=int(input("Enter Place ID to Delete:"))
        try:
            cursor.execute(f"delete from Safe_Houses where Place_ID={Place_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except:
            print("Unable to Delete Data.")

    while True:
        print(' ----------------------------- ')
        print('|        A:Add                |')
        print('|        D:Display            |')
        print('|        U:Update             |')
        print('|        S:Search             |')
        print('|        X:Delete             |')
        print('|        E:Exit               |')
        print(' ----------------------------- ')
        print('                               ')
        choice=input('Enter the function to perform: ')
        print('                               ')
        if choice in "Aa":
            Add()
        elif choice in "Dd":
            Display()
        elif choice in "Uu":
            Update()
        elif choice in "Ss":
            Search()
        elif choice in "Xx":
            Delete()
        else:
            break

def Table_Gadgets():

    def Add():
        Gadget_ID=int(input("Enter Gadget ID:"))
        Gadget_type=input("Enter Gadget Type:")
        Quantity=input("Enter Quantity:")
        Stored_at=input("Enter Safe House's ID:")
        try:
            cursor.execute(f"Insert into Gadgets values({Gadget_ID},'{Gadget_type}','{Quantity}','{Stored_at}')")
            mydb.commit()
            print("Data Added Successfully.")
        except:
            print("Failed to Add Data.")
    
    def Display():
        try:
            cursor.execute("Select * from Gadgets")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Unable to fetch Data.")

    def Update():
        Old_Gadget_ID=int(input("Enter Current Gadget ID:"))
        New_Gadget_ID=int(input("Enter New Gadget ID:"))
        Gadget_type=input("Enter Gadget Type:")
        Quantity=input("Enter Quantity:")
        Stored_at=input("Enter Safe House's ID:")
        try:
            cursor.execute(f"Update Gadgets set Gadget_ID={New_Gadget_ID}, Gadget_type='{Gadget_type}', Quantity='{Quantity}', Stored_at='{Stored_at}' where Gadget_ID={Old_Gadget_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except:
            print("Failed to Update Data.")

    def Search():
        Gadget_ID=int(input("Enter Gadget ID to Search:"))
        try:
            cursor.execute(f"Select * from Gadgets where Gadget_ID={Gadget_ID}")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Failed to Search Data.")
    
    def Delete():
        print("Proceed with caution.")
        Gadget_ID=int(input("Enter Gadget ID to Delete:"))
        try:
            cursor.execute(f"delete from Gadgets where Gadget_ID={Gadget_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except:
            print("Unable to Delete Data.")

    while True:
        print(' ----------------------------- ')
        print('|        A:Add                |')
        print('|        D:Display            |')
        print('|        U:Update             |')
        print('|        S:Search             |')
        print('|        X:Delete             |')
        print('|        E:Exit               |')
        print(' ----------------------------- ')
        print('                               ')
        choice=input('Enter the function to perform: ')
        print('                               ')
        if choice in "Aa":
            Add()
        elif choice in "Dd":
            Display()
        elif choice in "Uu":
            Update()
        elif choice in "Ss":
            Search()
        elif choice in "Xx":
            Delete()
        else:
            break

def Table_Missions():

    def Add():
        Mission_ID=int(input("Enter Mission ID:"))
        Mission_Name=input("Enter Mission's Name:")
        Assigned_to=input("Enter Code Name of the Agent the Mission is assigned to:")
        Against=input("Enter Code Name of the Criminal the Mission is against:")
        Starting_Date=input("Enter Starting Date[yyyy-mm-dd]:")
        Completion_Date="NULL"
        print("Completion Date is always NULL when a Mission is started.")
        try:
            cursor.execute(f"Insert into Missions values({Mission_ID},'{Mission_Name}','{Assigned_to}','{Against}','{Starting_Date}',{Completion_Date})")
            mydb.commit()
            print("Data Added Successfully.")
        except:
            print("Failed to Add Data.")

    def Display():
        try:
            cursor.execute("Select * from Missions")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Unable to fetch Data.")

    def Update():
        Old_Mission_ID=int(input("Enter Current Mission ID:"))
        New_Mission_ID=int(input("Enter New Mission ID:"))
        Mission_Name=input("Enter Mission's Name:")
        Assigned_to=input("Enter Code Name of the Agent the Mission is assigned to:")
        Against=input("Enter Code Name of the Criminal the Mission is against:")
        Starting_Date=input("Enter Starting Date[yyyy-mm-dd]:")
        Completion_Date=input("Enter Completion Date[yyyy-mm-dd]:")
        try:
            cursor.execute(f"Update Missions set Mission_ID={New_Mission_ID}, Mission_Name='{Mission_Name}', Assigned_to='{Assigned_to}', Against='{Against}', Starting_Date='{Starting_Date}', Completion_Date='{Completion_Date}' where Mission_ID={Old_Mission_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except:
            print("Failed to Update Data.")

    def Search():
        Mission_ID=int(input("Enter Mission ID to Search:"))
        try:
            cursor.execute(f"Select * from Missions where Mission_ID={Mission_ID}")
            results=from_db_cursor(cursor)
            print(results)
        except:
            print("Failed to Search Data.")
    
    def Delete():
        print("Proceed with caution.")
        Mission_ID=int(input("Enter Mission ID to Delete:"))
        try:
            cursor.execute(f"delete from Missions where Mission_ID={Mission_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except:
            print("Unable to Delete Data.")

    while True:
        print(' ----------------------------- ')
        print('|        A:Add                |')
        print('|        D:Display            |')
        print('|        U:Update             |')
        print('|        S:Search             |')
        print('|        X:Delete             |')
        print('|        E:Exit               |')
        print(' ----------------------------- ')
        print('                               ')
        choice=input('Enter the function to perform: ')
        print('                               ')
        if choice in "Aa":
            Add()
        elif choice in "Dd":
            Display()
        elif choice in "Uu":
            Update()
        elif choice in "Ss":
            Search()
        elif choice in "Xx":
            Delete()
        else:
            break

while True:
    print(' ----------------------------- ')
    print('|        A:Agents             |')
    print('|        C:Criminals          |')
    print('|        S:Safe_Houses        |')
    print('|        G:Gadgets            |')
    print('|        M:Missions           |')
    print('|        E:Exit               |')
    print(' ----------------------------- ')
    print('                               ')
    choice=input('Enter the table to work with: ')
    print('                               ')
    if choice in "Aa":
        Table_Agents()
    elif choice in "Cc":
        Table_Criminals()
    elif choice in "Ss":
        Table_Safe_Houses()
    elif choice in "Gg":
        Table_Gadgets()
    elif choice in "Mm":
        Table_Missions()
    else:
        break
