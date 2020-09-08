string = "Когда мне было 8 лет моему другу было 10 а его сестре 15"
string = string.split()
num = 0
for n in string:
    if n.isdigit():
        num += 1
print(num)
