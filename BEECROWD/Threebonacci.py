respostas = []
fibo = [1, 1]

while(len(respostas) < 60):
    fibo.append(fibo[-1] + fibo[-2])
    if(fibo[-1]%3 == 0 or '3' in list(str(fibo[-1]))):
        respostas.append(fibo[-1])

while(True):
    try:
        print(respostas[int(input())-1])
    except EOFError:
        break