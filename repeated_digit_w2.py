
def repeated_digit(n,n1):
    count =0
    for i in range(n,n1+1,1):
        flag=0
        l=[]
        while i!=0:
            r=i%10
            if r in l:
                flag =1
                break
            l.append(r)
            i=i//10
        if flag == 0:
            count +=1

    print(count)

n=int(input())
n1=int(input())

repeated_digit(n,n1)
