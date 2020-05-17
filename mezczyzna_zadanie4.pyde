import random
add_library('pdf') 

def setup():
    global img 
    size(400, 400) # to nie jest proporcja zdjęcia dokumentowego
    img = loadImage("mezczyzna.jpg") 
    beginRecord(PDF, "outmezczyzna.pdf")
def draw():
    if keyPressed:
        image(img,0,0,height,width)
        if key == 'c':
            image(img,0,0,height,width)
        if key==('z'):
            zarost= loadImage("was_1.png")
            image(zarost,140,215,height-290,width-330)
            endRecord()
        if key==('x'):
           zarost2= loadImage("was_2.png")
           image(zarost2,140,215,height-290,width-340)
           endRecord()
def mousePressed():
    exit()

#1,75pkt
