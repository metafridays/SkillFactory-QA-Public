a = "In the hole in the ground there lived a hobbit"
a = a.replace(" ", "*")
a = a[0:a.find("*")] + " " + a[a.find("*")+1:a.rfind("*")] + " " + a[a.rfind("*")+1:len(a)]
print(a)
