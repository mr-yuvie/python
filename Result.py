import csv


def Accept():
    sid = int(input("Enter Student ID:"))
    sname = input("Enter Student Name:")
    Class = input("Enter Class:")
    res = input("Enter Result:")
    headings = ["Student ID", "Student Name", "Class", "Result"]
    data = [sid, sname, Class, res]
    f = open("Y:\\CS\School Codes\Result.csv", "a", newline="")
    csvwriter = csv.writer(f)
    csvwriter.writerow(headings)
    csvwriter.writerow(data)
    f.close()


def PassCount():
    f = open("Y:\\CS\School Codes\Result.csv", "r", newline="")
    csvreader = csv.reader(f)
    head = list(csvreader)
    for x in head:
        if x[3] == "PASS":
            print(x)
    f.close()


while True:
    print("A:Add Data")
    print("P:Display all Pass Students")
    ch = input("Enter choice:")
    if ch == "A":
        Accept()
    elif ch == "P":
        PassCount()
    else:
        break
