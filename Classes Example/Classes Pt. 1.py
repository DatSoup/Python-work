ClassDictionary = {}
className = 0
while className != '':
    className = input("\nEnter a class: ")
    if className != '':
        credits = int(input("Enter the number of credits: "))
    else:
        break
    ClassDictionary[className.upper()] = credits
file = open("./local_data/" +input("Enter file name: "), 'w')
for key, value in ClassDictionary.items():
    file.write("%s\t%d\n" % (key, int(value)))
file.close()
print(ClassDictionary)