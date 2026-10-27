import json
import os

FILE_NAME = "contacts_data.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading contacts file.")
            return {}
    return {}


def save_contacts(contacts):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)
    except OSError:
        print("Error saving contacts.")


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone are required!")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_contact(contacts):
    query = input("Enter name to search: ").strip().lower()

    if not query:
        print("Please enter a name.")
        return

    found = False

    for name, details in contacts.items():
        if query in name.lower():
            print("\nName:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter exact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone (Enter to skip): ").strip()
    email = input("Enter new email (Enter to skip): ").strip()

    if phone:
        contacts[name]["phone"] = phone

    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    name = input("Enter exact name to delete: ").strip()

    if name in contacts:
        confirm = input("Confirm deletion? (yes/no): ").lower()

        if confirm == "yes":
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
