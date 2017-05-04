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


def main():
    print("Playing with Values App...\n")

    print("Please enter two values:")
    Va=eval(input("\tFirst: "))
    Vb=eval(input("\tLast: "))
    if Va>=Vb:
        Va,Vb=Vb,Va
            
                 

    print("\nFrom "+str(Va)+" to "+str(Vb)+":",end="")
    print(listValues(Va,Vb))
    
    print("\n\tSum of Values: ", end="")
    print(sumValues(Va,Vb))

    print("\tMultiplication of values: ", end="")
    print(xValues(Va,Vb))

def listValues(a,b):
    #initialize accumulator
    s=" "

    #concatenate values from a to b
    for i in range(a, b+1):
        s=s+str(i)+" "
        #print(s)
    #return the list    
    return s


# def sumValues(a,b)
# Calc and return the sum
def sumValues(a, b):
    #initialize accumulator
    sum=0

    for i in range(a, b+1):
        sum = sum+i

    return sum

#def xValues(a,b)
#return product

def xValues(a, b):
    prod=1
    for i in range(a,b+1):
        
        prod=prod*i

    return prod

    

main()
