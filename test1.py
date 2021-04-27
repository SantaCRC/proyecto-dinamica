import pygame, sys, math
import ecuaciones
from tkinter import *
import threading

from tkinter import messagebox


def animar():
    h_v,x_v=ecuaciones.resolver()
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
    bloque = pygame.image.load("bloque.png")

    while run:
        msElapsed = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(white)
        screen.blit(bloque,(xb,yb))
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

        pygame.display.flip()

    pygame.quit()

top = Tk()
top.geometry("300x300")
def helloCallBack():
   ecuaciones.set_vars(float(txt.get()),float(txt1.get()),0,1,2,0.6)
   animar()

B=Button(top, text = "Simular", command = helloCallBack)
label=Label(top, text="Coeficiente de friccion dinamico:")
label.place(x=0,y=80)
label1=Label(top, text="Masa bloque A, en kilogramos:")
label1.place(x=0,y=100)
txt = Entry(top,width=10)
txt.place(x=180,y=80)
txt1 = Entry(top,width=10)
txt1.place(x=180,y=100)
B.place(x=50,y=250)

top.mainloop()
