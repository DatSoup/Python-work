#Build our own error on top of the Exception error object
#we are creating a more specific type of exception, called a subclass Exception
class UnsortedListAddError (Exception):
    pass #must have at least one line of code in a class, but I don't really want to add anything

class UnsortedListGetNextItemError (Exception):
    pass #must have at least one line of code in a class, but I don't really want to add anything



class UnsortedList:

    def __init__ (self, maxSize=100):
        self.__data = [None] * maxSize #creates the entire list, with each value assigned None 
        self.__numOfItems = 0
        self.__currentIndex = 0
        self.__nextIndex = 0
        self.__maxSize = maxSize #store the max number of values that can be in the list
        pass

    def add (self, itemToAdd):
        if not self.isFull():
            self.__data[self.__numOfItems] = itemToAdd
            self.__numOfItems += 1
            self.reset()
        else:
            #raise Exception ("Unable to add " + itemToAdd + " to a full UnsortedList") Exception is a generic exception
            raise UnsortedListAddError ("Unable to add " + itemToAdd + " to a full UnsortedList")

    def remove (self, itemToRemove):
        for index in range (0, self.__numOfItems):
            if self.__data[index] == itemToRemove:
                #for index2 in range (index, self.__numOfItems -1):
                #    self.__data[index2] = self.__data[index2 + 1]
                self.__data[index] = self.__data[self.__numOfItems - 1] #replace the item to be removed with the last item 
                self.__data[self.__numOfItems - 1] = None    
                self.__numOfItems -= 1    
                self.reset()
                return True
        return False    

    def __findIndexOf (self, itemToFind):
        for index in range (0, self.__numOfItems):
            if self.__data[index] == itemToFind:
                return index 
        return -1 #didn't find itemToFind in the list     

    def remove2 (self, itemToRemove):  #original remove
        for index in range (0, self.__numOfItems):
            if self.__data[index] == itemToRemove:
                for index2 in range (index, self.__numOfItems -1):
                    self.__data[index2] = self.__data[index2 + 1]
                self.__data[self.__numOfItems - 1] = None    
                self.__numOfItems -= 1    
                self.reset()
                return True
        return False    

    def remove3 (self, itemToRemove):  #original remove
        index = self.__findIndexOf (itemToRemove)
        if index != -1:
            for index2 in range (index, self.__numOfItems -1):
                self.__data[index2] = self.__data[index2 + 1]
            self.__data[self.__numOfItems - 1] = None    
            self.__numOfItems -= 1    
            self.reset()
            return True
        return False    


    def isInList (self, itemToFind):
        #for index in range (0, self.__numOfItems):
        #    if self.__data[index] == itemToFind:
        #        return True
        #return False
        return self.__findIndexOf(itemToFind) != -1

    def edit (self, currentValue, newValue):
        for index in range (0, self.__numOfItems):
            if self.__data[index] == currentValue:
                self.__data[index] = newValue
                return True
        return False    

    def maxSize(self):
        return self.__maxSize

    def size(self):
        return self.__numOfItems

    def count (self, itemToCount):
        count = 0
        for index in range (0, self.__numOfItems):
            if self.__data[index] == itemToFind:
                count += 1
        return count 

    def isFull (self):
        return self.__numOfItems == self.__maxSize


    def isEmpty(self):
        return self.__numOfItems == 0

    def reset(self):
        '''
        reset ensures that the next call to getNextItem will return the first item in the UnsortedList
        '''
        self.__currentIndex = 0
        #self.__nextItem = 0

    def getNextItem(self):
        '''
        getNextItem returns the "current" item in the list. Subsequent calls to getNextItem
        will return the next item in the list. Once the end of the list has been reached the
        next call to getNextItem will return the first item. 

        '''
        temp = self.__data[self.__currentIndex]
        self.__currentIndex += 1
        if self.__currentIndex == self.__numOfItems:
            self.__currentIndex = 0
        return temp

    def __iter__ (self):
        self.__nextIndex = 0
        return self

    def __next__ (self):
        if self.__nextIndex == self.__numOfItems:
            raise StopIteration

        temp = self.__data[self.__nextIndex]
        self.__nextIndex += 1
        return temp    