n=int(input().strip())
if n<=1917 and n>=1700:
    if n%4==0:
        print("12.09.{}".format(n))
    else:
        print("13.09.{}".format(n))
else:
    if (n % 400==0) or (n % 4 ==0 and n % 100 !=0):
        print("12.09.{}".format(n))
    else:
        print("13.09.{}".format(n))