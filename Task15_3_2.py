def insertion_descend_sort(A):
    for i in range(len(A)):
        b = A[i]
        j = i-1
        while (j >= 0) and (b > A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b
    return A

a = [5, 7, 1, 8, 178, 34, 79, 33, 15]
insertion_descend_sort(a)
myString = ', '.join(map(str, a))
print(myString)