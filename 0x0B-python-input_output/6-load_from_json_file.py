#!/usr/bin/python3
"""function load from json file"""

import json


def load_from_json_file(filename):
    """create and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
