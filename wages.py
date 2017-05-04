"""
Flavio Leon
3.14.17

wages.py

Calculates the total wages for a week based on the number of hours worked,
and the hourly rate.


Input:  Hours worked and hourly rate.
Process:  1. Prompt user for hours and rates.
    2. Calculate total wages such that:
        if (hours<=40)
            wages = hours * rate
        else 
            Calculate overtime:
                overtime= hours - 40
            Calculate weekly wages:
                wages= (40 * rate) + (overtime * rate * 1.5)
    3. Display result.
                
    
Output:  Total wages for a week.

"""
def main():
    #heading
    print("Weekly Pay Calculator...")
    print()

    # Prompt user for hours and rate
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate:  "))

    #Calculate total wages
    if (hours <= 40):
        wages = hours * rate
    else :
        overtime = hours - 40
        wages = float(40 * rate) + (overtime * rate * 1.5)
    # Display result
    print("\nYour week's pay is ${0:0.2f}".format(wages))

main()
