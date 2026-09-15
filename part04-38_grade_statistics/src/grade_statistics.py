
exam_points = []
exercise_completed = []
exercise_points = []
grade = []

while True:
    user_input = input("Exam points and exercises completed: ")

    if user_input == "":
        break

    parts = user_input.split()
    exam = int(parts[0])
    exercise = int(parts[1])

    exam_points.append(exam)

    
    exercise_points.append(exercise // 10)

sum_list = [a + b for a, b in zip(exam_points, exercise_points)]

for total, exam in zip(sum_list, exam_points):
      
    if exam < 10 or total <= 14:
        grade.append(0)
    elif total <= 17:
        grade.append(1)
    elif total <= 20:
        grade.append(2)
    elif total <= 23:
        grade.append(3)
    elif total <= 27:
        grade.append(4)
    elif total <= 30:
        grade.append(5)

average = sum(sum_list) / len(grade)
passing = 0
for number in grade:
     if number > 0:
          passing += 1

pass_percentage = (passing / len(grade)) * 100

print("Statistics:")
print(f"Points average: {average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")

for i in range(5, -1, -1):
     stars_count = grade.count(i)

     stars = "*" * stars_count
     print(f" {i}: {stars}")
