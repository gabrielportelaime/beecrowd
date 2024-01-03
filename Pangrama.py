def remove(entrada):
    string = ""
    for i in range(len(entrada)):
        if(entrada[i] not in string):
            string += entrada[i]
    return string
al = ''.join(sorted(list(remove(input().replace(',', '').replace(':', '').replace(' ', '')))))
print(al)
if(al == "abcdefghijlmnopqrstuvxz"):
    print('S')
else:
    print('N')