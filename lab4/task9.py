a = int(input())
b=[]
for i in range(a):
    b.append(set())
    for j in range(int(input())):
        b[i].add(input())
s= set.intersection(*b)
s1= set.union(*b)
print(len(s), *sorted(s), sep='\n')
print(len(s1), *sorted(s1), sep='\n')