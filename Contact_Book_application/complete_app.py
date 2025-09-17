contact_book = {}

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")


def add_contact(contact_book):
    contact_name = input()
   

    if contact_name not in contact_book:
        contact_phone = input()
        contact_email = input()
        contact_address = input()
        contact_book[contact_name] = {
                    "phone": contact_phone,
                    "email": contact_email,
                    "address": contact_address
        }
        print("Contact added successfully!")
    else:
        print("Contact already exists!")

def view_contact(contact_book):
    view_name = input()

    if view_name in contact_book:
        view_phone = contact_book[view_name]["phone"]
        view_email = contact_book[view_name]["email"]
        view_address = contact_book[view_name]["address"]

        print(f"Name: {view_name}")
        print(f"Phone: {view_phone}")
        print(f"Email: {view_email}")
        print(f"Address: {view_address}")

    else:
        print("Contact not found!")

def edit_contact(contact_book):
    edit_name = input()
    if edit_name not in contact_book:
        print("Contact not found!")
    else: 
        edit_phone = input()
        edit_email = input()
        edit_address = input()  

        if edit_phone != '':
            contact_book[edit_name]["phone"] = edit_phone
        if edit_email != '':
            contact_book[edit_name]["email"] = edit_email
        if edit_address != '':
            contact_book[edit_name]["address"] = edit_address
        print("Contact updated successfully!")

def delete_contact(contact_book):
    delete_name = input()
    
    if delete_name not in contact_book:
        print("Contact not found")
    
    else:
        del contact_book[delete_name]
        print("Contact deleted successfully!")
    

def list_all_contacts(contact_book):

    if not contact_book:
        print("No contacts available.")
    
    else:
        for contacts in contact_book:
            display_name = contact_book[contacts]["phone"]
            display_email = contact_book[contacts]["email"]
            display_address = contact_book[contacts]["address"]

            print(f"Name: {contacts}")
            print(f"Phone: {display_name}")
            print(f"Email: {display_email}")
            print(f"Address: {display_address}")
            print()

while(True):
    display_menu()
    user_input = input()

    match user_input:
        case '1':
             add_contact(contact_book)
        case '2':
             view_contact(contact_book)
        case '3':
             edit_contact(contact_book)
        case '4':
             delete_contact(contact_book)
        case '5':
            list_all_contacts(contact_book)
        case '6':
            break
        case _:
            print("Invalid Input")