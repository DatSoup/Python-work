#Chris Campbell
#c.campbell.1@und.edu
#Program 1a

def FtoC( fahr ):
    # Convert from Fahrenheit to celcius
    celsius = (fahr - 32) * (5.0/9.0)
    return celsius

def FtoK ( fahr ):
    # Convert from Fahrenheit to Kelvin
    kelvin = (fahr + 459.67) * (5.0/9.0)
    return kelvin

def CtoK ( celsius ):
    # Convert from Celsius to Kelvin
    kelvin = celsius + 273.15
    return kelvin
    
def CtoF ( celsius ):
    # Convert from Celsius to Fahrenheit
    fahr = celsius * (9.0/5.0) + 32
    return fahr

def KtoC ( kelvin ):
    # Convert from Kelvin to Celsius
    celsius = kelvin - 273.15
    return celsius

def KtoF ( kelvin ):
    # Convert from Kelvin to Fahrenheit
    fahr = kelvin * (9.0/5.0) - 459.67
    return fahr

def getMenuChoice( ):
    # Show the menu and return a valid choice within the range of 1-7
    print("1) Fahrenheit to Celsius")
    print("2) Fahrenheit to Kelvin")
    print("3) Celsius to Kelvin")
    print("4) Kelvin to Celsius")
    print("5) Celsius to Fahrenheit")
    print("6) Kelvin to Fahrenheit")
    print("7) Quit")
    x = input("Selection: ")
    if x == '1':
        fahr = float(input('\nFahrenheit temperature: '))
        celsius = FtoC(fahr)
        print (f'{fahr:.2f} degrees in Fahrenheit is {celsius:.2f} degrees in Celsius')
        
    elif x == '2':
        fahr = float(input('\nFahrenheit temperature: '))
        kelvin = FtoK ( fahr )
        print (f'{fahr:.2f} degrees in Fahrenheit is {kelvin:.2f} degrees in Kelvin')
    
    elif x == '3':
        celsius = float(input('\nCelsius temperature: '))
        kelvin = CtoK ( celsius )
        print (f'{celsius:.2f} degrees in Celsius is {kelvin:.2f} degrees in Kelvin')
        
    elif x == '4':
        kelvin = float(input('\nKelvin temperature: '))
        celsius = KtoC ( kelvin )
        print (f'{kelvin:.2f} degrees in Kelvin is {celsius:.2f} degrees in Celsius')
        
    elif x == '5':
        celsius = float(input('\nCelsius temperature: '))
        fahr = CtoF ( celsius )
        print (f'{celsius:.2f} degrees in Ceslsius is {fahr:.2f} degrees in Fahrennheit')
        
    elif x == '6':
        kelvin = float(input('\nKelvin temperature: '))
        fahr = KtoF ( kelvin )
        print (f'{kelvin:.2f} degrees in Kelvin is {fahr:.2f} degrees in Fahrenheit')
        
    elif x == '7':
        print ('\nExiting program.')
        
def main():
    # Main program
    getMenuChoice( )

main()