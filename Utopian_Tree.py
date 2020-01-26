n=int(input())
for i in range(0,n,1):
    cycle=int(input())
    height=0
    for j in range(0,cycle+1,1):
        if j%2==0:
            height+=1
        else:
            height=height*2
    print(height)
