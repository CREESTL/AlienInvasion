''' Файл отвечает за полет пули'''
import pygame
from pygame.sprite import Sprite
# спрайты объединяют связанные элементы и позволяет работать с группой
class Bullet(Sprite): # дочерний класс
    def __init__(self, settings , screen, ship):
        super(Bullet, self).__init__() # это значит что он наследует от класса Sprite все значения его init
        self.screen = screen
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height) # создание самой пули
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top # будет вылетать из верха корабля
        self.y = float(self.rect.y) # y пули равен y корабля
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update_bullet(self):
        '''перемещает пулю вверх по экрану '''
        self.y -= self.speed
        self.rect.y = self.y # необходимо обновлять позицию пули после каждого смещения

    def draw_bullet(self):
        pygame.draw.rect(self.screen , self.color , self.rect) # рисует пулю
