import math
def car_fare(r1,n,r2,x):
    t_h=math.ceil(x/60)
    if t_h > n:
        print(n*r1+(t_h-n)*r2)
    else:
        print(n*t_h)

r1=int(input())
n=int(input())
r2=int(input())
x=float(input())

car_fare(r1,n,r2,x)
