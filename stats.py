def get_num_words (filepath) :
    count =0
    with open(filepath) as file :
        file_content = file.read()
        words = file_content.split()
        for word in words :
            count  +=1
    print (f"Found {count} total words")
    


def count_chars (filepath) :
    with open (filepath) as file:
        file_contents= file.read()
        words = file_contents.split()
        current = {}
        count_exist =0
        count_notexist =0
        for word in words :
            for charector in word :
                charector=charector.lower()
                if charector not in current :   
                    current[charector]=1
                else  :
                     current[charector]+=1
        current=dict(sorted(current.items(), key = lambda item:item[1] , reverse=True))
        for char,count in current.items() :
            print (f"{char}: {count}")                 
                    



                   
        
                
        
      
        

        
    