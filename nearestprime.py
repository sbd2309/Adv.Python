def nearest_prime(n):
    gen=n
    while True:
        flag=0
        for i in range(2,int(gen/2),1):
            if gen%i == 0:
                flag=1
                break
        if flag == 0:
            #print(f"{gen} is upper prime")
            upper=gen
            break
        gen+=1
    gen=n
    while True:
        flag=0
        for i in range(2,int(gen/2),1):
            if gen%i == 0:
                flag=1
                break
        if flag == 0:
            #print(f"{gen} is Lower prime")
            lower=gen
            break
        gen-=1
    if n-lower < upper-n or n-lower == upper-n:
        print(lower)
    else:
        print(upper)

n=int(input())
for i in range(0,n,1):
    nearest_prime(int(input()))

