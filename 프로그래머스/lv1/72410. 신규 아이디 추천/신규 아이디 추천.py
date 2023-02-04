import re


def removepoint(value):
    value = re.sub(r"^[.]|[.]$", '', value)  # 여러 번 반복해줘야하는 부분인가??
    return value


def solution(new_id):
    value = new_id
    value = value.lower()
    print(value)
    value = re.sub(r"[^a-z0-9\-_.]", '', value)
    print(value)
    value = re.sub(r"\.+", '.', value)
    value = re.sub(r"^[.]|[.]$", '', value)  # 여러 번 반복해줘야하는 부분인가??
    if len(value) == 0:
        value = 'a'
        print()
        value=re.sub(r"^[.]|[.]$",'',value)
    if len(value) >= 16:
        print('check1')
        value = value[0:15]
        value=re.sub(r"^[.]|[.]$",'',value)
    if len(value) <= 2:
        print('check2')
        temp = 3 - len(value)
        print(temp)
        value=re.sub(r"^[.]|[.]$",'',value)
        a = value[-1]
        for i in range(temp):
            value = value + a

    value = re.sub(r"^[.]|[.]$", '', value)
    return value

