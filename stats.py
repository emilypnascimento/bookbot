def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(content):
    chars_low = content.lower()
    letters = {}
    for c in chars_low:
        if c in letters:
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1
    return letters

def sorted_list(char_count):
    char_count_list = []
    for letter, count in char_count.items():
        char_dict = { "char": letter, "num": count}
        char_count_list.append(char_dict)
    char_count_list.sort(reverse=True, key=sort_helper)
    return char_count_list

def sort_helper(item):
    return item["num"]
    
