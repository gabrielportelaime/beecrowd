v = [0] * 14

def inicializa_vetor():
    v[4] = 1
    v[5] = 2
    v[6] = 3
    v[7] = 4
    v[12] = 5
    v[11] = 6
    v[13] = 7
    v[1] = 8
    v[2] = 9
    v[3] = 10


numjogos = 0
p1 = 0
p2 = 0
c = [[0] * 3 for _ in range(2)]

inicializa_vetor()

numjogos = int(input())

for _ in range(numjogos):
    pp1 = 0
    pp2 = 0
    c[0][0], c[0][1], c[0][2], c[1][0], c[1][1], c[1][2] = map(int, input().split())
    
    if v[c[0][0]] >= v[c[1][0]]:
        pp1 += 1
    else:
        pp2 += 1
    
    if v[c[0][1]] >= v[c[1][1]]:
        pp1 += 1
    else:
        pp2 += 1
    
    if v[c[0][2]] >= v[c[1][2]]:
        pp1 += 1
    else:
        pp2 += 1
    
    if pp1 > pp2:
        p1 += 1
    else:
        p2 += 1

print(f"{p1} {p2}")
