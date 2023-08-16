#!/usr/bin/python3
"""the function wrtie_file"""


def write_file(filename="", text=""):
    """returns the number of chars"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
