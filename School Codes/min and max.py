A = []
n = int(input("Enter Total number of values:"))
for i in range(n):
    c = int(input("Enter number:"))
    A.append(c)
L = len(A)
print("Min of", A[: L // 2], "is", min(A[: L // 2]))
print("Max of", A[L // 2 :], "is", max(A[L // 2 :]))
