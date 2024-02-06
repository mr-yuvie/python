def Binary(num):
    if num >= 1:
        Binary(num // 2)
        print(num % 2, end='')
num = int(input("Enter:"))
Binary(num)