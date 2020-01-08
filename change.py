class givechange():
    def __init__(self,pchange):
        self.pchange=pchange

    def calchange(self,chn):
        x=self.pchange
        pnote=pfhundred=phundred=pfifty=pten=0
        while chn>10:
            if self.pchange < chn:
                pnote=int(chn/self.pchange)
                chn=chn%self.pchange
            elif chn >=500:
                pfhundred=int(chn/500)
                chn=chn%500
            elif chn >=100:
                phundred=int(chn/100)
                chn=chn%100
            elif chn>=50:
                pfifty=int(chn/50)
                chn=chn%50
            elif chn>=10:
                pten=int(chn/10)
                chn=chn%10
            else:
                print ('Preferred chnage cannot be more than the Change itself!')
        print ('{} preferred notes , {} five hundred notes , {} hundred notes, {} fifty notes , {} ten rupee notes and {} coins'.format(pnote,pfhundred,phundred,pfifty,pten,chn))

i_givechnage=givechange(int(input("Enter Preferred Note: ")))
i_givechnage.calchange(int(input("Enter Chnage Required:")))