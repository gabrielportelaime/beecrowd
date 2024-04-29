class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def coeficiente_angular(a, b):
    if(a.y != b.y):
        alfa = (b.x-a.x)/(a.y-b.y)
    else:
        alfa = 0
    return alfa

def coeficiente_linear(a, b):
    if(a.y != b.y):
        beta = (1/2)*(a.y+b.y+ (a.x+b.x)*((b.x-a.x)/(b.y-a.y)))
    else:
        beta = 0
    return beta

for i in range(int(input())):
    estrelas = []
    for j in range(4):
        x, y = [float(x) for x in input().split()]
        estrelas.append(Ponto(x, y))
    ma = coeficiente_angular(estrelas[0], estrelas[2])
    ba = coeficiente_linear(estrelas[0], estrelas[2])
    mn = coeficiente_angular(estrelas[1], estrelas[3])
    bn = coeficiente_linear(estrelas[1], estrelas[3])
    if(ma == 0):
        x = (estrelas[0].x + estrelas[2].x)/2
        y = mn*x+bn
    elif(mn == 0):
        x = (estrelas[1].x + estrelas[3].x)/2
        y = ma*x+ba
    else:
        x = (bn - ba)/(ma - mn)
        y = (ma*bn - mn*ba)/(ma - mn)
    print(f"Caso #{i+1}: {x:.2f} {y:.2f}")