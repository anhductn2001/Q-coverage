import random
import math
import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageDraw
NUMBER_OF_SENSOR = 150
from audioop import reverse
import argparse
R = 70
M = [[0 for x in range(10)] for y in range(NUMBER_OF_SENSOR)]
xT = []
yT = []
q = [1,2,3,4,5,6,7,8,9,10]
uncover_label = [1, 3, 2, 4, 3, 5, 2, 3, 1, 1]
b = [1 for x in range(NUMBER_OF_SENSOR)]
def return_list_index(list):
    A = [x for x in range(0, list.__len__())]
    A.sort(reverse = True, key = lambda k : list[k] )
    return A

for i in range(10):
    xT.append(random.uniform(0, 800))
    yT.append(random.uniform(0, 800))


def check():
    for j in range(10):
        tong = 0
        for p in range(NUMBER_OF_SENSOR):
            tong += M[p][j] * b[p]
        if tong >= q[j]:
            return False
    return True


def check_cover():
    dem = 0
    for j in range(10):
        if uncover_label[j] == 0:
            dem += 1

    if dem == 10:
        return False
    return True


if __name__ == '__main__':
    while check():
        Sx = []
        Sy = []
        for i in range(10):
            uncover_label[i] = q[i]
        while check_cover():
            tmp = return_list_index(b)
            for l in range(NUMBER_OF_SENSOR):
                s = tmp[0]
                for k in range(10):
                    if uncover_label[k] > 0 and len(Sx) < NUMBER_OF_SENSOR:
                        r = R * math.sqrt(random.random())
                        theta = random.random() * 2 * math.pi
                        tx = xT[k] + r * math.cos(theta)
                        ty = yT[k] + r * math.sin(theta)
                        if tx>0 and tx< 800 and ty>0 and ty<800:
                            Sx.append(tx)
                            Sy.append(ty)
                            for h in range(10):
                                if ((tx - xT[h]) ** 2 + (ty - yT[h]) ** 2) <= R ** 2:
                                    if(uncover_label[h] > 0):
                                        uncover_label[h] -= 1
                                        M[s][h] = 1
                                        b[s] -= 0.1
                        else:
                            k-=1
                            continue
                        break
                del tmp[0]
        for e in range(len(Sx)):
            xx = Sx[e]
            xy = Sy[e]
            Sx.pop(e)
            Sy.pop(e)
            if check_cover():
                continue
            Sx.append(xx)
            Sy.append(xy)
    print(M)
    print(b)
    print(Sx)
    print(Sy)
    print(xT)
    print(yT)
    print(Sx.__len__())
img = Image.new("RGB", (800,800), color = "white")
draw = ImageDraw.Draw(img)

for i,t in enumerate(Sx):
    draw = ImageDraw.Draw(img)
    x = Sx[i]
    y = Sy[i]
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(1, 0, 0, 0))
for i,t in enumerate(Sx):
    draw = ImageDraw.Draw(img)
    x = Sx[i]
    y = Sy[i]
    draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(1, 0, 0, 0))

for i,t in enumerate(xT):
    draw = ImageDraw.Draw(img)
    x = xT[i]
    y = yT[i]
    draw.ellipse((x - 6, y - 6, x + 6, y + 6), fill='blue')

img.save("test.png")