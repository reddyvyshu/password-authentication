def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

students = [
    {"name": "Student1", "marks": [85, 78, 92]},
    {"name": "Student2", "marks": [70, 65, 60]},
    {"name": "Student3", "marks": [95, 90, 93]},
    {"name": "Student4", "marks": [50, 55, 58]},
    {"name": "Student5", "marks": [88, 82, 84]}
]

total_class_marks = 0
topper = None
highest_avg = 0

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    grade = assign_grade(avg)

    student["average"] = avg
    student["grade"] = grade

    total_class_marks += avg

    if avg > highest_avg:
        highest_avg = avg
        topper = student

    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print("-" * 30)

class_average = total_class_marks / len(students)

print("\nClass Average:", round(class_average, 2))
print("Topper:", topper["name"], f"with average {topper['average']:.2f}")
