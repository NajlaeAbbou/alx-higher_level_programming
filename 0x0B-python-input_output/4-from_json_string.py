#!/usr/bin/python3
"""json string function"""

import json


def from_json_string(my_str):
    """returns an object JSON string"""
    return json.loads(my_str)
