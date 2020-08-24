dict_to_sort = {"Петя": 23, "Вася": 40, "Лена": 14, "Катя": 22}
sorted_dict = sorted(dict_to_sort.items(), key=lambda dict: dict[1])
string = ''
for i in sorted_dict:
  string += str(list(i))
string = string.replace('[', '')
string = string.replace('\'', '')
string = string.replace(', ', ' : ')
string = string.replace(']', ' ')
print(string)
