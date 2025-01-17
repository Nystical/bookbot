def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    get_report(chars_dict)
    print("--- End report ---")
    

def sort_on(dict):
    return dict["num"]

def get_report(dict):
    chars_list = []
    for x in dict:
        if x.isalpha():
            chars_list.append({"name":x,"num":dict[x]})
    chars_list.sort(reverse=True, key=sort_on)
    
    for char in chars_list:
        print(f"The '{char["name"]}' character was found {char["num"]} times")

    return chars_list


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()