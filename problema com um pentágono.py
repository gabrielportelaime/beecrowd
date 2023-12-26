while(True):
    try:
        valor = float(input())
        resultado = 1.067395681711181*(valor)
        print(f"{resultado:.10f}")
    except EOFError:
        break