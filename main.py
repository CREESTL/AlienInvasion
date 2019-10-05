import sys
import pygame
from settings import Settings # импортировали единственный раз а дальше она переносится во все фугкции
from ship import Ship
from alien import Alien
import game_functions
from game_stats import GameStats
from scoreboard import ScoreBoard
from pygame.sprite import Group # импортируем для группировки пуль
from button import Button
def run():
    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption('alien invasion')

    ''' Создание экземпляров'''
    ship = Ship(settings, screen)
    alien = Alien(settings , screen)

    ''' Группы для обработки'''
    bullets = Group()
    aliens = Group()

    ''' Создание флота пришельцев'''
    game_functions.create_fleet(settings , screen ,ship, aliens)

    ''' Создание класса для ведения статичтики'''
    stats = GameStats(settings)
    score_board = ScoreBoard(settings, screen, stats, )
    '''Создание кнопки PLAY'''
    play_button = Button(settings , screen, 'PLAY')

    while True:
        game_functions.check_events(settings, screen, stats, score_board, play_button, ship, aliens, bullets)

        if stats.game_active:
            # если корабли еще остались у игрока
            ship.update_ship()
            game_functions.update_bullets(settings, screen, stats, score_board, ship, aliens, bullets)
            game_functions.update_aliens(stats, screen, bullets, score_board, settings, aliens, ship)
        game_functions.update_screen(score_board, settings, screen, ship, aliens, stats,  bullets, play_button) # здесь settings screen ship и bullets
run()