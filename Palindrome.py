n = int(input("Enter any number:"))
rev = 0
t = n
while n >= 1:
    i = n % 10
    n = n // 10
    rev = rev * 10 + i
print("Reverse =", rev)
if rev == t:
    print("Palindrome")
else:
    print("Not Palindrome")
