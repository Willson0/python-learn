n = int(input("Введите число конечное число диапазона: "))
print("Простые числа:")

is_prime = [True] * (n + 1)

if n >= 0:
    is_prime[0] = False

if n >= 1:
    is_prime[1] = False

p = 2
while p * p <= n:
    if is_prime[p]:
        multiple = p * p
        while multiple <= n:
            is_prime[multiple] = False
            multiple += p
    p += 1

primes = []
number = 2

while number <= n:
    if is_prime[number]:
        primes.append(str(number))
    number += 1

print(" ".join(primes))
