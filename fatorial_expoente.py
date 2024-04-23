# QUEM É MAIOR

def fatorial(n):
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

print(50**99)
print(fatorial(99))
print(50**99 > fatorial(99))
