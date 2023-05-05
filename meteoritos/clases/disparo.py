import pygame 

class Misil (pygame.sprite.Sprite):
    def __init__ (self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil = pygame.image.load("pygamesJuego/meteoritos/imagenes/misil.png")
        self.rect = self.imagenMisil.get_rect() 
        self.velocidadDisparo = 10
        self.rect.top = posY #el rect sirve para la posicion 
        self.rect.left = posX
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo #Se le va restando la velocidad para que el misil comience a subir
    def dibujar(self,superficie):
        superficie.blit(self.imagenMisil,self.rect)     