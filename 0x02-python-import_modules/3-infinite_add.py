#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    s = 0
    l = len(sys.argv) - 1
    for i in range(l):
        s+= int(sys.argv[i + 1])
    print("{:d}".format(s))
