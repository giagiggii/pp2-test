n=int(input())
h=n//60
while(h>23):
  h=h-24
print(h,n%60)