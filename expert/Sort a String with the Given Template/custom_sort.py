def custom_sort(t, s):
    r = ''
    for word in t:
        if word in s:
            r += word * s.count(word)
    r += ''.join(sorted(filter(lambda x: x not in t, s)))
    return r
