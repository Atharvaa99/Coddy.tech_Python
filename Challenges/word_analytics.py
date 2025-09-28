import string

def analyze_text(text):
    split_text = text.split(" ")
    cleaned = ["".join(ch for ch in word if ch not in string.punctuation) for word in split_text]
    lowercase = map(lambda x: x.lower(),cleaned)
    word_dict = {}
    for word in lowercase:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    unique_count = len(word_dict)
    repeated = sorted([word for word,count in word_dict.items() if count > 1])
    palindrome = sorted([word for word in word_dict if word == word[::-1]])
    results = {
        "unique_count": unique_count,
        "repeated_words": repeated,
        "palindromes": palindrome
    }
    return results