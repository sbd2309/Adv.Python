class spell_n():
    def __init__(self):
        pass

    def spell_number(self,n):
        if n<=99999 and n>0:
             l1=['zero','one','two','three','four','five','six','seven','eight','nine']
             l2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
             l3 = ['', '', '', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
             if n<10:
                 r=int(n%10)
                 print (r)
                 print (str(l1[r]).upper())
             elif n>=10 and n<=20:
                 r=int(n%10)
                 print (str(l2[r]).upper())
             elif n>20 and n<=99:
                q=int(n/10)
                r=int(n%10)
                print (l3[q],l1[r])
             elif n>99 and n<=99999:
                l4=[]
                tn=n
                print (n)
                while tn>0:
                    q = int(tn % 10)
                    l4.append(q)
                    tn=tn/10
                if len(l4)==3:
                    print ("{} hundred and {} {}".format(l1[l4[2]],l3[l4[1]],l1[l4[0]]))
                elif len(l4)==4:
                    print ("{} thoushand and {} hundred and {} {}".format(l1[l4[3]],l1[l4[2]],l3[l4[1]],l1[l4[0]]))
                elif len(l4)==5:
                    print("{} thoushand and {} hundred and {} {}".format(l3[l4[3]], l1[l4[2]], l3[l4[1]], l1[l4[0]]))




i_spell_n=spell_n()
i_spell_n.spell_number(int(input("Enter Integer: ")))
