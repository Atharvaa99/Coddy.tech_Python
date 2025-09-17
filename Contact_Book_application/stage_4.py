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
    
    return contact_book