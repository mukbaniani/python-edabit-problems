    Create a class with a couple of functions like these examples.

    magic.replace("string", 'char', char') is a function that replaces all of the specified characters with another characters.
    magic.str_length("string") is a function that returns the length of the string.
    magic.trim(" string ") is a function that returns a string that truncates spaces at both the beginning and end.
    magic.list_slice(list, tuple) is a function that returns the items in the list that are among the specified indexes. If the length of the new list is 0, return -1.

    Examples

    magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

    magic.str_length("hello world") ➞ 11

    magic.trim("      python is awesome      ") ➞ "python is awesome"

    magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]