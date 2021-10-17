def balanced_brackets(n):
    res = ''
    if len(n) == 2:
        if n[0] == '(' and n[1] == ')' or n[0] == '[' and n[1] == ']' or n[0] == '{' and n[1] == '}':
            print("Balanced")
            exit()
        else:
            print("Not Balanced")
            exit()
    for i in range(0, len(n), 1):
        temp = ''
        flag = 0
        if n[i] == '{':
            for j in range(i + 1, len(n), 1):
                if n[j] == '}':
                    flag = 1
                    break
                else:
                    temp = temp + n[j]
        elif n[i] == '[':
            for j in range(i + 1, len(n), 1):
                if n[j] == ']':
                    flag = 1
                    break
                else:
                    temp = temp + n[j]
        elif n[i] == '(':
            for j in range(i + 1, len(n), 1):
                if n[j] == ')':
                    flag = 1
                    break
                else:
                    temp = temp + n[j]
        # print(temp)
        if flag == 1:
            if len(temp)==0:
                res="Balanced"
            for k in range(0, len(temp), 1):
                if temp[k] == '{':
                    if '}' in temp:
                        res = "Balanced"
                        break
                elif temp[k] == '[':
                    if ']' in temp:
                        res = "Balanced"
                        break
                elif temp[k] == '(':
                    if ')' in temp:
                        res = "Balanced"
                        break
                else:
                    res="Not Balanced"
                    break

    print(res)


n = input()
balanced_brackets(n)
