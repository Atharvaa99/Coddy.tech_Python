def delete_contact(contact_book):
    delete_name = input()
    
    if delete_name not in contact_book:
        print("Contact not found!")
    
    else:
        del contact_book[delete_name]
        print("Contact deleted successfully!")