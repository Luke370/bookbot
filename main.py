from stats import get_num_words
from stats import get_chars
from stats import sort_data
import sys

def main():
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")

    num_words = get_num_words(sys.argv[1])
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    chars = sort_data(sys.argv[1])
    for c in chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

