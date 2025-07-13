def get_book_text(path):
    with open(path) as p:
        text = p.read()
    return text

def word_counter(path):
    text = get_book_text(path)
    words = text.split()
    num_words = len(words)
    return num_words


def main():
    num_words = word_counter("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()