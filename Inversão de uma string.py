tam_string, a, b = [int(x) for x in input().split()]
minha_string = input()
print(minha_string[0:a-1] + minha_string[a-1:b][::-1] + minha_string[b::])
