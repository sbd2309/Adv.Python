n = input()


def r_rotate(n):
    rrotate = ''
    for i in range(1, len(n), 1):
        rrotate = rrotate + n[i]
    rrotate = rrotate + n[0]
    return rrotate


def l_rotate(n):
    lrotate = n[-1]
    for i in range(0, len(n) - 1, 1):
        lrotate = lrotate + n[i]
    return lrotate


if l_rotate(n) == r_rotate(n):
    print(1)
else:
    print(0)
