"""
Flavio Leon
cylinder.py
3/1/2017
Calculate volume of cylinder.

input: radius and height
process: prompt for radius and height. calc volume. v=pie*r**2h
output: display volume
"""
#import math library
import math
def main():
    #header
    print("Volume of a Cylinder...")
    print()
    #prompt for
    rad, height = input("Enter radius and height of cylinder (seperated by commas):").split(",")
    rad=float(rad)
    height=float(height)
    #calc vol
    v=math.pi*rad**2*height
    #display results
    print("The volume of a cylinder with:") 
    print("\tRadius:{0:0.4f} and Height:{1:0.4f} is {2:0.4f}".format(rad,height,v))


main()
