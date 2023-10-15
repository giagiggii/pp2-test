def palinka(s):
    s1 = ''.join(s.split()).lower()
    return s1 == s1[::-1]

s=input()
result = palinka(s)
print(result)
