def while_bubblesort(A):
    i = 0
    while i < len(A)-1:
        j = 0
        while j < len(A)-i-1:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            j += 1
        i += 1
    return A

a = [93, 12, 67, 77, 12, 81, 88, 58, 72, 55]
while_bubblesort(a)
myString = ', '.join(map(str, a))
print(myString)