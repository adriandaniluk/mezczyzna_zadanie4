import random
add_library('pdf') 

def setup():
    global img 
    size(400, 400) 
    img = loadImage("mezczyzna.jpg") 
    beginRecord(PDF, "outmezczyzna.pdf")
def draw():
    if keyPressed:
         if key==('c'):
            clear() 
            img= loadImage("mezczyzna.jpg")
            image(img,0,0,height,width)
            endRecord()
         if key==('z'):
            img= loadImage("mezczyzna.jpg")
            image(img,0,0,height,width)
            global zarost
            zarost= loadImage("was_1.png")
            beginRecord(PDF,"outwas_1.pdf")
            image(zarost,140,215,height-290,width-330)
            endRecord()
         if key==('x'):
           img= loadImage("mezczyzna.jpg")
           image(img,0,0,height,width)
           global zarost2
           zarost2= loadImage("was_2.png")
           beginRecord(PDF,"outwas_2.pdf")
           image(zarost2,140,215,height-290,width-340)
           endRecord()
def mousePressed():
    exit()
