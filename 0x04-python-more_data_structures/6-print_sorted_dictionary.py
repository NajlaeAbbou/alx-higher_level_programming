#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ele = sorted(a_dictionary.keys())
    for i in ele:
        print("{:s}: {}".format(i, a_dictionary[i]))
