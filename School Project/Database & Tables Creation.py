#python -m pip install mysql-connector-python
import mysql.connector as mysql
password=input("Enter your MySQL password:")
def DataBaseCreation():
    # Objective: This Function will create a Database "Secret_Services" if not exists.
    try:
        mydb = mysql.connect(host="localhost", user="root", passwd=f"{password}")
        cursor = mydb.cursor()
        cursor.execute("create database if not exists Secret_Services")
        print("Created Database Successfully")
    except:
        print("Database can't be created")


def TablesCreation():
    # Objective: This Function will create the required tables if not exists.
    try:
        mydb = mysql.connect(host="localhost", user="root", passwd=f"{password}", database="Secret_Services")
        cursor = mydb.cursor()
        cursor.execute("create table if not exists Agents(Agent_ID int(5) primary key,Code_Name varchar(15) Unique,Agent_Name varchar(20),Division varchar(20),Date_of_Joining date,Cases_Solved int(3))")
        cursor.execute("create table if not exists Criminals(Criminal_ID int(5) primary key,Code_Name varchar(15) Unique,Criminal_Name varchar(20),City varchar(25),Country varchar(25))")
        cursor.execute("""create table if not exists Safe_Houses(Place_ID int(5) primary key,Code_Word varchar(15) Unique,Address varchar(40),City varchar(25),Country varchar(25),Operated_by varchar(15), 
foreign key (Operated_by) references Agents (Code_Name) on update cascade on delete cascade)""")
        cursor.execute("""create table if not exists Gadgets(Gadget_ID int(5) primary key,Gadget_type varchar(15),Quantity int(4),Stored_at int(5), 
foreign key (Stored_at) references Safe_Houses(Place_ID) on update cascade on delete cascade)""")
        cursor.execute("""create table if not exists Missions(Mission_id int(5) primary key,Mission_Name varchar(15) Unique,Assigned_to varchar(15),Against varchar(15),Starting_Date date,Completion_Date date, 
foreign key (Assigned_to) references Agents (Code_Name) on update cascade on delete cascade, foreign key (Against) references Criminals (Code_Name) on update cascade on delete cascade)""")
        print("Required Tables Created")
    except:
        print("Required Tables can't be created")

DataBaseCreation()
TablesCreation()