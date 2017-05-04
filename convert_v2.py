#
#  Flavio Leon
#
#   convert_v2.py
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
    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius +32
        print("  ", celsius, "\t\t", fahrenheit)
    

          
    #Display result
    #print("The temp in Fahrenheit is:", fahrenheit)
    
main()
