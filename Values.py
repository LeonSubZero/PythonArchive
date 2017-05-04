"""
values.py
Flavio Leon
3.28.17

Prompt user for the two number a and b and display:
    List of values from a to b
    Sum of values from a to b
    Multiplcation of values from a to b

Input: Two value A and B (a<=b)
Processing:  1. Prompt user for two number.
            2.List and disply valus from a to b.
            3. Calc and disp sum of values fro a to b.
            4. Calc and disp the multiplication of values from a to b.
            
Output: List, sum, and multiplication of values from a to b.

listValues(a,b)

Return a string containing the list of values from a to b.


"""
def listValues(a,b):
    s=" "
    for i in range(a, b+1):
        s=s+str(i)+" "
        print(s)
    return s

print(listValues(3,18))

def main():
    print("\nTesting listValues()")
    print(listValues(3,18))


main()
