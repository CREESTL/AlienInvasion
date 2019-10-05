import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings , screen):
        '''Инициализирует пришельца и задает его начальную позицию'''
        super(Alien, self). __init__()
        self.screen = screen
        self.settings = settings


        ''' Загружает изображение пришельца'''
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        ''' Каждый новый пришелец появляется в левом верхнеем углу экрана'''
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        '''Сохранение позиции пришельца'''
        self.x = float(self.rect.x)
    ''' Выводит на экран пришельца'''
    def blitme(self):
        self.screen.blit(self.image , self.rect)
    def update_alien(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    ''' Проверяет находится ли корабль у края '''
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True
