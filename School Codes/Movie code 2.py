import pickle


def WriteData():
    with open("Y:\\CS\School Codes\Movie.dat", "wb") as F:
        R = []
        while True:
            Mno = int(input("Movie ID:"))
            Name = input("Movie Name:")
            R.append([Mno, Name])
            C = input("More(Y/N)?")
            if C in "Nn":
                break
        pickle.dump(R, F)


def Update():
    try:
        with open("Y:\\CS\School Codes\Movie.dat", "rb+") as F:
            R = pickle.load(F)
            for L in R:
                print(L)
                C = input("Modify(Y/N)?")
                if C in "Yy":
                    L[1] = input("Changed Name:")
            F.seek(0)
            pickle.dump(R, F)
    except:
        print("File not found")


while True:
    print("W:Write Data")
    print("U:Update")
    ch = input("Enter choice:")
    if ch == "W":
        WriteData()
    elif ch == "U":
        Update()
    else:
        break
