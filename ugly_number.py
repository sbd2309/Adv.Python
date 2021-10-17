def ugly_number(n):
    l = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    if n < 9:
        print(l[n])
    else:
        count = 11
        while len(l) < n:
            factors = []
            p_factors = []
            for i in range(2, int(count / 2) + 1, 1):
                if count % i == 0:
                    factors.append(i)
            for j in factors:
                flag = 0
                for k in range(2, int(j / 2) + 1, 1):
                    if j % k == 0:
                        flag = 1
                        break
                if flag == 0:
                    p_factors.append(j)
            if len(p_factors) == 3:
                if 5 in p_factors and 3 in p_factors and 2 in p_factors:
                    l.append(count)
            elif len(p_factors) == 2:
                if 3 in p_factors and 2 in p_factors or 2 in p_factors and 5 in p_factors or 3 in p_factors and 5 in p_factors:
                    l.append(count)
            elif len(p_factors) == 1:
                if 2 in p_factors or 3 in p_factors or 5 in p_factors:
                    l.append(count)
            count += 1
        print(l[-1])


n = int(input())
for i in range(0, n, 1):
    n1 = int(input())
    ugly_number(n1)
