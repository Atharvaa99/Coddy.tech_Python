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