import pygame,sys #sys es para poder usar exit
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800,700))
pygame.display.set_caption("TITULO DE LA VENTANA") 
#Colores
colorFondo = (1,150,70)
colorLinea = (255,128,0)
colorCirculo = (255,255,0)
colorFiguras = (255,0,155)
while True:
    ventana.fill(colorFondo)
    #Lineas
    pygame.draw.line(ventana,colorLinea,(60,90),(200,100),40) #Dibuja una linea las primeras coordenadas son el punto de inicio y las segundas el punto final y el ultimo parametro es el grosor de la linea
    pygame.draw.line(ventana,colorLinea,(80,190),(100,150),20)
    pygame.draw.line(ventana,colorLinea,(10,30),(250,190),10)
    #Circulos
    pygame.draw.circle(ventana,colorCirculo,(400,100),100,30)
    pygame.draw.circle(ventana,colorCirculo,(500,150),40,20)
    #Figuras
    pygame.draw.rect(ventana,colorFiguras,(100,200,120,250)) 
    pygame.draw.polygon(ventana,colorFiguras,((400,400),
                    (500,400),(500,500),(400,500)))
    for evento in pygame.event.get(): #Bucle para comprobar los eventos que estan ocurriendo
        if evento.type == QUIT: #Vamos a comprobar si el evento es del tipo QUIT
            pygame.quit() #Si es asi, cerramos el juego
            sys.exit() #Y salimos del bucle
    pygame.display.update() 
