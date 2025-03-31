def count_words (filepath):
    with open(filepath) as file:
        content = file.read()
        words = content.split()
        return (len(words))
print (f"{count_words("./books/frankenstein.txt")} words found in the document")

def count_characters(filepath):
    with open(filepath) as file:
        content = file.read()
        lowercase = content.lower()
    frenquency = {}
    for char in lowercase:
        frenquency[char] = frenquency.get(char, 0) +1
    print(frenquency)

#def sorted_list (dictionary):
#    dictionary = count_characters("./books/frankenstein.txt")

   # dictionary.sort(key=None)
#    print (dictionary)
#print(f"{sorted_list("./books/frankenstein.txt")}")


