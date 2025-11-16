
user_path = "books/frankenstein.txt"






def get_book_text (filepath) :
    with open(filepath) as file :
        string_file = file.read()
    print (string_file)
        
   


def main ():
    get_book_text(user_path)
    
    
    

main ()