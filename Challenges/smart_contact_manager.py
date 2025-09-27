
def validation_helper_email(contact):
    email = contact.get('email', '')
    return "@" in email and "." in email and " " not in email

def validation_helper_num(contact):
    phone = contact.get('phone', '')
    phone_digits = ''.join(filter(str.isdigit, phone))
    return len(phone_digits) == 10

def organize_contacts(contact_list):
    seen_emails = set()
    seen_phones = set()
    organized_list = []

    for contact in contact_list:
        email = contact.get('email')
        if email:
            contact['email'] = email.lower()

        phone = contact.get('phone', '')
        phone_digits = ''.join(filter(str.isdigit, phone))

        if (
            validation_helper_email(contact) and
            len(phone_digits) == 10 and
            contact['email'] not in seen_emails and
            phone_digits not in seen_phones
        ):
            contact['phone'] = phone_digits
            organized_list.append(contact)
            seen_emails.add(contact['email'])
            seen_phones.add(phone_digits)

    return organized_list