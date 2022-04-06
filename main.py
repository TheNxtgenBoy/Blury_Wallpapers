# Build By NxtgenBoy

import random, ctypes
from PIL import Image, ImageFilter
from getpass import getuser

def generate():
    hexlist = ['a','b','c','d','e','f']
    colors = []
    for i in range(6):
        hexcolor = ''
        for i in range(6):
            hexcolor += hexlist[random.randint(0, 5)]
        colors.append(hexcolor)
    size = 1024
    stp = int(size/4)
    im = Image.new('RGB', (size,size))
    for i in range(0,size,stp):
        for j in range(0,size,stp):
            col = colors[random.randint(0, 5)]
            col = tuple(int(col[i:i+2], 16) for i in (0, 2, 4))
            for x in range(stp):
                for y in range(stp):
                    im.putpixel((i+x,j+y), col)
    im = im.filter(ImageFilter.GaussianBlur(radius = 100))
    im.save(f'C:/Users/{getuser()}/Downloads/wallp.png',quality=100)
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'C:/Users/{getuser()}/Downloads/wallp.png' , 0)

while True:
    input("Press Enter To Generate New")
    generate()
