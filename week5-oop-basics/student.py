class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


student1 = Student("Radhika", 20, "A")
student1.display_info()
