grade = int(input(""))

if  grade >= 90 and grade <= 100:
    grade = "A"
elif grade >= 80 and grade < 90:
    grade = "B"
elif grade >= 70 and grade < 80:
    grade = "C"
elif grade >= 60 and grade < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is", grade)
