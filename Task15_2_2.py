from random import randint

def descend_bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
         if A[j] < A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
    return A

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
a = [2, 7, 3, 8, 78, 34, 67, 33, 8]
print(a)
descend_bubble(a)
print(a)
print(a[0]+a[5])