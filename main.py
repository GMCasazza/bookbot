from stats import count_words
from stats import count_characters
from stats import sorted_list
import sys
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
word_count = count_words(sys.argv[1])
char_counts = count_characters(sys.argv[1])
sorted_chars = sorted_list(char_counts)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["count"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")
