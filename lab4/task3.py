a=set([int(i) for i in input().split()])
b=set([int(i) for i in input().split()])
c=(set(a&b))
c=list(c)
c.sort()
print(' '.join([str(i)for i in c]))