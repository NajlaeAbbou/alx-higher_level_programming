#!/usr/bin/python3
"""
indentation module
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these character"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for let in text:
        if x == 0:
            if let == ' ':
                continue
            else:
                x = 1
        if x == 1:
            if let == '?' or let == '.' or let == ':':
                print(let)
                print()
                x = 0
            else:
                print(let, end="")
