def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = input()
nums = list(map(int,n.split()))
primes = list(filter(lambda x: prime(x),nums))
print(primes)

