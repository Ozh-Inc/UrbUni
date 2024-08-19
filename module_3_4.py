def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


print(single_root_words('Count', 'Accounting', 'counter', 'rumble', 'ooga-booga', 'Viscount'))
