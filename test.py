#names = ["Vidya", "Vinayak Naik"]

#for name in names:
 #   print(name)

names = ["Vidya", "Vinayak Naik"]

count = 0

for name in names:
    count += name.lower().count("a")

print("Alphabet 'a' repeated:", count)

