import sys

from stats import get_num_words, get_char_count, sort_on,get_letter_count

book_path = sys.argv
if len(book_path) != 2:
    print("Usage: python3 main.py <path_to_book>")

    sys.exit(1)
else:
    with open(book_path[1]) as f:
        file_content = f.read()



def get_book_text(file_path):
    print(file_path)




char_counts = get_letter_count(get_char_count(file_content))
char_counts.sort(reverse = True, key=sort_on)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path[1]}.")
print("----------- Word Count ----------")
word_count = get_num_words(file_content)
print("--------- Character Count -------")
for letter in char_counts:
    print(f"{letter['char']}: {letter['num']}")
print("============= END ================")





