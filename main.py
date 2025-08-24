import sys
from stats import get_word_count, unique_characters_count, return_sorted_dic_list


if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_to_file):
    """
    Reads the content of a file and returns it as a string.

    :param path_to_file: The path to the file to be read.
    :return: The content of the file as a string.
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    """
    Main function to execute the script.
    """
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    strint_length = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {strint_length} total words")
    print("--------- Character Count -------")
    charcters_count = unique_characters_count(book_text)
    soreted_dict_list = return_sorted_dic_list(charcters_count)
    for item in soreted_dict_list:
        print(item)


print(sys.argv)

if __name__ == "__main__":
    main()
