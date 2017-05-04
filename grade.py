"""
Flavio Leon
3.20.2017

grade.py

Calculate the corresponding grade using the input of an exam score.

Input: exam score
Process: 1.Prompt for score 2. Use if statements to create ranges
for the letter grade and scores.  3. Display
Output: Final letter grade.

"""
def main():
    print("Exam Grader...")

    score=int (input("\nEnter the score: "))
    print()
    if (score>=90 and score<=100):
        print("The grade is A")
    elif (score<90 and score>=80):
        print("The grade is B")
    elif (score<80 and score >=70):
        print("The grade is C")
    elif (score<70 and score >=60):
        print("The grade is D")
    else:
        print("The grade is F")

main()
