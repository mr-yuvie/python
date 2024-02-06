import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost", user="root", password="yuv2323", database="project"
)
mycur = mydb.cursor()


def Add():
    try:
        a = input("Enter Name:")
        b = input("Enter Class:")
        c = input("Enter House:")
        mycur.execute("Insert into student values(%s,%s,%s)", (a, b, c))
        mydb.commit()
        print("Records Added")
    except:
        print("Unable to add Data")


def Dis():
    try:
        mycur.execute("Select * from Student")
        result = mycur.fetchall()
        for x in result:
            print(x)
    except:
        print("Unable to fetch Data")


while True:
    print("1.Add Record")
    print("2.Display Table")
    print("3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        Add()
    elif ch == 2:
        Dis()
    elif ch == 3:
        print("Exiting")
        exit()
