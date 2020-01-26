for _ in range(int(input().strip())):
    n,m,s = map(int, input().strip().split(" "))
    print(((s-2+m)%n)+1)