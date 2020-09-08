string = "У меня есть несколько лучших друзей Катя Петя Ваня и Маша"
string = string.split()
names = [word for word in string if word.istitle() == True and string.index(word) != 0]
print(names)
