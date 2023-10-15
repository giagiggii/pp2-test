def tiposet(n):
    n1 = []
    for i in n:
        if i not in n1:
            n1.append(i)
    return n1

n=input()
num=list(map(int, n.split()))
result = tiposet(num)
print(result)  
