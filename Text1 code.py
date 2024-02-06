def SaveText():
    with open("Y:\\CS\School Codes\Text1.txt", "w+") as F:
        while True:
            L = input("Line:")
            F.write(L + "\n")
            M = input("More(Y/N):")
            if M in ["N", "n"]:
                break


def ReadText():
    with open("Y:\\CS\School Codes\Text1.txt", "r") as F:
        L = F.readlines()
        for i in L:
            print(i, end="")


while True:
    print("S:Save Text")
    print("R:Read Text")
    ch = input("Enter choice:")
    if ch == "S":
        SaveText()
    elif ch == "R":
        ReadText()
    else:
        break
