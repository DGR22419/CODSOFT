contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    
    for name, details in contacts.items():
        if search == name or search == details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
