def vowelCount():
    with open("Y:\\CS\School Codes\Count.txt", "r") as F:
        l = F.read()
        c = 0
        for ch in l:
            if ch in "AEIOUaeiou":
                c += 1
        print("Total number of vowels:", c)


def LineCount():
    with open("Y:\\CS\School Codes\Count.txt", "r") as F:
        c = 0
        L = F.readlines()
        for ch in L:
            c += 1
        print("Total number of lines:", c)


def ConsonantCount():
    with open("Y:\\CS\School Codes\Count.txt", "r") as F:
        l = F.read()
        c = 0
        for ch in l:
            if ch in "BCDFGHJKLMNPQRSTXYZbcdfghjklmnpqrstvxyz":
                c += 1
        print("Total number of consonants:", c)


while True:
    print("V:Vowel Count")
    print("C:Consonant Count")
    print("L:Line Count")
    choice = input("Enter Choice:")
    if choice == "V":
        vowelCount()
    elif choice == "C":
        ConsonantCount()
    elif choice == "L":
        LineCount()
    else:
        break
