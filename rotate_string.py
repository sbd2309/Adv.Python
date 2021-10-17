def rotatestring(n, r_by, r_to):
    if r_to == 'L':
        for i in range(0,r_by,1):
            s=''
            for j in range(1,len(n),1):
                s=s+n[j]
            s=s+n[0]
            n=s
        print(n)
    elif r_to=='R':
        for i in range(0,r_by,1):
            s=''
            s=s+n[-1]
            for j in range(0,len(n)-1,1):
                s=s+n[j]
            n=s
        print(n)

n = input()
r_by = int(input())
r_to = input()
rotatestring(n, r_by, r_to)
