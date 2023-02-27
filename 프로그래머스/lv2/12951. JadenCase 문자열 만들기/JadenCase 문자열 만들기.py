def solution(s):
    # aa = ' '.join(s.split())
    # man= aa.split(" ")
    # print(man)
    # for i in range(len(man)):
    #     if not man[i][0].isdigit():
    #         a=man[i][0].upper()
    #         b=man[i][1:].lower()
    #         final=a+b
    #         man[i]=final
    #     else:
    #         a=man[i][0]
    #         b=man[i][1:].lower()
    #         final=a+b
    #         man[i]=final
    # answer=" ".join(man)
    # return answer
    s=s.lower()
    if s[0].isalpha():
        a = s[0].upper()
        print(s[1:],'ss')
        s = a + s[1:].lower()
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i].isalpha() == True:
            a = s[i].upper()
            b = s[i + 1:].lower()
            s = s[:i] + a + b

    return s
