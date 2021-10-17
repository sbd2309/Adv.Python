z = int(input())
n = int(input())
l = []
d = {}
for i in range(0, n, 1):
    temp = [str(i) for i in input().strip().split(' ')]
    l.append(temp)
for i in l:
    d[i[0]] = i[1]
# max=0
value = ''
for i in range(0, z, 1):
    max = 0
    for x, y in d.items():
        if max < int(y):
            max = int(y)
            value = x
    d.pop(value)
d.update(a=4)
print(d)
print(value)
