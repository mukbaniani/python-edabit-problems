from re import search


def security(txt):
    return "ALARM!" if search(r"Tx*[$]", txt) or search(r"[$]x*T", txt) else "Safe"
    