n = int(input())
x = 4


def power(n, x):
    if x == 0:
        return 1
    if x == 1:
        return n
    return n * power(n, x - 1)


result = power(n, x)

st = str(result)
if int(st[-1]) == n:
    print("Yes")
else:
    print("No")
