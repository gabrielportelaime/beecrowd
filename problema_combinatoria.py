contador = 0
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            if(i + j + k == 120 and i != j and i != k and j != k):
                print(i, j, k)
                contador += 1
print(contador)