#Chris Campbell
#c.campbell.1@und.edu
#Wk 3 Part 2

#Inputs
x = int(input("Please enter a value for x: "))
y = int(input("Please enter a value for y: "))

#Quadrant I
if x > 0 and y > 0:
    print ("(", x, ",",y, ")"," ","is in quadrant I.", sep='')

#Quadrant II
elif x < 0 and y > 0:
    print ("(", x, ",",y, ")"," ","is in quadrant II.", sep='')
    
#Quadrant III
elif x <0 and y <0:
    print ("(", x, ",",y, ")"," ","is in quadrant III.", sep='')
        
#Quadrant IV
elif x > 0 and y < 0:
    print ("(", x, ",",y, ")"," ","is in quadrant IV.", sep='')
    
#Not in a quadrant
else:
    print ("(", x, ",",y, ")"," ","is not in a quadrant.", sep='')
