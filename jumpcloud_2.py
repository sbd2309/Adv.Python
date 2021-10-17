def jumplcloud2(l, y):
    energy = 100
    for i in range(0, len(l), y):
        if l[i] == 1:
            energy -= 3
            print(f"Value of Energy is {energy}")
        else:
            energy -= 1
            print(f"Value of Energy is {energy}")
    print(energy)


x, y = [int(i) for i in input().strip().split(' ')]
#l = [int[y] for y in input().strip().split(' ')]
l=[int(i) for i in input().strip().split(' ')]
jumplcloud2(l, y)
