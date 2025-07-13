def get_book_text(path):
    with open(path) as p:
        text = p.read()
    return text

def get_num_words(path):
    text = get_book_text(path)
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars(path):
    text = get_book_text(path).lower()
    chars = {}
    for t in text:
        if t not in chars:
            chars[t] = 1
        else:
            chars[t] += 1
    
    return chars


