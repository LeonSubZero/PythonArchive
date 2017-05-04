"""
Flavio Leon
3.21.2017
congress.py

Calculate if a person's age and citizens makes them eligible for senate or house.
input:   age and years citizen
process: 1. Prompt for age and years cit.
         2. Create if-else statement with ranges.
         3. Display eligibility status.
output: Display eligible for both, one or the other, or none.

"""
def main():
    print("Congressional Eligibility...\n")
    age=int (input("Enter your age: "))
    czn=int (input("Enter years of citizenship: "))
    if (age>=30 and czn>=9):
        print("You are eligible for the Senate and the House.")
    elif (age>=25 and age<=30 and czn>=7):
        print("You are eligible for the House alone.")
    else:
        print("You are currently ineligible.")

main()
