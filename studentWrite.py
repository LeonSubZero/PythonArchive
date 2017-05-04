#Flavio Leon
#2.22.17
#studentWrite.py
#
#Program that asks the user for the id,name,and gpa of 5 students and saves to file called students.txt
#
#input: id,name,gpa
#process: prompt for id, name, and gpa
#output: to students.txt

def main():

    outfile=open("students.txt", "w")
    for i in range(1,6,1):
        
        #Prompt user for student info
         
        print("Please enter the following data for student",i)
        id = float(input("\tStudent Id: "))
        name = input("\tStudent Name: ")
        gpa = float(input("\tStudent GPA: "))
        print(id, file=outfile)
        print(name, file=outfile)
        print(gpa, file=outfile)

    outfile.close()
        
main()
