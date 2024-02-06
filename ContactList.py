contacts = []

def addContact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    while len(phone)!=10 or phone.isnumeric()==False:
        print("Phone munbers must consist of 10 numbers")
        phone = input("Enter phone number: ")
    contact = {
        'name': name,
        'phone': phone,
    }
    contacts.append(contact)
    print("Contact added successfully!")

def viewContact():
    if not contacts:
        print("No contacts available.")
        return
    
    print("List of Contacts:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

def searchContact():
    searchTerm = input("Enter name or phone number to search: ")
    foundContact = []
    
    for contact in contacts:
        if searchTerm.lower() in (contact['name']).lower() or searchTerm in contact['phone']:
            foundContact.append(contact)
    
    if foundContact:
        print("Search Results:")
        for contact in foundContact:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No matching contacts found.")

    return foundContact

def updateContact():
    foundContact = searchContact()
    
    if foundContact:
        searchTerm = input("Enter exact name or phone number to be upated from the searched items: ")
        for contact in foundContact:
            if searchTerm.lower() in (contact['name']).lower() or searchTerm in contact['phone']:
                contact['name'] = input("Enter new name (press enter to keep current): ") or contact['name']
                newPhone = input("Enter new phone number (press enter to keep current): ") or contact['phone'] 
                while len(newPhone)!=10 or newPhone.isnumeric()==False:
                    print("Phone number must consist of 10 digits")
                    newPhone = input("Enter phone number: ")
                contact['phone'] = newPhone 
                print("Contact updated successfully!")
                return
    print("Enter valid name or phone number!")

def deleteContact():
    foundContact = searchContact()

    if foundContact:
        searchTerm = input("Enter exact name or phone number to be deleted: ")
        for contact in foundContact:
            if searchTerm.lower() in (contact['name']).lower() or searchTerm in contact['phone']:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                return
    print("Enter valid name")
        

#main function
while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            addContact()
        elif choice == '2':
            viewContact()
        elif choice == '3':
            searchContact()
        elif choice == '4':
            updateContact()
        elif choice == '5':
            deleteContact()
        elif choice == '6':
            print("Exiting Contacts!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")