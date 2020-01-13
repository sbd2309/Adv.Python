# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
l=[]
for i in range (0,n,1):
    l.append(input())
#print(l)
for i in l:
    #print(i)
    if '.' in i:
        try:
            x=float(i)
            if (type(x))==float:
                print ("True")
        except:
            #print(i)
            print("False")
    else:
        print("False")        
