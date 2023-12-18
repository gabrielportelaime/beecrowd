INF = 1000000

f, s, g, u, d = [int(x) for x in input().split()]

empurroes = 0
andar = s

if(andar < g and u > 0):
    empurroes = (g - andar)//u
    andar += empurroes*u
elif(andar < g):
    empurroes = INF
elif(d > 0):
    empurroes = (andar - g)//d
    andar -= empurroes*d
else:
    empurroes = INF

while(andar != g and empurroes < INF):
    empurroes += 1
    up, down = andar + u, andar - d
    if(up <= f and (andar < g or down < 1)):
        andar = up
    elif(down >= 1):
        andar = down
    else:
        empurroes = INF
if(empurroes < INF):
    print(empurroes)
else:
    print("use the stairs")
