import math

n = int(input("Enter any number:"))
t = n
m = n
i = 0
s = 0
while t >= 1:
    t = t // 10
    i = i + 1
while m >= 1:
    j = m % 10
    m = m // 10
    k = math.pow(j, i)
    s = s + k
if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")
