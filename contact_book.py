import json
import os
FILE_NAME = "contacts.json"
# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)
# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added!\n")
# View contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\nContact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()
# Search contact
def search_contact(contacts):
    query = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print("\nFound Contact:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found = True
    if not found:
        print("No contact found.\n")
# Update contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        num = int(input("Enter contact number to update: "))
        contact = contacts[num - 1]
        print("Leave blank to keep current value.")
        name = input(f"Name ({contact['name']}): ") or contact['name']
        phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
        email = input(f"Email ({contact['email']}): ") or contact['email']
        address = input(f"Address ({contact['address']}): ") or contact['address']
        contacts[num - 1] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        save_contacts(contacts)
        print("Contact updated!\n")
    except:
        print("Invalid input.\n")
# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        num = int(input("Enter contact number to delete: "))
        removed = contacts.pop(num - 1)
        save_contacts(contacts)
        print(f"Deleted: {removed['name']}\n")
    except:
        print("Invalid input.\n")
# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
if __name__ == "__main__":
    main()