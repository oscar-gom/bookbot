def get_book_text(path: str) -> str:
    with open (path) as f:
        return f.read()

def count_words(content: str):
    words = content.split()
    num_words = len(words)
    print(num_words, "words found in the document")

def main():
    count_words(get_book_text("books/frankenstein.txt"))
    
main()