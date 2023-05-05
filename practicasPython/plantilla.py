import pygame,sys #sys es para poder usar exit
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800,700))
pygame.display.set_caption("TITULO DE LA VENTANA") 
colorFondo = (1,150,70)
while True:
    ventana.fill(colorFondo)
    for evento in pygame.event.get(): #Bucle para comprobar los eventos que estan ocurriendo
        if evento.type == QUIT: #Vamos a comprobar si el evento es del tipo QUIT
            pygame.quit() #Si es asi, cerramos el juego
            sys.exit() #Y salimos del bucle
    pygame.display.update() 
