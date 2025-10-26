
def get_num_words(file_path):
    num_words = len(file_path.split())
    print(f'Found {num_words} total words')



def get_char_count(file_path):
    num_chars = file_path.split()
    char_count = {}
    for i in num_chars:
        for j in i.lower():
            if j in char_count:
                char_count[j] += 1
            else:
                char_count[j] =  + 1
    return char_count


def get_letter_count(char_counts):
    letter_count = []
    for key, value in char_counts.items():
        if key.isalpha():
            letter_count.append({"char": key, "num": value})
    return letter_count

def sort_on(items):
    return items["num"]



      
      
   
        
        

   
