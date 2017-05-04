"""
Flavio Leon

roman_v2.py

Prompt the user for a number from 1-10 and display it's corresponding Roman numeral.

Note: Uses if else statement


"""

def main():
    print("Roman Numeral Converter App... ")
    print()

    number=0 #Temporary value to avoid error.
    while(number<1 or number>10):
        #promt for number 1-10
        number= int(input("Please enter a number (1-10): "))

        #Display corresponding roman numeral

        if (number>10 or number<1):
            print("\n\tError....Invalid Number")
        else:
            print("Roman Numeral: ", end=" ") 
            if (number ==1):
                print("I")
            else:        
                if (number ==2):
                    print("II")
                else:   
                    if (number ==3):
                        print("III")
                        else:
                            if (number ==4):
                                print("IV")
                            else:
                                if (number ==5):
                                    print("V")
                                else:
                                    if (number ==6):
                                        print("VI")
                                    else:
                                        if (number ==7):
                                            print("VII")
                                         else:       
                                            if (number ==8):
                                                print("VIII")
                                            else:
                                                if (number ==9):
                                                    print("IX")
                                                else:
                                                   
                                                        print("X")

            
main()
