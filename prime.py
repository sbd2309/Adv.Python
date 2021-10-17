'''
n=input().strip()
l=[int(i) for i in input().strip().split(' ')]
print (l)
'''

n = int(input())
n1 = int(input())


def operation(n, n1):
    s1 = ''
    count = 0
    flag = 1
    if n < n1:
        for i in range(n, n1 + 1, 1):
            s1 = str(i)
            for j in range(0, len(s1), 1):
                if s1[j] in s1[j + 1:]:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                count += 1

    print(count)


operation(n, n1)
