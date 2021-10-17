def operation(n):
    if n=='+':
        r=int(input())
        c=int(input())
        matrix1=[]
        for i in range(0,r,1):
            a=[]
            for j in range(0,c,1):
                a.append(int(input()))
            matrix1.append(a)
        matrix2=[[int(input()) for i in range (c)] for j in range(r)]

        sum_matrix=[]
        for i in range(0,c,1):
            for j in range(0,c,1):
                sum_matrix.append(matrix1[i][j]+matrix2[i][j])

        for i in range(0,r,1):
            for j in range(0,c,1):
                print(s)
            

n=input()
operation(n)
