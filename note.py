class note():
    def __init__(self):
        pass

    def calminnote(self,n):
        c_2k=0
        c_1k=0
        c_5k=0
        c_20k=0
        c_10k=0
        c_50k=0
        c_200k=0
        while n>0:
            if n//2000 >= 1:
                c_2k=c_2k+n//2000
                n=n%2000
            elif n//1000 >= 1:
                c_1k=c_1k+n//1000
                n=n%1000
            elif n//500 >=1:
                c_5k=c_5k+n//500
                n=n%500
            elif n//200>=1:
                c_20k=c_20k+n//200
                n=n%200
            elif n//100>=1:
                c_10k=c_10k+n//100
                n=n%100
            elif n//50>=1:
                c_50k=c_50k+n//50
                n=n%50
            elif n//20>=1:
                c_200k=c_200k+n//20
                n=n%20
        print("{} 2k note and {} thoushand notes and {} five hundred notes and {} two hundred notes and {} hundred notes and {} fifty notes and {} twenty rupee notes  ".format(c_2k,c_1k,c_5k,c_20k,c_10k,c_50k,c_200k))

n = int(input())
x = note()
x.calminnote(n)
