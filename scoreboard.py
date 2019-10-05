import pygame.font
from pygame.sprite import Group
from ship import Ship
class ScoreBoard():
    '''Класс для вывода игровой информации'''
    def __init__(self, settings, screen , stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        #Настройки шрифта для вывода счета'''
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('arial', 48)
        #подготовка вывода счета , рекорда и уровня
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        ''' Преобразует текущий счет в графическое изображение'''
        rounded_score = int(round(self.stats.score, -1)) # round округляет дробное число до количества знаков в аргументе
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Счет: " + score_str, True, self.text_color, self.settings.bg_color)
        #вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, - 1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("Рекорд: " + high_score_str,True, self.text_color, self.settings.bg_color)
        # рекорд выравнивается по центру экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect) # счет число
        self.screen.blit(self.level_image, self.level_rect) # уровень число
        self.screen.blit(self.high_score_image, self.high_score_rect)  # рекорд число
        self.ships.draw(self.screen)

    def prep_level(self):
        # выводит уровень на экран
        self.level_image = self.font.render("Уровень: " + str(self.stats.level), True, self.text_color, self.settings.bg_color)
        # уровень выводится под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

