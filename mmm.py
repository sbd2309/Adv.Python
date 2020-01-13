# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=int(input())
# mylist=[]
# for i in range(1,n+1,1):
# mylist = list(map(int, input("Enter 5 numbers: ").split()))[2]
# print(mylist)

#n = int(input("Enter N: "))
#l = []
#for i in range(1, n + 1, 1):
    #l.append(int(input("Enter Any Integer: ")))

n = int(input().strip())

l = [int(i) for i in input().strip().split(' ')]

l.sort()
x = int(len(l) / 2)
# print (x)
print(sum(l) / n)
# print(l[x],l[x-1])
print((l[x] + l[x - 1]) / 2)

uniq_list = []
for i in l:
    if i not in uniq_list:
        uniq_list.append(i)

#print(uniq_list)

count = 0
d = {}
for i in uniq_list:
    for j in l:
        if j == i:
            count += 1
    d.update({i: count})
    count = 0
#print (d)
# print (d)
x=0
for key, value in d.items():
    if value>x:
        x=value
#print (x)
for key , value in d.items():
    if x==value:
        print (key)
        break

