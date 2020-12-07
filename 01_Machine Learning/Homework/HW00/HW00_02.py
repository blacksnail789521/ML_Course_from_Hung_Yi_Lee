from PIL import Image

lena = Image.open("input/lena.png")
lena_modified = Image.open("input/lena_modified.png")

w, h = lena.size
for j in range(h):
    for i in range(w):
        if lena.getpixel((i, j)) == lena_modified.getpixel((i, j)):
            lena_modified.putpixel((i, j), 255)

lena_modified.save("output/HW00_02.png")