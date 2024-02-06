import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost", user="root", password="yuv2323", database="project"
)
mycur = mydb.cursor()


def Add():
    try:
        a = input("Enter Movie_ID:")
        b = input("Enter Movie_Name:")
        c = input("Enter Ticket_Price:")
        mycur.execute("Insert into movie values(%s,%s,%s)", (a, b, c))
        mydb.commit()
        print("Record Added")
    except:
        print("Unable to add Data")


def Search():
    try:
        a = input("Enter Movie_ID:")
        mycur.execute(f"Select * from Movie where Movie_ID='{a}'")
        print("Record Found")
        r = mycur.fetchall()
        print(r)
    except:
        print("Unable to Search Data")


while True:
    print("1.Add Record")
    print("2.Search Record")
    print("3.Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        Add()
    elif ch == 2:
        Search()
    elif ch == 3:
        print("Exiting")
        exit()
