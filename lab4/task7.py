n = int(input())
a= set(range(1, n + 1))
b = a
while True:
    n1 = input()
    if n1 == 'HELP':
        break
    n1 = {int(x) for x in n1.split()}
    c = input()
    if c == 'YES':
        b &= n1
    else:
        b&= a-n1

print(' '.join([str(x) for x in sorted(b)]))