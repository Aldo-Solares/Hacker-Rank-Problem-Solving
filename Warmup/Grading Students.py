
#LINK https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

def gradingStudents(grades):
    round_grades = []
    for x in grades:
        if x >= 38 and x%5 >=3:
            round_grades.append(x-(x%5)+5)
        else:
            round_grades.append(x)
    return round_grades

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    for _ in result:
        print(_)