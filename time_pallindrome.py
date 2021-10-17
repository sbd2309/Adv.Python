def time_pallindrome(n):
    x = 0
    s1 = ''
    s2 = ''
    for i in n:
        if i == ':':
            x = 1
        elif x == 0:
            s1 = s1 + i
        elif x == 1:
            s2 = s2 + i
    n2 = int(s2)
    while True:
        xy = str(n2)
        yx = xy[::-1]
        if s1 == yx:
            print(n2-int(s2))
            break
        else:
            n2 = n2 + 1
n = input()
time_pallindrome(n)
