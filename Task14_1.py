#Filename had been hardcoded for debug reason 
#filename = input()
filename = 'testfile.txt'
file = open(filename, 'r')
text = file.read()

#Delete digits and special characters, switch double space
#to single space and switch to lowercase
for i in '~`!@#$%^&*()-–=+_0987654321{}[]:;\'\"/\\,.<>':
    text = text.replace(i, '').replace('  ', ' ').lower()

list = text.split(' ')
#Initilaizing variable for number of most_common_word
counter = 0
most_common_word = ''

for i in list:
    if len(i) > 3 and counter < list.count(i):
        most_common_word = i
        counter = list.count(i)

#Delete russian letters
for i in 'абвгдеёжзийклмнопрстуфхцчшщыъьэюя':
    text = text.replace(i, '').replace('  ', '')

list = text.split(' ')
#Initilaizing variable for number of word_max_length
counter = 0
word_max_length = ''

#Check length of all words
for i in list:
    if len(i) > counter:
        counter = len(i)
        word_max_length = i

#Print results
print(most_common_word)
print(word_max_length)

#Close the file
file.close()