a = [['Егор', 15, 165, 44], ['Лена', 20, 160, 45], ['Витя', 32, 180, 77], ['Полина', 28, 175, 65]]

a_sort = sorted(a, key=lambda x: x[1])
print(', '.join(str(i) for i in a_sort))
