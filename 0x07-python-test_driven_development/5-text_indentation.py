#!/usr/bin/python3
"""
indentation module
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these character"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for l in text:
        if x == 0:
            if l == ' ':
                continue
            else:
                x = 1
        if x == 1:
            if l == '?' or l == '.' or l == ':':
                print(l)
                print()
                x = 0
            else:
                print(l, end="")
