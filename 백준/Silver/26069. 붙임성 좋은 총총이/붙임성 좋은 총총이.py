n = int(input())
s = set()
for _ in range(n):
    a, b = input().split()
    if (a == "ChongChong" or b == "ChongChong") or (a in s or b in s):
        # Your code here
        # print(a,b)
        s.add(a)
        s.add(b)
print(len(s))
