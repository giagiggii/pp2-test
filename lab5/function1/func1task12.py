def histogram(inputes):
    for num in inputes:
        print('*' * num)

n=input()
num=list(map(int, n.split()))
histogram(num)
