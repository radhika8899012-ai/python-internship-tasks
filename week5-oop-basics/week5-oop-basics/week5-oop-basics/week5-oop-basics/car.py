class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.make, self.model, "is starting.")

    def stop(self):
        print(self.make, self.model, "has stopped.")

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)


car1 = Car("Toyota", "Innova", 2024)
car1.display_info()
car1.start()
car1.stop()
