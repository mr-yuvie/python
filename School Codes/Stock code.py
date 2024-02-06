import csv


def Add():
    with open("Y:\\CS\School Codes\Stock.csv", "w", newline="") as cF:
        cW = csv.writer(cF)
        Lines = []
        while True:
            Ino = int(input("Ino:"))
            Item = input("Item:")
            Qty = int(input("Qty:"))
            Lines.append([Ino, Item, Qty])
            Q = input("More(Y/N)?")
            if Q == "N":
                break
        cW.writerows(Lines)


def Show():
    try:
        with open("Y:\\CS\School Codes\Stock.csv", "r", newline="") as cF:
            cR = csv.reader(cF)
            for L in cR:
                print(L)
    except FileNotFoundError:
        print("File not found")


while True:
    print("W:Write")
    print("R:Read")
    choice = input("Enter Choice:")
    if choice == "W":
        Add()
    elif choice == "R":
        Show()
    else:
        break
