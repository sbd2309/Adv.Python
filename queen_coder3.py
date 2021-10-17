l = [int(i) for i in input().strip().split(' ')]
l.append(-1)
sum = 0
max = 0
for i in range(0, len(l), 1):
    sum = 0
    sum = sum + l[i]
    #print(sum)
    x = l[i]
    if l[i] == -1:
        break
    for j in range(i + 1, len(l), 1):
        if x < l[j]:
            sum = sum + l[j]
            x = l[j]
            # print(sum)
        else:
            #print(sum)
            if max < sum:
                max = sum
                sum = l[i] + l[j]
                # print(sum)
                x = l[j]
print(max)
