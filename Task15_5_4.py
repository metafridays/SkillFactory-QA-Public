string = "Сегодня была дождливая погода".replace(' ', '').lower()
if string == string[::-1]:
    print(True)
else:
    print(False)
