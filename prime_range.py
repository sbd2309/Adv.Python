def check_prime(n, n1):
    for i in range(n, n1 + 1, 1):
        flag = 0
        for j in range(2, int(i/2), 1):
            if i % j == 0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            print(i)


n = int(input())
n1 = int(input())

check_prime(n, n1)
