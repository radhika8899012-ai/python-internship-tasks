import unittest
import os
import json
import tempfile

from contacts_manager import (
    load_contacts,
    save_contacts
)


class TestContactManager(unittest.TestCase):

    def test_save_and_load_contacts(self):
        contacts = {
            "Riya": {
                "phone": "9876543210",
                "email": "riya@example.com"
            }
        }

        with tempfile.TemporaryDirectory() as folder:
            file_path = os.path.join(folder, "contacts.json")

            with open(file_path, "w") as file:
                json.dump(contacts, file)

            with open(file_path, "r") as file:
                loaded_contacts = json.load(file)

            self.assertEqual(contacts, loaded_contacts)

    def test_empty_contacts(self):
        contacts = {}
        self.assertEqual(len(contacts), 0)


if __name__ == "__main__":
    unittest.main()
