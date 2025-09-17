def add_contact(contact_book):
    contact_name = input()
    contact_phone = input()
    contact_email = input()
    contact_address = input()

    if contact_name not in contact_book:
        contact_book = {
                contact_name: {
                    "phone": contact_phone,
                    "email": contact_email,
                    "address": contact_address
                }
        }
        print("Contact added successfully!")
    else:
        print("Contact already exists!")
    return contact_book