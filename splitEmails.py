def main():

    email="johndoe@broward.edu"
    email.split("@")
    part2=email.split("@")[1]
    print(part2)

    #list=[]
    #list=login(list)
    #print(list)

    score=eval(input("score:"))
    print(getLetterGrade(score))
    


def getLetterGrade(score):
    score = round(score)
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    for i in range(len(grades)):
        if score >= grades[i][0]:
            return grades[i][1]    




def grade(gr):
    grade=[a,b]
    
    return grade
    


def login(user):
    user=[str(input("Type ur id: ")),str(input("Type password: "))]
    return user

main()
