"""
Flavio Leon

roman_v1.py

Prompt the user for a number from 1-10 and display it's corresponding Roman numeral.


"""

def main():
    print("Roman Numeral Converter App... ")
    print()

    number=0 #Temporary value to avoid error.
    while(number<1 or number>10):
        #promt for number 1-10
        number= int(input("Please enter a number (1-10): "))

        #Display corresponding roman numeral

        print("Roman Numeral: ", end=" ") 
        if (number ==1):
            print("I")
        elif (number ==2):
            print("II")
        elif (number ==3):
            print("III")
        elif (number ==4):
            print("IV")
        elif (number ==5):
            print("V")
        elif (number ==6):
            print("VI")
        elif (number ==7):
            print("VII")
        elif (number ==8):
            print("VIII")
        elif (number ==9):
            print("IX")
        elif (number ==10):
            print("X")
        else:
            print("\n\tError....Invalid Number")
main()
