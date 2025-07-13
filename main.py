from stats import get_num_words
from stats import get_chars

def main():
    num_words = get_num_words("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")
    chars = get_chars("./books/frankenstein.txt")
    print(chars)

main()