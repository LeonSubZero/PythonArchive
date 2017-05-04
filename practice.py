"""
Flavio Leon
exam2practice.py

A program to test a few functions .

"""


def main():
    print("Functions App...")
    file=input("\nInsert filename:" )
    DisplayFile(file)

    num=int(input("\nInsert a number to see if it is even: "))
    print(isEven(num))

    score=int(input("\nYour test score is?"))
    LetterGrade(score)

    m1, m2, m3, m4=eval(input("\nEnter 4 numbers seperated by commas just becuz: "))
    MIN , MAX , AVG=NumAnalysis(m1,m2,m3,m4)
    print("Minimum: ",MIN,"\nMaximum: ", MAX, "\nAverage: ",AVG)

    great=[]
    n1, n2=eval(input("\nEnter two number sep by comma to have the greatest retorted to you: "))
    great=GreatestNumber(n1,n2,great)
    print(great[0])
    
    isIs=[]
    n1=eval(input("\nEnter number to see if it is divisible by 3: "))
    isIs=isMultipleThree(n1,isIs)
    print(isIs[0])

    AList=[]
    AList=Login(AList)
    print("Your id and pw is:",AList[0],AList[1])

    

def DisplayFile(filename):

    infile=filename
    whole=open(infile,"r")
    wholefile=whole.read()
    print(wholefile)

    return


def isEven(number):
    if (number%2==0):
        return True
    else:
        return False


def LetterGrade(score):
    if (score>=90):
        print("Your grade is A.")
    elif (score>=80):  
        print("Your grade is B.")
    elif (score>=70):
        print("Your grade is C.")
    elif (score>=60): 
        print("Your grade is D.")
    else:
        print("Your grade is F.")
    return

def NumAnalysis(n1,n2,n3,n4):
    minim=n1
    if n2<minim:
        minim=n2
    if n3<minim:
        minim=n3
    if n4<minim:
        minim=n4
    #determ max
    maxim=n2
    if n1>maxim:
        maxim=n1
    if n3>maxim:
        maxim=n3
    if n4>maxim:
        maxim=n4
    #calc avg
    avg=(n1+n2+n3+n4)/4

    return minim, maxim,avg

def GreatestNumber(num1, num2, greatest):
    ##greatest=[]
    if(num1>num2):
        greatest=[num1]
    if(num2>num1):
        greatest=[num2]
    return greatest

def isMultipleThree(n, isIt):
    if (n%3==0):
        isIt=[True]
    else:
        isIt=[False]
    return isIt

def Login(user):
    user=[input("What is your ID:"),input("What is your pw:")]
    
    return user


main()
