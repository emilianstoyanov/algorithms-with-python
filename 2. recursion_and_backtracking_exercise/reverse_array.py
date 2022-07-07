def rev(l):
    if len(l) == 0:
        return []
    return [l[-1]] + rev(l[:-1])


l = [int(x) for x in input().split(" ")]

r = rev(l)
print(' '.join(str(x) for x in r))

"""

1 2 3 4 5 6

6 5 4 3 2 1

"""
