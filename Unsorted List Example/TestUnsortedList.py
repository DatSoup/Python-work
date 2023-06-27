from UnsortedList import *
#import UnsortedList 

def main():
    #ul1 = UnsortedList.UnsortedList (5)
    ul1 = UnsortedList (5)
    ul2 = UnsortedList ()
    try:
        ul1.add("a")
        ul1.add("b")
        ul1.add("c")
        ul1.add("d")
        ul1.add("e")
        ul1.add("f")
        ul1.add("g")
    except UnsortedListAddError as e:   
        print ("Here is where we deal with the error ")
        print (e)    
    except Exception as e:   
        print ("Here is where we deal with the error, this diff tho ")
        print (e)
    finally: #optional, but this code is done regardless of what happens in the try block
        ("Lets see what this does :-)")
    print ("Is b in the list? (should be there) ", ul1.isInList ("b"))
    ul1.remove ("b")    
    print ("Is b in the list? (should not be there now) ", ul1.isInList ("b"))
    ul1.reset()
    for counter in range (ul1.size() * 3):
        print (ul1.getNextItem(), end=' ')
    print ()    
    print ("Should go back to the beginning ", ul1.getNextItem())
    print ("Iterating through ul1 using the for loop")
    for item in ul1:
        print (item, end= ' ')
    print ()    
    print ("Iterating through ul2 using the for loop")
    for item in ul2:
        print (item, end= ' ')
    print ()    
    ul1.remove3 ("a")    
    print ("Iterating through ul1 using the for loop after removing a")
    for item in ul1:
        print (item, end= ' ')
    print ()    
    
main()    