#!/usr/bin/python3
"""adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.
    Args:
        obj (any): The object to add.
        att (str): The name of att.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
