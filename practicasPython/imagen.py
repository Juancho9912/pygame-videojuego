import pygame,sys #sys es para poder usar exit
from pygame.locals import *
from random import randint #genera numeros aleatorios


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Carga imagen y posicion aleatoria de la imagen o rectangulos") 
#Colores
colorFondo = (1,150,70)
colorRectangulo = (255,60,40)
#Cargar imagen
imagen = pygame.image.load("pygamesJuego/practicasPython/imagenes/pygame.png")
#Posicion de la imagen
posX1,posY1 = (10,40)
while True:
    ventana.fill(colorFondo)
    #ventana.blit(imagen,(posX1,posY1))
    for i in range(20): #Bucle para dibujar 15 rectangulos
        posX2,posY2 = randint(1,500),randint(1,300) #Generamos numeros aleatorios para la posicion
        r,g,b = randint(0,255),randint(0,255),randint(0,255) #Generamos numeros aleatorios para el color
        colorRectangulo = (r,g,b)
        pygame.draw.rect(ventana,colorRectangulo,(posX2,posY2,50,50))
    for evento in pygame.event.get(): #Bucle para comprobar los eventos que estan ocurriendo
        if evento.type == QUIT: #Vamos a comprobar si el evento es del tipo QUIT
            pygame.quit() #Si es asi, cerramos el juego
            sys.exit() #Y salimos del bucle
    pygame.display.update() 
