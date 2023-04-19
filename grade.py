def grade():
    if 85 < marks <= 100:
        print("A")
    elif 75 < marks <= 85:
        print("B")
    elif 65 < marks <= 75:
        print("C")
    elif 60 < marks <= 65:
        print("D")
    elif 50 < marks <= 60:
        print("E")
    elif 0 < marks <= 60:
        print("F")
    else:
        exit("WRONG MARK TYPED")


def average():
    if 70 < Average <= 100:
        print("You are above Average")
    elif 50 < Average <= 70:
        exit("You are Average")
    else:
        exit("You are below Average")


english_marks = int(input("what mark did you get for english?"))
marks = english_marks
grade()

science_marks = int(input("what mark did you get for science?"))
marks = science_marks
grade()

math_marks = int(input("what mark did you get for maths?"))
marks = math_marks
grade()

social_marks = int(input("what mark did you get for social?"))
marks = social_marks
grade()

marks = [english_marks, science_marks, math_marks, social_marks]

sum = marks[0] + marks[1] + marks[2] + marks[3]

print("Sum of all three causes =", sum)

Average = (sum) / 4

print("Average=", Average)
average()
