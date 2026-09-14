def count_words(text):
    split_texts = text.split()
    return len(split_texts)


def get_chars_dict(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(item):
    return item[1]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        sorted_list.append((char, count))

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
