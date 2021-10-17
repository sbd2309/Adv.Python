l = [int(i) for i in input().strip().split(' ')]
i = 0
count = 0
x = 0
while i < len(l):
    jump = l[i]
    max = 0
    for j in range(i + 1, i + jump + 1, 1):
        if len(l) < i + jump:
            break
        if max < l[j]:
            max = l[j]
            #print("Max{} ".format(max))
            x = j
    i = x
    count += 1
    #print(i, count)
    if l[i] == len(l):
        break
    elif l[i] > len(l) - i:
        count += 1
        break

print(count)
