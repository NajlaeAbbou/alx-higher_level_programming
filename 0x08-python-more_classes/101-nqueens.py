#!/usr/bin/python3
"""
nqueens backtracking program
"""


from sys import argv

if __name__ == "__main__":
    ap = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    nu = int(argv[1])
    if nu < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(nu):
        ap.append([i, None])

    def already_exists(y):
        """check not already exist """
        for x in range(nu):
            if y == ap[x][1]:
                return True
        return False

    def reject(x, y):
        """reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(ap[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers"""
        for i in range(x, nu):
            ap[i][1] = None

    def nqueens(x):
        """recursive backtracking function"""
        for y in range(nu):
            clear_a(x)
            if reject(x, y):
                ap[x][1] = y
                if (x == nu - 1):
                    print(ap)
                else:
                    nqueens(x + 1)

    nqueens(0)
