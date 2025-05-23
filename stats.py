import string

def count_words(content: str):
    words = content.split()
    num_words = len(words)
    print(num_words, "words found in the document")
    
    
def get_num_characters(content: str):
    low_content = content.lower()
    
    characters = {letter: low_content.count(letter) for letter in string.ascii_lowercase}
    
    return characters