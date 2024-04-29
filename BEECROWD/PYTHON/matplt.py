#importando biblioteca numpy
import numpy as np
#importando biblioteca matplotlib
import matplotlib.pyplot as plt

# Definindo conjunto de 1000 valores de x entre 0 e 3
x = np.linspace(0,3,1000)
# definindo vetor y nas mesmas dimensões que o vetor x
y = np.array(x.shape)
#definindo y, ou seja, aplicando x na função f(x) = x^3 - 2x^2 + 7
y = x*x*x - 2*x*x + 7

#tamanho da figura
plt.figure(figsize = (10,6))
#define X, Y, tipo de marcador(nenhum nesse caso) e cor
plt.plot(x,y, marker = '', color = 'green')     
#define título
plt.title('Gráfico f(x)')
#define nome a mostrar no eixo x
plt.xlabel('Eixo x')
#define nome a mostrar no eixo y
plt.ylabel('Eixo y')
#faz a plotagem
plt.show()