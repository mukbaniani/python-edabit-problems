def fauna_number(txt):
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
    lst = txt.replace(',', ' ').replace('.', '').replace("and", "").split()
    filter = [(lst[lst.index(i) + 1], i) for i in lst if i.isnumeric() and lst[lst.index(i) + 1] in animals]
    return filter