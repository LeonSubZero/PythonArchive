#
#  Flavio Leon
#
#   convert_v1.py
#
#   Create a table showing Cel to Fahren
#   Temperatures every 10 deg, for 0C to 100C
#   
#
#
#   Input:  Temperature in Celsius
#
#   Processing: For each celsius temp:
#               Calculate corresponding temp in Fahrenheit:
#                   fahrenheit = 9/5 *celsius+32
#               Display result
#               
#   Output: Table of equivalent temps to Fahren
#

def main():
    print()
    print("Temperature Converter App....")
    print()

    #Display table heading
    print("Celsius       Fahrenheit")
    print("========================")

    #Calculate corresponding temp in Fahrenheit
    celsius = 0
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 10
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 20
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 30
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 40
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 50
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 60
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 70
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 80
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 90
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)
    celsius = 100
    fahrenheit = 9/5 * celsius +32
    print("  ", celsius, "\t\t", fahrenheit)

          
    #Display result
    #print("The temp in Fahrenheit is:", fahrenheit)
    
main()
