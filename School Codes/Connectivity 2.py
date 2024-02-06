import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost", user="root", password="yuv2323", database="project"
)
mycur = mydb.cursor()


def Add():
    try:
        a = input("Enter Patient_ID:")
        b = input("Enter Name:")
        c = int(input("Enter Age:"))
        d = input("Enter Date & Time:")
        mycur.execute("Insert into appointment values(%s,%s,%s,%s)", (a, b, c, d))
        mydb.commit()
        print("Records Added")
    except:
        print("Unable to add Data")


def Update():
    try:
        a = input("Enter Patient_ID:")
        b = input("Enter new Patient_ID:")
        c = input("Enter Name:")
        d = int(input("Enter Age:"))
        e = input("Enter Date & Time:")
        mycur.execute(
            f"Update appointment set Patient_ID='{b}',Name='{c}',Age={d},Time='{e}' where Patient_ID='{a}'"
        )
        print("Record Updated")
        mydb.commit()

    except:
        print("Unable to Update Data")


def Dis():
    try:
        mycur.execute("Select * from appointment")
        result = mycur.fetchall()
        for x in result:
            print(x)
    except:
        print("Unable to fetch Data")


while True:
    print("1.Add Record")
    print("2.Update Table")
    print("3.Display Table")
    print("4.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        Add()
    elif ch == 2:
        Update()
    elif ch == 3:
        Dis()
    elif ch == 4:
        print("Exiting")
        exit()
