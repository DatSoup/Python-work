from StudentInfo import *

def main():
    myCSStudents = StudentInfo()
    myDSStudents = StudentInfo()
    
    myCSStudents.add ("Tom", 250)
    myCSStudents.add ("Fred", 25)
    myCSStudents.add ("Chris", 150)
    myCSStudents.add ("Nick", 70)
    myCSStudents.add ("Ella", 9)
    
    for name in myCSStudents:
        print ( "%-15s%-5d%-15s" % (name, myCSStudents.getCredits(name), myCSStudents.classLevel(name)))

    
main()