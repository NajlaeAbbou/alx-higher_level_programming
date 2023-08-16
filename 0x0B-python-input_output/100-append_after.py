#!/usr/bin/python3
"""append after function"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string"""
    with open(filename, 'r', encoding='utf-8') as f:
        l_list = []
        while True:
            l = f.readline()
            if l == "":
                break
            l_list.append(l)
            if search_string in l:
                l_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(l_list)
