"""
Flavio Leon
3.20.2017

bmi.py
Calculate a persons bmi and print if with health tolerances.

Input: Weight in lbs, and height in inches.
Process: 1. Prompt for w and h. 2. Calculate using formula. 3. Display BMI and health range.
Output: Display BMI and health range status.
"""
def main():
    print("Body Mass Index Calculator...\n")
    weight=int (input("Enter your weight (in pounds):"))
    height=int (input("Enter your weight (in inches): "))
    print()
    bmi=weight*720/(height**2)

    if (bmi>=19 and bmi<=25):
        print("Your BMI is {0:0.4f}".format(bmi))
        print("That is in the healthy range.")
    else:
        print("Your BMI is {0:0.4f}".format(bmi))
        print("You are in danger of diabetes.")

main()
