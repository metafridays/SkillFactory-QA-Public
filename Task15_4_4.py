A = [2, 54, 38, 21, 10, 22, 45, 33]
A = sorted(A[:int(len(A)/2)]) + sorted(A[int(len(A)/2):])
A = [str(item) for item in A]
print(', '.join(A))
