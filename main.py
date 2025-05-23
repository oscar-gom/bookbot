from stats import get_num_characters, count_words

def get_book_text(path: str) -> str:
    with open (path) as f:
        return f.read()


def main():
    count_words(get_book_text("books/frankenstein.txt"))
    dictionary = get_num_characters(get_book_text("books/frankenstein.txt"))
    print(dictionary)
    
main()