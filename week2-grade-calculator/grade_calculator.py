# Student Grade Calculator
# The Developers Arena - Week 2

print("=" * 40)
print("STUDENT GRADE CALCULATOR")
print("=" * 40)

name = input("Enter student name: ")

try:
    math = float(input("Enter Maths marks (0-100): "))
    science = float(input("Enter Science marks (0-100): "))
    english = float(input("Enter English marks (0-100): "))

    marks = [math, science, english]

    if any(m < 0 or m > 100 for m in marks):
        print("Error: Marks must be between 0 and 100.")

    else:
        total = sum(marks)
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        print("\n" + "=" * 40)
        print("STUDENT RESULT")
        print("=" * 40)

        print(f"Student Name: {name}")
        print(f"Mathematics: {math:g}")
        print(f"Science: {science:g}")
        print(f"English: {english:g}")
        print("-" * 40)
        print(f"Total Marks: {total:g}/300")
        print(f"Average: {average:.2f}")
        print(f"Highest Marks: {max(marks):g}")
        print(f"Lowest Marks: {min(marks):g}")
        print(f"Final Grade: {grade}")

except ValueError:
    print("Error: Please enter valid numbers.")
