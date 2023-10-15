def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(all):
    return [num for num in all if prime(num)]

n=input()
num=list(map(int, n.split()))
result = filter_prime(num)
print(result)

