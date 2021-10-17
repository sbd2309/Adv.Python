n = int(input())
l = []
while n != 6:
    if n == 1:
        i = int(input("Enter value of element"))
        l.insert(0, i)
    elif n == 2:
        i = int(input("Enter value of element"))
        l.append(i)
    elif n == 3:
        for i in l:
            print(i, end=" ")
    elif n == 4:
        print(f"{l[0]} deleted from beginning successfully.")
        del l[0]
    elif n == 5:
        print('{} deleted from end successfully.'.format(l[-1]))
        l.pop(-1)
    else:
        break
    n=int(input())
    print()