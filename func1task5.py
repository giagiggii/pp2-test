def perm(s, s1=''):
    if not s:
        print(s1)
    else:
        for i in range(len(s)):
            lett = s[:i] + s[i+1:]
            perm(lett, s1 + s[i])

s=input()
perm(s)