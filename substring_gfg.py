n = input()

class sub():
    def __init__(self):
        pass

    def subs(self, n):
        l = []
        st = ''
        max = 0
        for i in range(0, len(n), 1):
            if n[i] in st:
                if max < len(st):
                    max = len(st)
                l.append(st)
                st = ''
            else:
                st = st + n[i]
        for i in range(0, len(n), 1):
            if n[i] in st:
                if max < len(st):
                    max = len(st)
                if st not in l:
                    l.append(st)
                st = ''+n[i]
            else:
                st = st + n[i]
        print(max)
        for i in l:
            if len(i) == max:
                print(i, end=" ")


x = sub()
x.subs(n)
