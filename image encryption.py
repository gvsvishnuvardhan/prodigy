from PIL import Image
import random
key = random.randint(1,255)
def encrypt(input,output,key):
    image=Image.open(input)
    image = image.convert("RGB")
    pixel = image.load()
    x,y = image.size
    for i in range(x):
        for j in range(y):
            r,g,b = pixel[i,j]
            pixel[i,j]= (r+key)%256 ,(g+key)%256, (b+key%256)
    image.save(output)
    image.show()
    print("IMage is EncRypTeD")
def decrypt(input,output,key):
    image=Image.open(input)
    image = image.convert("RGB")
    pixel = image.load()
    x,y = image.size
    for i in range(x):
        for j in range(y):
            r,g,b = pixel[i,j]
            pixel[i,j]= (r-key)%256 ,(g-key)%256, (b-key%256)
    image.save(output)
    image.show()
    print("IMage is DecRypTeD")
inp= r"C:\Users\rveer\OneDrive\Documents\prodigy\p1.png"
outp= r"C:\Users\rveer\OneDrive\Documents\prodigy\p2.png"
encrypt(inp,outp,key)
decrypt(outp,outp,key)