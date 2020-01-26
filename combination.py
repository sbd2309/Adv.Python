from itertools import combinations_with_replacement
userinput=input()
stringinput=userinput.split(' ')[0]
value=userinput.strip().split(' ')[1]
combinedlist=list(combinations_with_replacement(stringinput,int(value)))
res=[]
for i in combinedlist:
    res.append(''.join(i))

print('\n'.join(sorted(res)))
