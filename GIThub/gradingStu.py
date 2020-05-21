grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)


def gradingStudents(grades):
    # Write your code here
    for j in range(len(grades)):
        i = grades[j]
        if i >= 38:
            if abs(i % 5 - 5) < 3:
                grades[j] = (i+(5-i % 5))
        else:
            continue
    return grades


result = gradingStudents(grades)
print(result)
