# height = float(1.61)
# print(height)
# height = int(input('input ur height:'))
# print(type(height))


studentName = input("Введите имя студента: ")
subject1 = float(input("Введите оценку по первому предмету: "))
subject2 = float(input("Введите оценку по второму предмету: "))
subject3 = float(input("Введите оценку по третьему предмету: "))

average_grade = (subject1 + subject2 + subject3) / 3

passing_grade = 4.0
is_allowed = average_grade >= passing_grade

print("\n--- Результаты ---")
print(f"Студент: {studentName}")
print(f"Средний балл: {average_grade:}")

