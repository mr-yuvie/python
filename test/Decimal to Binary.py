import math
def Binary(num):
    t = num
    c = 0
    while t >= 2:
        t = t / 2
        c += 1
    for i in range(c,-1,-1):
        if (num / (math.pow(2, i))) >= 1:
            print("1",end='')
        elif (num / (math.pow(2, i))) < 1:
            print("0",end='')
        num = num % (math.pow(2, i))
num = int(input("Enter decimal number:"))
Binary(num)