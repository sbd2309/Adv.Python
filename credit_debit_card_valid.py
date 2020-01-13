class validator():
    def __init__(self):
        pass

    def check_valid(self,n):
        l=[]
        n=str(n)
        v=n[1]
        if len(n)!=16:
            print ("Invalid Card Number")
        else:
            count=0
            s=0
            for i in n:
                if count%2 == 0:
                    l.append(int(i))
                else:
                    s=s+int(i)
                count += 1
            #print (l)
            #print (s)
            l1=[]
            for i in l:
                l1.append(i * 2)
            #print(l1)
            l2=[]
            for i in l1:
                if i >= 10:
                    l2.append(int((i / 10)) + int((i % 10)))
                else:
                    l2.append(i)
            #print(l2)
            #print (sum(l2)+s)
            if (sum(l2)+s) % 10 ==0 :
                print ("Valid Card")
                if (int(l[0])==4):
                    print ("VISA CARD")
                elif int(l[0])==5 and int(v) >=1 and int(v)<=5:
                    print ("Master Card")
            else:
                print ("The card is invalid")

i_validator=validator()
i_validator.check_valid(int(input("Enter Your Card Number: ")))
