A =[10,25,31]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] <A[j]:
            T = A[i]
            A[i] = A[j]
            A[j] = T
print(A)            