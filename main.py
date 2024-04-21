def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text = to_lower(text)
    chars_dict = count_letters(text)
    num_words = get_num_words(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def to_lower(text):
    return text.lower()

def count_letters(text):
    count_dict = {}
    for char in text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(nums_chars_dict):
    sorted_list = []
    for ch in nums_chars_dict:
        sorted_list.append({"char": ch, "num": nums_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
