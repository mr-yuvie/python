def SearchLinebyWord():
    with open("Y:\\CS\School Codes\Search.txt", "r+") as F:
        L = F.readlines()
        M = input("First Word:")
        for ch in L:
            L = ch.split()
            if L[0] == M:
                print(ch, end="")


def SearchLinebyLetter():
    with open("Y:\\CS\School Codes\Search.txt", "r+") as F:
        L = F.readlines()
        M = input("First Letter:")
        for ch in L:
            if ch[0] == M:
                print(ch, end="")


while True:
    print("W:Search by Word")
    print("L:Search by Letter")
    choice = input("Enter Choice:")
    if choice == "W":
        SearchLinebyWord()
    elif choice == "L":
        SearchLinebyLetter()
    else:
        break
