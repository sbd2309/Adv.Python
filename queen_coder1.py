s1, s2 = (str(i) for i in input().strip().split(' '))
diff = len(s1) - len(s2)
l = list(s1)
s3=s2
s2 = 'x' * diff + s2
print(s2)
count = 0
if diff > 0:
    for i in range(0, len(s1), 1):
        if s1[i] == s2[i]:
            continue
        elif s1[i] in s2:
            continue
        else:
            count += 1
        for i in range(0, len(s3), 1):
            if s3[i] not in s1:
                count += 1
else:
    for i in range(0, len(s1), 1):
        if s1[i] == s2[i]:
            continue
        elif s1[i] in s2:
            continue
        else:
            count += 1

print(count)
