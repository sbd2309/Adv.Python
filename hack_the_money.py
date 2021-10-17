def hackmoney(value):
    if value == 1:
        return  "Yes"
    elif value % 10 == 0:
        return "Yes"
    else:
        return "No"
n=int(input())
for i in range(0,n,1):
    print(hackmoney(int(input())))

