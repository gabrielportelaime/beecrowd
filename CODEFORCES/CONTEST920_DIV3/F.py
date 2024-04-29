import sys
input = sys.stdin.readline
K = 200
def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    
    queries = [[] for _ in range(n + 1)]
    res = [0] * q
    for i in range(q):
        s, d, k = map(int, input().split())
        s -= 1
        queries[d].append((s, k, i))
    for d in range(min(K, n + 1)):
        if not queries[d]:
            continue
        P = [0] * (n + d)
        G = [0] * (n + d)
        for i, a in enumerate(A):
            j = i // d
            P[i + d] += a + P[i]
            G[i + d] += (j + 1) * a + G[i]
        for s, k, i in queries[d]:
            ns = s + (k - 1) * d
            res[i] = G[ns + d] - G[s] - (s // d) * (P[ns + d] - P[s])
    return " ".join(map(str, res))

T = int(input())
out = [solve() for _ in range(T)]
print("\n".join(map(str, out)))