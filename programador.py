sp, hp = [int(x) for x in input().split()]
sd, hd = [int(x) for x in input().split()]
progra = design = 0
for i in range(int(input())):
	h1, h2 = [int(x) for x in input().split()]
	if(h2 <= hd and h1 <= hp):
		progra += sp
		design += sd
print("Programador: R$", progra)
print("Designer: R$", design)