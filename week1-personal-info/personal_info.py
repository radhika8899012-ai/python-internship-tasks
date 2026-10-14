# Personal Information Manager
# Week 1 Python Internship Assignment

print("===== Personal Information Manager =====")

name = input("Enter your full name: ")
age_input = input("Enter your age: ")

try:
    age = int(age_input)

    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        city = input("Enter your city: ")
        course = input("Enter your course: ")

        print("\n===== Your Information =====")
        print(f"Name: {name}")
        print(f"Age: {age} years")
        print(f"Age in months: {age * 12} months")
        print(f"City: {city}")
        print(f"Course: {course}")

except ValueError:
    print("Error: Please enter age as a whole number.")
