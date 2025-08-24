def get_word_count(text):
    """
    Counts the number of words in a given text.

    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    return len(text.split())


def unique_characters_count(text):
    """
    Counts the number of unique characters in a given text.

    :param text: The text to count unique characters in.
    :return: The number of unique characters in the text.
    """
    unique_characters_count = {}
    text = text.lower()
    # remove the whitespace characters
    text = "".join(text.split())
    for char in text:
        if char not in unique_characters_count:
            unique_characters_count[char] = 1
        else:
            unique_characters_count[char] += 1

    return unique_characters_count


def return_sorted_dic_list(char_counts):
    def get_count(item):
        return item[1]

    items_list = list(char_counts.items())

    items_list.sort(key=get_count, reverse=True)

    result = []
    for char, count in items_list:
        if char.isalpha():
            result.append(f'{char}: {count}')

    return result
