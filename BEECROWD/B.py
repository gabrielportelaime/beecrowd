for i in range(int(input())):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    d = (y2*(x1**2) - y1*(x2**2))/(y2*x1 - y1*x2)
    print(d)