quantidade = int(input())
al = ''.join(sorted(list(input().replace(',', '').replace('.', '').replace(' ', ''))))
bl = ''.join(sorted(list(input().replace(',', '').replace('.', '').replace(' ', ''))))
if(al == bl):
    print('S')
else:
    print('N')