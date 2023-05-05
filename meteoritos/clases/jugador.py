import pygame
from clases import disparo


class Nave(pygame.sprite.Sprite): # hereda de la clase Sprite que sirve para crear objetos en pantalla y poder manipularlos
    def __init__(self): # metodo constructor
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("pygamesJuego/meteoritos/imagenes/nave.png")
        self.imagenExplota = pygame.image.load("pygamesJuego/meteoritos/imagenes/naveExplota.png")
        #tomamos rectangulo imagen
        self.rect = self.imagenNave.get_rect()
        #posicion inicial nave
        self.rect.centerx = 240 
        self.rect.centery = 590
        self.velocidad = 10
        self.vida = True
        self.listaDisparo = []
        self.sonidoDisparo = pygame.mixer.Sound("pygamesJuego/meteoritos/sonidos/disparo.aiff")
        
    def mover (self):    
        if self.vida == True:
            if self.rect.left<=0:
                self.rect.left = 0
            elif self.rect.right>490:
                self.rect.right = 490
        
            
                    
    def disparar(self,x,y):
        if self.vida == True:
            #print("Estoy disparando")  
            misil = disparo.Misil(x,y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()
        
    def dibujarNave (self,superficie):   
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect) # dibuja la nave en la ventana
        else:
            superficie.blit(self.imagenExplota, self.rect)            