string = "Добрый День!"
string1 = ""
for i in string:
    if not i.isupper():
        string1 = string1 + i
print(string1)
