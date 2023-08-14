#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """a subclass"""
    def __init__(self):
        """init  object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
