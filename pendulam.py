class pendulum():
    def __init__(self):
        pass

    def do_psort(self, l):
        l.sort()
        for i in range(len(l)-2,0,-2):
            print(l[i],end=" ")
        print(l[0],end=" ")
        for i in range(2,len(l),+2):
            print(l[i],end=" ")





n = int(input())
l = [int(i) for i in input().strip().split(' ')]
pen=pendulum()
pen.do_psort(l)