def sort_key(k):
    return k[0]


a = [['Егор', 15, 165, 44], ['Лена', 20, 160, 45], ['Витя', 32, 180, 77], ['Полина', 28, 175, 65]]

a_sort = sorted(a, key=sort_key)
print(a)
print(a_sort)
