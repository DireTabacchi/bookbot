def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_chars(book_text)
    print_report(book_path, num_words, char_count)

def count_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_chars(text):
    char_counts = {}
    for c in text.lower():
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1
    return char_counts


def sort_on_count(char_list):
    return char_list["count"]


def chars_dict_to_sorted_list(chars_dict):
    char_list = []
    for c in chars_dict:
        if c.isalpha():
            char_list.append({"letter": c, "count": chars_dict[c]})
    char_list.sort(key=sort_on_count, reverse=True)
    return char_list


def print_report(path, word_count, char_count):
    char_list = chars_dict_to_sorted_list(char_count)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for c in char_list:
        print(f"The '{c['letter']}' character was found {c['count']} times")
    print("--- End report ---")

main()
