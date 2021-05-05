import pygame, sys, math
import ecuaciones
from tkinter import *
import threading
from PIL import Image, ImageTk
from tkinter import messagebox
pygame.init()
myfont = pygame.font.SysFont("Comic Sans MS", 15)
yellow = (0, 0, 0)
# apply it to text on a label

def animar():
    h_v,x_v=ecuaciones.resolver()
    h_v,x_v=round(h_v,6),round(x_v,6)
    run = True
    white = (255, 255, 255)
    black = (0, 0, 0)
    angle = 1.57
    x,y=10,10
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    xb,yb=400,350

    clock = pygame.time.Clock()
    screen.fill(white)

    while run:
        msElapsed = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(white)
        pygame.draw.line(screen,black,(300,200),(x,y))
        pygame.draw.rect(screen, black, pygame.Rect(xb, yb, 90, 70))
        pygame.draw.circle(screen,black,(x,y),20)
        y=int(math.sin(angle) * 200+200)
        x=int(math.cos(angle) * 200+300)
        if(xb>100):
            xb-=3
        grados=(angle*180)/math.pi-90
        h=h_v
        xa=x_v
        max=70
        if(xb<300 and grados<=max):
            angle+=0.05
        if(xb<=100):
            label = myfont.render("X={} m".format(x_v), 1, yellow)
            pygame.draw.line(screen,yellow,(150,425),(300,425))
            label2 = myfont.render("h={} m".format(h_v), 1, yellow)
            pygame.draw.line(screen,yellow,(75,390),(75,270))
            # put the label object on the screen at point x=100, y=100
            screen.blit(label, (175, 430))
            texto = pygame.transform.rotate(label2, 90)
            screen.blit(texto, [50, 280])


        pygame.display.flip()

    pygame.quit()

top = Tk()
top.geometry("380x640")
def simular():
    try:
        ecuaciones.set_vars(float(txt4.get()),float(txt1.get()),0,float(txt2.get()),float(txt3.get()),float(txt.get()))
        animar()
    except:
        ecuaciones.set_vars(0.8,0.5,0,1,2,0.6)
        messagebox.showinfo(title="Error", message="No ingreso todas las variables")
        animar()

def default():
    ecuaciones.set_vars(0.8,0.5,0,1,2,0.6)
    messagebox.showinfo(title="Info", message="Simulando con valores por defecto")
    animar()

B=Button(top, text = "Simular", command = simular)
B1=Button(top, text = "Caso por defecto", command = default)
label=Label(top, text="Coeficiente bloque y superficie:")
label.place(x=0,y=80+400)
txt = Entry(top,width=10)
txt.place(x=180,y=80+400)
label1=Label(top, text="Masa esfera A, en kilogramos:")
label1.place(x=0,y=100+400)
txt1 = Entry(top,width=10)
txt1.place(x=180,y=100+400)
B.place(x=100,y=250+350)
B1.place(x=160,y=250+350)
label2=Label(top, text="Masa bloque B, en kilogramos:")
label2.place(x=0,y=120+400)
txt2=Entry(top,width=10)
txt2.place(x=180,y=120+400)
label3=Label(top,text="Velocidad bloque B:")
label3.place(x=0,y=140+400)
txt3=Entry(top,width=10)
txt3.place(x=180,y=140+400)
label4=Label(top,text="Coeficiente bloque y esfera:")
label4.place(x=0,y=160+400)
txt4=Entry(top,width=10)
txt4.place(x=180,y=160+400)
enunciado=Label(top,text="Un bloque B de 1 kg se mueve con una velocidad Vo de \n magnitud Vo=2 m/s cuando golpea una esfera A de 0.5 kg, la cual esta\n en reposo y cuelga de una cuerda amarrada a O. \nSi se sabe que \u03BCk entre el bloque y la superficie horizontal \ny que e=0.8 entre el bloque y la esfera, determine despues\n del impacto, a) la altura maxima h alcanzada por la esfera , \nb) la distancia x recorrida por el bloque")
enunciado.place(x=0,y=0)
load = Image.open("Figura0.png")
render = ImageTk.PhotoImage(load)
img = Label(top, image=render)
img.image = render
img.place(x=2, y=120)

top.mainloop()
