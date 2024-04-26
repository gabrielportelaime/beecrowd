def primo (numero):
    if(numero == 2):
        return True
    if(numero == 1 or numero == 0 or numero%2 == 0):
        return False
    for i in range(3, int((numero)**(1/2)) + 1, 2):
        if(numero%i == 0):
            return False
    return True