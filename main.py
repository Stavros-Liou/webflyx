import sys
from stats import count_words, count_chars,char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv)<2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    path = sys.argv[1]

    book_text=get_book_text(path)
    
    # Print the result
    
    
    
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

   

    char_dict=count_chars(book_text)
    char_list = char(char_dict)  # <-- This gets your sorted list from your function
    for entry in char_list:
     if entry["char"].isalpha():
        print(f"{entry['char']}: {entry['num']}")


if __name__ == "__main__":
    main()
