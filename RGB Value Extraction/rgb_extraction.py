from PIL import Image

im = Image.open("test_sprite.bmp")
pix = im.load()
imWidth = im.width
imHeight = im.height

print(type(pix[0, 0]))
print(pix[0, 0])

for x in range(imWidth):
    for y in range(imHeight):
        p = list(pix[y, x])
        #p.pop(3)
        for z in range(len(p)):
            if p[z] < 16:
                p[z] = 0
            elif p[z] < 32:
                p[z] = 1
            elif p[z] < 48:
                p[z] = 2
            elif p[z] < 64:
                p[z] = 3
            elif p[z] < 80:
                p[z] = 4
            elif p[z] < 96:
                p[z] = 5
            elif p[z] < 112:
                p[z] = 6
            elif p[z] < 128:
                p[z] = 7
            elif p[z] < 144:
                p[z] = 8
            elif p[z] < 160:
                p[z] = 9
            elif p[z] < 176:
                p[z] = 10
            elif p[z] < 192:
                p[z] = 11
            elif p[z] < 208:
                p[z] = 12
            elif p[z] < 224:
                p[z] = 13
            elif p[z] < 240:
                p[z] = 14
            else:
                p[z] = 15

            p[z] = bin(p[z])[2:].zfill(4)
        print(*p, sep='')
    #print(' ')









