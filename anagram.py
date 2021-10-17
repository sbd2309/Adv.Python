def anagram(s1, s2):
    if s1 == s2:
        print("Strings are same")
    elif len(s1) == len(s2):
        count = 0
        for i in range(0, len(s1), 1):
            if s1[i] in s2:
                count += 1
            else:
                break
        if count == len(s2):
            print("Anagram")
        else:
            print("Not Anagram")


s1 = input()
s2 = input()
anagram(s1, s2)
