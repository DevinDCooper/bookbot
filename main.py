from stats import get_num_words, get_char_count, sort_on,get_letter_count



with open("books/frankenstein.txt") as f:
    file_content = f.read()

def get_book_text(file_path):
    print(file_path)




char_counts = get_letter_count(get_char_count(file_content))
char_counts.sort(reverse = True, key=sort_on)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
word_count = get_num_words(file_content)
print("--------- Character Count -------")
for letter in char_counts:
    print(f"{letter['char']}: {letter['num']}")
print("============= END ================")





