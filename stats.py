def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    for character in text.lower():
        char_dict[character] = char_dict.get(character, 0) + 1
    return char_dict

def char(char_count):
    new_list=[]
    for char, count in char_count.items():
        new_list.append({"char": char, "num": count})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(d):
    return d["num"]
