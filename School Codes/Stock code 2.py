import csv


def ReOrderItems():
    try:
        with open("Y:\\CS\School Codes\Stock.csv", "r", newline="") as cF:
            cR = csv.reader(cF)
            R = 0
            for L in cR:
                if int(L[2]) < 150:
                    print(L)
                    R += 1
                    print(R, " Items to be reordered.")
    except FileNotFoundError:
        print("File not found")


def Search():
    try:
        with open("Y:\\CS\School Codes\Stock.csv", "r", newline="") as cF:
            cR = csv.reader(cF)
            Ino = input("Ino to Search:")
            for L in cR:
                if Ino == L[0]:
                    print(L)
                    break
            else:
                print("Item ", Ino, " not found")
    except FileNotFoundError:
        print("File not found")


while True:
    print("R:Reorder")
    print("S:Search")
    choice = input("Enter Choice:")
    if choice == "S":
        Search()
    elif choice == "R":
        ReOrderItems()
    else:
        break
