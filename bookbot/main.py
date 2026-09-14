import sys
from stats import chars_dict_to_sorted_list, count_words, get_chars_dict


def get_book_text(book_files):
    with open(book_files) as f:
        contents = f.read()
        return contents


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    result = get_book_text(path)

    num_words = count_words(result)
    char_counts = get_chars_dict(result)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print_report(path, num_words, sorted_chars)


main()
