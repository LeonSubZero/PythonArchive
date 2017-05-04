"""3
Flavio Leon
sumOfSquares.py

Calc the sum of squares of numbers read from a file
input: filename, r
process: prompt for filename, define several functions, one for converting list
from file to numbers.    1. Prompt for filename
                         2. def toNumbers,sqEach,sumList
                         3. Convert file toNumbers.
                         4. Call functions
                         5. Process returned values in for loop
                         6. Display

output:list of entries,square root of entries,sum of sq. entries.



3"""

def main():
    print("Program to find the sum of squares from numbers in a file...")
    print()

    filename=input("Enter filename: ")

    #open file
    inFile=open(filename, "r")

    #Read lines with numbers into a list
    #listNumbers = inFile.readlines()
    #print(listNumbers)
    
    #read numbers into a list
    listNumbers=inFile.readlines()
    #converts lines to numbers
    toNumbers(listNumbers)

    print("\nList of numbers:")
    for i in range(len(listNumbers)):
        print(listNumbers[i],end=" ")
    print()

    print("\nSquares of numbers:")
    squareEach(listNumbers)
    sum=0
    for i in range(len(listNumbers)):
        print(listNumbers[i],end=" ")
        #sum=sum+listNumbers[i]
    print()

    print("\nSum of squares:  "+sumList(listNumbers))
    

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i]=eval(strList[i])

    return

def squareEach(numList):
    for i in range(len(numList)):
        numList[i]=numList[i]**2
        
    return

def sumList(formalPar):
    
    sum=0
    for i in range(len(formalPar)):
        #print(formalPar[i],end=" ")
        sum=sum+formalPar[i]
    sum=str(sum)    
    return sum

main()












                   
