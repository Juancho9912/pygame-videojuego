import pygame,sys #sys es para poder usar exit
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500,400))
pygame.display.set_caption("MOVIMIENTO AUTONOMO") 
colorFondo = (1,150,70)
colorFigura = (255,255,255)
#variables
velocidad = 2
direccion = True
posX, posY = randint(10,400), randint(10,300)
while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana,colorFigura,(posX,posY,40,40))
    #movimiento
    if direccion == True: #si es verdadero se mueve a la derecha
        if posX < (500-40): #limite derecho para que no se salga de la ventana
            posX += velocidad 
        else: 
            direccion = False #si llega al limite cambia de direccion
    else:
        if posX > 1: #limite izquierdo para que no se salga de la ventana
            posX -= velocidad  #si es falso se mueve a la izquierda 
        else: 
            direccion = True #si llega al limite cambia de direccion    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update() 
