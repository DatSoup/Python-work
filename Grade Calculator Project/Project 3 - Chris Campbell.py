#Chris Campbell
#c.campbell.1@und.edu
#Project 3

#Creates dictionary for honorPoints system
honorPoints = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

#reads txt file and returns a dictionary
def readClassInfo(fileName):
    with open (fileName, 'r') as f:
        classes = {}
        for line in f:
            if line.strip() != '':
                line = line.strip()
                className, grade, credits = line.split('\t')
                addClass(classes, className, grade, credits)
    return classes  
    
#writes a text file from the dictionary input
def writeClassInfo(fileName, classes):
    with open (fileName, 'w') as f:
        for className, (grade, credits) in classes.items():
            f.write("%s\t%s\t%d\n" % (className, grade, int(credits)))
        f.close() 

#adds classes to the dictionary if it doesn't already exists in the dictionary    
def addClass(classes, className, grade, credits):
    if className in classes:
        classes[className] = (grade, credits)
        return False
    else:
        classes[className] = (grade, credits)
        return True
    
#Returns the number of attempted credits    
def attemptedCredits(classes):
    return sum(int(credits) for grade, credits in classes.values())

#Returns the number of passed credits
def passedCredits (classes):
    return(sum(int(credits) for grade, credits in classes.values() if grade in 'ABCD'))

#Returns the number of passed classes
def passedClasses (classes):
    passedClasses = 0
    for grade, credits in classes.values():
        if grade == 'A':
            passedClasses += 1
        elif grade == 'B':
            passedClasses += 1
        elif grade == 'C':
            passedClasses += 1
        elif grade == 'D':
            passedClasses += 1
        else:
            passedClasses += 0
    return passedClasses

#Prints the table for all classes, grades, credits, and overall gpa
def printClasses(classes):
    print('{:<20}{:<10}{:>}'.format('Class', 'Grade', 'Credits'))
    print('-------------------------------------')
    for className, (grade, credits) in classes.items():
        print('{:<22}{:<10}{:>}'.format(className, grade, credits))
    print(f"\nOverall GPA: {getGPA(classes):.3f}")
 
 #calculates GPA   
def getGPA (classes):
    totalHonorPoints = 0
    for grade, credits in classes.values():
        totalHonorPoints += int(credits) * honorPoints[grade]
    return totalHonorPoints/attemptedCredits(classes)

#Updates a grade for a class
def updateGrade (classes, className, newGrade):
    if className in classes:
        classes[className] = (newGrade, classes[className][1])
        return True
    else:
        return False
    
#Indicates which year a student is based off overall credits taken
def classStatus (classes):
    classStatus = 0
    if passedCredits (classes) < 24:
        classStatus = "Freshman"
    elif 24 <= passedCredits (classes) < 60: 
        classStatus ="Sophomore"
    elif 60 <= passedCredits (classes) < 90: 
        classStatus ="Junior"
    elif 90 <= passedCredits (classes): 
        classStatus ="Senior"
    return classStatus

#Main funcion used to call the dictionary from a txt file and output the data into a table    
def main ():
    classes = readClassInfo('UpdatedProject.txt')
    updateGrade (classes, 'EE 201', 'A')
    addClass(classes, 'CSCI 161', 'A', '4')
    printClasses(classes)
    passedClasses (classes)
    passedCredits (classes)
    classStatus (classes)
    attemptedCredits(classes)
    writeClassInfo('UpdatedProject.txt', classes)
    
main()