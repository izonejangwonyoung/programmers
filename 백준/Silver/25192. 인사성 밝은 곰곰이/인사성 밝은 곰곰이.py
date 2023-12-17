n = int(input())
s = []
emoziList = set()
count = 0
for i in range(n):
    value = input()
    s.append(value)
tmp_index = 0
for i in range(len(s)):
    if s[i] == "ENTER":
        tmp_index = i
        emoziList.clear()
    else:
        if s[i] in emoziList:
            count += 0
        else:
            count += 1
            emoziList.add(s[i])

print(count)
