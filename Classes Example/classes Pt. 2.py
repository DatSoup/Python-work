#Chris Campbell
#c.campbell.1@und.edu
#Program 10 part 2

def readClasses (fileName):
    ClassDict = {}
    inFile = open(fileName, 'r')
    for line in inFile:
        line = line.strip()
        key, value = line.split('\t')
        ClassDict[key] = int(value)
        
    return ClassDict


def totalCredits (theDictionary):
    totalCredits = sum(theDictionary.values())
    return totalCredits
        
        
    
def classesByDepartment(theDictionary, department):
    classByDept = []
    for item in theDictionary.keys():
        if item.startswith(department):
            classByDept.append(item)
    return classByDept

 
def classByCredits (theDictionary, credits):
    classByCredit = []
    for k,v in theDictionary.items():
        if v==credits:
            classByCredit.append(k)
    return classByCredit
    
def isFullTime(theDictionary):
    if sum(theDictionary.values()) >= 12:
        return True
    else:
        return False
    
def numOfClasses(theDictionary):
    return len(theDictionary)
    
def upperLevelCredits (theDictionary):
    creds = 0
    for k, v in theDictionary.items():
        courses = k.rsplit(' ')
        if len(courses) >= 2 and int(courses[1]) >= 300: #len(courses) verifies that the class was typed correctly and a split occured between the class type and number
            creds+= v
    return creds 
            
        

def printClasses(theDictionary):
    width = 8
    print("%-5s % 20s" % ("\nClass Name", "Number of Credits"))
    print("-------------------------------")
    for k , v  in theDictionary.items():
        print("%-5s %15s" % (f'{k:<{width}}' , f'{v:>{width}}'))
    print("Total number of credits this semester: ", sum(theDictionary.values()))

    
def main(): 
    ClassDict = readClasses(input("Enter a text file: "))
    totalCredits (ClassDict)
    classesByDepartment(ClassDict, 'CSCI')
    classByCredits(ClassDict, 4)
    isFullTime(ClassDict)
    numOfClasses(ClassDict)
    upperLevelCredits (ClassDict)
    printClasses(ClassDict)
    
main()