import math

def intersecao(rectangle_bottom_left, circle_center, circle_radius):
    
    if (rectangle_bottom_left[0] <= circle_center[0] <= rectangle_bottom_left[0] + rectangle_width and
        rectangle_bottom_left[1] <= circle_center[1] <= rectangle_bottom_left[1] + rectangle_height):
        return True

    for x in range(rectangle_bottom_left[0], rectangle_bottom_left[0] + rectangle_width):
        for y in range(rectangle_bottom_left[1], rectangle_bottom_left[1] + rectangle_height):
            if math.sqrt((x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2) <= circle_radius:
                return True

    for x in range(rectangle_bottom_left[0], rectangle_bottom_left[0] + rectangle_width + 1):
        for y in range(rectangle_bottom_left[1], rectangle_bottom_left[1] + rectangle_height + 1):
            if math.sqrt((x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2) <= circle_radius:
                return True
    
    return False

magias = {'fire':[200, 20, 30, 50], 'water':[300, 10, 25, 40], 'earth':[400, 25, 55, 70], 'air':[100, 18, 38, 60]}

for i in range(int(input())):
    w, h, xr, yr = [int(x) for x in input().split()]
    magia, nivel, xc, yc = input().split()
    xc, yc = int(xc), int(yc)
    dano, raio = magias[magia][0], magias[magia][nivel]
    rectangle_bottom_left = (xr, yr)  
    rectangle_width = w
    rectangle_height = h
    circle_center = (xc, yc)  
    circle_radius = raio
    if intersecao(rectangle_bottom_left, circle_center, circle_radius):
        print(dano)
    else:
        print("0")