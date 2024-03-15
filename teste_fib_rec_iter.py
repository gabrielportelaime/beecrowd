import time
num_teste = 40
def fib (n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)
inicio = time.time()
print(fib(num_teste))
fim = time.time()
print(fim - inicio)
inicio = time.time()
fib1 = 0
fib2 = 1
for i in range(num_teste):
    aux = fib2
    fib2 += fib1
    fib1 = aux
print(fib2)
fim = time.time()
print(fim - inicio)