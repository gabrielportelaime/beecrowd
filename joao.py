for i in range(int(input())):
    n = int(input())
    cnt = [0]*(n+1)
    mx = [0]*(n+1)
    saltos = [int(x) for x in input().split()]
    for salto in saltos:
        if(salto <= n):
            cnt[salto] += 1
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            mx[j] += cnt[i]
    print(max(mx))