dias = {0:0, 5:9, 6:9, 7:9, 8:10, 9:11, 10:16, 11:16, 12:16, 13:16, 14:16, 15:17, 
        16:18, 17:23, 18:23, 19:23, 20:23, 21:23, 22:24, 23:25, 24:30, 25:30, 26:30}

quantidade_dias = 30
total_ganho = 41

for i in range(30):
    for j in range(30):
        for k in range(30):
            if(i + j + k == quantidade_dias and (i > 4 and j > 4 and k > 4) and (i > 13 or j > 13 or k > 13) 
            and (dias[i] + dias[j] + dias[k] == total_ganho)):
                print(i, j, k, end=' - ')
                print(dias[i] + dias[j] + dias[k])
