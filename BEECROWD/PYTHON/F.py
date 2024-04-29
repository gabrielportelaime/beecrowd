for i in range(int(input())):
    x, y, v, t = [int(x) for x in input().split()]
    if((x**2+y**2)**(1/2) > v*t):
        print("NO")
    else:
        print("YES")