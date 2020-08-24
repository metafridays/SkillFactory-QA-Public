from random import randint

def insertion_descend_sort(A):
    counter = 0
    print(A)
    for i in range(len(A)):
        b = A[i]
        j = i-1
        while (j >= 0) and (b > A[j]):
            A[j+1] = A[j]
            j -= 1
            counter += 1
        A[j+1] = b
        counter += 1
    return A, counter

def descend_bubble(A):
    counter = 0
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
         if A[j] < A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            counter += 1
    return A, counter

N = 10
a = []
b = []
for i in range(N):
    tmp = randint(1, 99)
    a.append(tmp)
    b.append(tmp)
    
print(insertion_descend_sort(a))
print(descend_bubble(b))