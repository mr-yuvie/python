import pickle


def AddData():
    try:
        with open("Y:\\CS\School Codes\Movie.dat", "rb+") as F:
            R = pickle.load(F)
            while True:
                Mno = int(input("Movie ID:"))
                Name = input("Movie Name:")
                R.append([Mno, Name])
                C = input("More(Y/N)?")
                if C in "Nn":
                    break
            F.seek(0)
            pickle.dump(R, F)
    except FileNotFoundError:
        print("File not found")


def Search():
    try:
        with open("Y:\\CS\School Codes\Movie.dat", "rb") as F:
            R = pickle.load(F)
            Mno = int(input("Movie ID to Search:"))
            for L in R:
                if L[0] == Mno:
                    print(L)
                    break
            else:
                print("Not Found")
    except FileNotFoundError:
        print("File not found")


while True:
    print("A:Add Data")
    print("S:Search")
    ch = input("Enter choice:")
    if ch == "A":
        AddData()
    elif ch == "S":
        Search()
    else:
        break
