#
#
#  Flavio Leon
#   finalgrade.py
#
#   Calculate a students final grade
#
#   Input:  Students id and name.
#           Midterm final and project grades.
#           
#   Processing: 1. Prompt user for stud id and name.
#               2.                   " grades.  
#               3. Calculate final grade:
#                   final_grade = (midterm + final + project)/3
#               4. Display Result
#
#   Output: Final Grade Report

def main():
    # Display App Header
    print()
    print("Final Grade Calculater....")

    n = int (input("What is the the number of students:  "))
    print()
    print ("The number of students in the class: ", n)
    print()
    for i in range(1,n+1,1):
    
        #Prompt user for student info
         
        print("Please enter the following data for student",i)
        id = input("\tStudent Id: ")
        name = input("\tStudent Name: ")
        midterm, final = eval(input("Midterm and Final Exam"
                               +" Grade (sep by commas: "))
        project = int(input("Project Grade: "))

        #Calculate final grade
        final_grade = (midterm + final + project)/3

        #Display result
        print()
        print("\tFinal Grade:", final_grade, sep='\t')

main()
