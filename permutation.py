from itertools import permutations
userinput=input()
l=userinput.strip().split(' ')[0]
value=userinput.strip().split(' ')[1]

permutatedlist=list(permutations(l,int(value)))

#print(permutatedlist.sort())
res=[]
for x in permutatedlist:
    res.append(''.join(x))
#print(res)
print('\n'.join(sorted(res)))


