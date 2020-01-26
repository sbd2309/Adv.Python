n=float(input())
n1=int(input())
e=2.71828
def fact(n1):
    f=1
    for i in range(1,n1+1,1):
        f=f*i
    return f
m=pow(e,n1)*pow(e,-n)
print(m/fact(n1))
