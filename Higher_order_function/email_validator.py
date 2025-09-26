def helper_function(email):
    if email.count("@") != 1:
        return False
    
    at_index = email.find("@")
    return at_index > 0 and at_index < len(email) - 1


def clean_email_list(emails):
    to_lowercase = map(str.lower, emails)
    strip_whitespace = map(str.strip, to_lowercase)
    valid_emails = filter(helper_function, strip_whitespace)
    
    return list(valid_emails)
