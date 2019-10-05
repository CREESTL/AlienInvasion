import pygame # сюда тоже надо импортировать чтобы работыало
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, settings , screen): # в main  мы уже задали screen через set mode
        super(Ship,self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # получили прямоугольник картинки
        self.screen_rect = screen.get_rect() # сам экран
        self.rect.centerx = self.screen_rect.centerx # центр корабля по иксу равен центру экрана
        self.rect.bottom = self.screen_rect.bottom # нижняя часть корабля на нижней части экрана
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update_ship(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: # ограничение перемещений
            self.center += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.speed
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image, self.rect) # загружает картинку на выделенный под нее прямоугольник


    ''' Размещает корабль в середине нижней части экрана'''
    def center_ship(self):
        self.center = self.screen_rect.centerx