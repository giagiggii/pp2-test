n,k = [int(i) for i in input().split()]
a = set()
b = [[int(i) for i in input().split()] for j in range(k)]
for i in range(k):
    d= b[i][0]
    s1= b[i][0]
    s2 =b[i][1]
    while d <= n:
        if d% 7 != 0 and d% 7 != 6:
            a.add(d)
        d+=s2
print(len(a))