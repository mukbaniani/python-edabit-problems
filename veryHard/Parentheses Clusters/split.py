def split(txt):
    lst = []
    word = ""
    for i in txt:
        word += i
        if word.count("(") == word.count(")"):
            lst.append(word)
            word = ""
    return lst