string = "info@value.com, value@info.com, com@value.info, q@value.com, q@vlue.c, 1asaf.asdf, qwe@wer@sdhjkfhs.dfsd"
emails = string.lower().split(', ')
dict = {}
for i in range(len(emails)):
  str = emails[i]
  if str.count('@') != 1:
    dict.update({str:False})
  elif str.index('@') < 2:
    dict.update({str:False})
  elif str.count('.') == 0 and (str.index('.') - str.index('@')) <= 2:
    dict.update({str:False})
  elif str[::-1].index('.') < 2:
    dict.update({str:False})
  else:
    dict.update({str:True})
print(dict.items())
