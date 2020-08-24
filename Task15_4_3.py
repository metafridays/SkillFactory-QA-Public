list_to_sort = [25, 47, 13, 5, 77, 12]
list_to_sort.sort(key = lambda x: str(x)[0])
list_to_sort = [str(item) for item in list_to_sort]
print(", ".join(list_to_sort))
