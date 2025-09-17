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