from stats import get_num_words
from stats import get_chars
from stats import sort_data

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")

    num_words = get_num_words("./books/frankenstein.txt")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    chars = sort_data("./books/frankenstein.txt")
    for c in chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()