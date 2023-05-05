import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Tiempo")
colorFondo = (1, 150, 70)
colorCuadro1 = (255, 255, 0)
colorCuadro2 = (0, 255, 255)
colorTexto = (255, 255, 255)
#variables
velocidad = 15
direccion = True
posX1, posY1 = randint(1, 400), randint(1, 300)
posX2, posY2 = randint(1, 400), randint(1, 300)
lado = 40
tamaño = 40
cadena = "Texto de pruebas"
tipoFuente = "Arial"
poxXtexto,posYtexto = 10,10
#preparacion de fuente texto
fuente = pygame.font.SysFont(tipoFuente, tamaño)
texto = fuente.render(cadena, True, colorTexto)
while True:
    ventana.fill(colorFondo)
    #Mostrar texto
    ventana.blit(texto, (poxXtexto,posYtexto))
    #Tiempo
    tiempo = pygame.time.get_ticks() / 1000
    cadena = "Tiempo: "+str(tiempo)
    texto = fuente.render(cadena, True, colorTexto)
    cuadro1 = pygame.draw.rect(ventana, colorCuadro1, (posX1, posY1, lado, lado))
    cuadro2 = pygame.draw.rect(ventana, colorCuadro2, (posX2, posY2, lado, lado))
    #detecta colision
    if cuadro1.colliderect(cuadro2): # si colisionan
        #print(f"Colision en coordenada {posX1} : {posY1}")
        #cadena = f"Colision en coordenada {posX1} : {posY1}"
        #texto = fuente.render(cadena, True, colorTexto)
        posX2, posY2 = randint(1, 400), randint(1, 300) # nueva posicion cuadro2 al momento de colisionar
        cuadro2.left=posX2-(lado/2) 
        cuadro2.top=posY2-(lado/2)
    # detecta movimiento raton
    posX1, posY1 = pygame.mouse.get_pos()
    cuadro1.left = posX1 - (lado / 2) # centrar figura
    cuadro1.top = posY1 - (lado / 2) # centrar figura
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()