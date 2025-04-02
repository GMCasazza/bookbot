def count_words (filepath):
    with open(filepath) as file:
        content = file.read()
        words = content.split()
        return (len(words))
#print (f"{count_words("./books/frankenstein.txt")} words found in the document")

def count_characters(filepath):
    with open(filepath) as file:
        content = file.read()
        lowercase = content.lower()
    frenquency = {}
    for char in lowercase:
        frenquency[char] = frenquency.get(char, 0) +1
    return(frenquency)


def sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    
    def sort_on(dict):
        return dict["count"]
    
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

