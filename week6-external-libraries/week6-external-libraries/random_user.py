from faker import Faker

fake = Faker()

def generate_user():
    print("----- Random User Details -----")
    print("Name:", fake.name())
    print("Address:", fake.address())
    print("Email:", fake.email())
    print("Phone:", fake.phone_number())
    print("Job:", fake.job())

generate_user()
