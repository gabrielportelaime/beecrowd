import time

limite = 100000000

inicio = time.time()

binario = ""
binario += "1"*limite

fim = time.time()

print(fim - inicio)
