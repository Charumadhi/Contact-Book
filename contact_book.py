# Define an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, \nPhone: {info['phone']}, \nAddress: {info['address']}")
            print("-------------------------")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in [name, info['phone']]:
            print(f"Name: {name}, \nPhone: {info['phone']}, \nEmail: {info['email']}, \nAddress: {info['address']}")
            print("-------------------------")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current)")
        phone = input(f"Enter new phone number for {name} (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email for {name} (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address for {name} (current: {contacts[name]['address']}): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# User interface
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

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
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
