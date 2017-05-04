"""
Flavio Leon
3.30.17
sphere.py

Menu-driven interface program that allows the user to:
    1.Calc the surface area of a sphere.
    2.Calc the volume of a sphere.
    3. Quit


""""
import math
def main():
    print("Geometry Calculator App...")
    print()
    option=0
    #Menu
    while option !==3:
        
        print("Choose one of the following options:")
        print("\t1. Calculate the surface area of a sphere.")
        print("\t2.Calculate the volume of a sphere.")
        print("\t3. Quit")
        option=eval(input("Option: "))
        
        
        #Drive menu option
        if option ==1: #Area of a Sphere
            #Prompt user for radius
            radius=getRadius()
            #Calculate area
            area=sphereArea(radius)

            #Display result
            print("The surface area is",area)
            print()
            
        elif option ==2:    #Volume of a sphere
            print()
            #Prompt user for radius
            #Calculate the volume
            #Display result
        elif option ==3: #Quit
            print("Good Bye...")
            print()

        else:           #Invalid option    
            print("Error...invalid try again")
#def getRadius()
#
#Prompt the user for the radius of a sphere,
#and returns the value entered.
    
def getRadius():
    rad = -1
    while rad <0:
        #Prompt user for radius
        rad = eval(input("\nPlease enter sphere radius: "))
        if rad <0:
            print("Error...Invalid radius. Try Again")
    return rad
            
def sphereArea(rad):
    #Calculate area
    area = 4* math.pi *rad**2
    return area
    

main()
