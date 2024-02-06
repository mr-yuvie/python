# Using sets to remove duplicate elements from a list.

n = int(input("Enter total number of elements:"))
L = []
for i in range(n):
    a = input("Enter:")
    L.append(a)
print(L)
a = set(L)
b = list(a)
print(b)

# Another way of converting the set to list.

"""
D = []
for i in a:
    D.append(i)
print(D)
"""
