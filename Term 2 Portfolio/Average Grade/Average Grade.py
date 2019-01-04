#Parker Dean
#Average Grade


gradelist = []

def getGrade(gradelist):
    maxGrade = 100
    while True:
        grade = input("Enter in a grade, to exit press spacebar: ")
        if grade == " ":
            break
        else:
            x = float(grade)
            if grade.isdigit() and x <= maxGrade:
                grade = float(grade)
                gradelist.append(grade)
            elif x >= maxGrade:
                q = input("Are you sure "+ grade+ " is the correct grade? yes or no: ")
                if q == "yes":
                    grade = float(grade)
                    gradelist.append(grade)
            else:
                print("That's not an actual grade ")


def avgGrade(gradelist):
    sumgrade = 0
    for grade in gradelist:
        sumgrade += grade
    avg = sumgrade/len(gradelist)
    return avg

def main(gradelist):
    getGrade(gradelist)
    avg = avgGrade(gradelist)
    print("Your final grade is" , avg)


main(gradelist)
















