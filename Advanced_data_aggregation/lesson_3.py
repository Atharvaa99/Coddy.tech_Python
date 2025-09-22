numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

ascending_numbers_sort = sorted(numbers)
descending_numbers_sort = sorted(numbers,reverse = True)
alphabetical_sort = sorted(words)
word_length_sort = sorted(words, key = len)

print(f"Ascending: {ascending_numbers_sort}")
print(f"Descending: {descending_numbers_sort}")
print(f"Alphabetical: {alphabetical_sort}")
print(f"By Length: {word_length_sort}")