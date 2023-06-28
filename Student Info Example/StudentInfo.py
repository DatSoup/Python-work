class StudentInfoFullError (Exception):
    pass

class StudentInfo:
    
    #inner class - designed to be used ONLY within the StudentInfo class
    class __Student:
        def __init__(self, studentName, studentCredits = -1):
            self.studentName = studentName
            self.studentCredits = studentCredits
            
        def classLevel (self):
            if self.studentCredits >= 90:
                return "Senior"
            elif self.studentCredits >= 60:
                return "Junior"
            elif self.studentCredits >= 24:
                return "Sophomore"
            else:
                return "Freshman"            

            
        
    def __init__(self, maxSize = 10):
        #self.__studentName = [None] * maxSize
        #self.__studentCredits = [None] * maxSize
        self.__data = [None] * maxSize
        self.__numOfItems = 0
        self.__nextLocation = 0
        
    def add (self, studentName, studentCredits):
        '''add methods add the name and number of credits to the list
        No searching is done to determine if the name currently exists in the list
        No error checking is done to validate the range of credits
        
        Raises a StudentInfoFullError exception if attempting to add to a full list
        '''
        #self.__studentName[self.__numOfItems] = studentName
        #self.__studentCredits[self.__numOfItems] = studentId
        if not self.isFull():
            self.__data[self.__numOfItems] = StudentInfo.__Student (studentName, studentCredits)
            self.__numOfItems += 1
            
        else:
            raise StudentInfoFullError ("Error attempting to add a student to a full list")
        
    def isFull (self):
        #This is a stub, it's syntactically correct, but not logically correct
        #with the idea we want to move on and we'll fix it later
        return False
    
    def classLevel (self, studentName):
        for index in range (0, self.__numOfItems):
            if self.__data[index].studentName == studentName:
                return self.__data[index].classLevel()
        return None #return None if the given student name doesn't exists in our data
    
    def getCredits (self, studentName):
        '''getCredits returns the number of credits for the given student
        
        returns -1 if the given student name doesn't exits in the data
        '''        
        for index in range (0, self.__numOfItems):
            if self.__data[index].studentName == studentName:
                return self.__data[index].studentCredits
        return -1 #return None if the given student name doesn't exists in our data        
    
    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.__nextLocation ==self.__numOfItems:
            self.nextLocation = 0
            raise StopIteration
        
        temp = self.__data[self.__nextLocation].studentName
        self.__nextLocation += 1
        return temp
    