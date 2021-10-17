def r_b(n):
    st = []

    for i in n:
        if i == ')':
            top = st[-1]
            st.pop()
            flag = 1
            while top != "(":
                if top == "+" or top == "-" or top == "*" or top == "/":
                    flag = 0
                top = st[-1]
                st.pop()
            if flag == 1:
                return 1
        else:
            st.append(i)
    return 0


n = input()
x=r_b(n)
if x == 1:
    print("Yes")
else:
    print("No")
