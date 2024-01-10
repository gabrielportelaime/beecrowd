limite = 10001

for i in range(1, limite):
    for j in range(i, limite):
        for k in range(j, limite):
            if((i*j + j*k + k*i)%(i*j*k) == 0):
                print(i, j, k)
print('Acabou!')