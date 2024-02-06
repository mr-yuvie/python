import pickle


def WriteData():
    with open("Y:\\CS\School Codes\Movie.dat", "wb") as F:
        while True:
            Mno = int(input("Movie ID:"))
            Name = input("Movie Name:")
            pickle.dump([Mno, Name], F)
            C = input("More(Y/N)?")
            if C in "Nn":
                break


def ReadData():
    with open("Y:\\CS\School Codes\Movie.dat", "rb") as F:
        while True:
            try:
                R = pickle.load(F)
                print(R)
            except:
                break


while True:
    print("W:Write Data")
    print("R:Read Data")
    ch = input("Enter choice:")
    if ch == "W":
        WriteData()
    elif ch == "R":
        ReadData()
    else:
        break
