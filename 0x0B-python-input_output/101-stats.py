#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for l in sys.stdin:
        tok = l.split()
        if len(tok) >= 2:
            j = i
            if tok[-2] in status_tally:
                status_tally[tok[-2]] += 1
                i += 1
            try:
                file_size += int(tok[-1])
                if j == i:
                    i += 1
            except FileNotFoundError:
                if j == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
