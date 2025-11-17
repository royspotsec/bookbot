import sys
from stats import get_num_words
from stats import count_chars



print ("Usage: python3 main.py <path_to_book>")


user_path = (sys.argv[1])


def get_book_text (filepath) :
    with open(filepath) as file :
        string_file = file.read()
    print (string_file)


print (f"============ BOOKBOT ============")
print (f"Analyzing book found at {user_path}")
print (f"----------- Word Count ----------")
get_num_words (user_path)
print (f"--------- Character Count -------")
count_chars (user_path)


