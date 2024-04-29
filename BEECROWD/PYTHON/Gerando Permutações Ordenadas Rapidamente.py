import os, sys, io

input = lambda: sys.stdin.readline()[:-1]

def imprimir(texto, end="\n"):
    sys.stdout.write(str(texto) + end)

def permute_unique_string(s):
    def backtrack(path, used):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        
        for i in range(len(s)):
            if used[i] or (i > 0 and s[i] == s[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(s[i])
            backtrack(path, used)
            used[i] = False
            path.pop()
    s = sorted(s)
    result = []
    used = [False] * len(s)
    backtrack([], used)
    return result

for i in range(int(input())):
    imprimir('\n'.join(permute_unique_string(input())), end='\n\n')