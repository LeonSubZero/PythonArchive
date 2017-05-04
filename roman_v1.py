"""
Flavio Leon

roman_v1.py

Prompt the user for a number from 1-10 and display it's corresponding Roman numeral.


"""

def main():
    print("Roman Numeral Converter App... ")
    print()

    number=0 #Temporary value to avoid error.
    while(number<1 or number>10)
        #promt for number 1-10
        number= int(input("Please enter a number (1-10): "))

        #Display corresponding roman numeral

        if (number>10 or number<1):
        print("\n\tError....Invalid Number")
        else:
        print()
        print("Roman Numeral: ", end=" ") 
            if (number ==1):
                print("I")
            if (number ==2):
                print("II")
            if (number ==3):
                print("III")
            if (number ==4):
                print("IV")
            if (number ==5):
                print("V")
            if (number ==6):
                print("VI")
            if (number ==7):
                print("VII")
            if (number ==8):
                print("VIII")
            if (number ==9):
                print("IX")
            if (number ==10):
                print("X")

            
main()
