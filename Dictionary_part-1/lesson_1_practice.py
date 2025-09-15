def create_book_dict(title,author,year):
    book_dict = {
            "title": title,
            "author": author,
            "year": year
    }
    return book_dict
print(create_book_dict("To Kill a Mockingbird", "Harper Lee", 1960))