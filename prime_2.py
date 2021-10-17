def check_prime(n):
    flag = 0

    for i in range(2, int(n/2)+1, 1):
        if n % i == 0:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        print("Prime")
    else:
        print("Not Prime")


n = int(input())
check_prime(n)
