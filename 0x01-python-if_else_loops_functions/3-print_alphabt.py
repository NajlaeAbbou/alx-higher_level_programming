#!/usr/bin/python3
for i in range(97, 123):
    if format(chr(i)) == 'q' or format(chr(i)) == 'e':
        continue
    print(format(chr(i)), end="")

