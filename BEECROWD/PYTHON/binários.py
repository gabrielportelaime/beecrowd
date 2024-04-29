from itertools import combinations
from collections import deque
import random
import time


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def isPrime(n, k=5):
    if n == 1:
        return True
    if n < 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        if miillerTest(d, n) == False:
            return False
    return True


def mdc(n, m):
    anterior = n
    atual = m
    resto = anterior % atual
    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual
    return atual


def all_numbers(numbers):
    result = set()
    for i in range(1, len(numbers) + 1):
        for combination in combinations(numbers, i):
            prod = 1
            for number in combination:
                prod *= number
            result.add(prod)
    return result


def isPrimo(numero):
    if numero == 1:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** (1 / 2)) + 1, 2):
        if numero % i == 0:
            return False
    return True


def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def PollardRho(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2
    x = random.randint(0, 2) % (n - 2)
    y = x
    c = random.randint(0, 1) % (n - 1)
    d = 1
    while d == 1:
        x = (modular_pow(x, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        d = mdc(int(abs(x - y)), int(n))
        if d == n:
            return PollardRho(n)
    return d


inicio = time.time()

numeros = []


def generate(n):
    q = deque()
    q.append("1")
    for _ in range(n):
        front = str(q.popleft())
        q.append(front + "0")
        q.append(front + "1")
        numeros.append(int(front))


generate(4096)

print(numeros)

divisores = {}

for binario in numeros:
    primos = []
    n = binario
    while not isPrime(n):
        primo = PollardRho(n)
        primos.append(primo)
        n = n // primo
    primos.append(n)
    div_num = list(all_numbers(primos))
    divisores[binario] = div_num

final = time.time()
print(final - inicio)

while True:
    try:
        numero = int(input())
        valida = True
        for binario in divisores.keys():
            if numero in divisores[binario]:
                print(binario)
                valida = False
                break
        if valida:
            print("-1")
    except EOFError:
        break
