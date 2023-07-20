#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for valueR in list(a_dictionary.keys()):
        if value == a_dictionary.get(valueR):
            del a_dictionary[valueR]
    return (a_dictionary)
