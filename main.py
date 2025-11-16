from stats import get_num_words
from stats import count_chars


user_path = "books/frankenstein.txt"




        


def get_book_text (filepath) :
    with open(filepath) as file :
        string_file = file.read()
    print (string_file)
        
   



    
    
    
get_num_words (user_path)
count_chars (user_path)