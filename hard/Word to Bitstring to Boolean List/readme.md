Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

    Locate the position of the letter in the English alphabet (from 1 to 26).
    Odd positions will be represented as 1 and even positions will be represented as 0.
    Convert the represented positions to boolean values, 1 for True and 0 for False.
    Store the conversions into an array.

Examples

to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0

to_boolean_list("loves") ➞ [False, True, False, True, True]

to_boolean_list("tesh") ➞ [False, True, True, False]