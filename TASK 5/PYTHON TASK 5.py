class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, updated_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = updated_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            manager.search_contact(keyword)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            updated_contact = Contact(new_name, new_phone, new_email, new_address)
            manager.update_contact(name, updated_contact)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
