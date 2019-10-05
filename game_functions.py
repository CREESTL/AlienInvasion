import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
''' Отдельный файл для функционала игры'''
def check_keydown_events(event,settings , screen , ship , bullets): # нажатие клавишь
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        '''cоздание новой пули и включение ее в группу bullets'''
        fire_bullet(settings , screen , ship , bullets)

    elif event.key == pygame.K_q: # выход при нажатии на Q
        sys.exit()


def check_keyup_events(event, ship): # отпускание клавишь
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings, screen, stats,score_board, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event ,settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats,score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y)
''' Проверяет нажатие мыши на кнопку ИГРАТЬ'''
def check_play_button(settings, screen, stats,score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        '''Обнуляет все статы'''
        stats.reset_stats()
        stats.game_active = True# координатами, то игра становится активной
        #сброс изображений счетов и уровня
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        # очистка списков пришельцев и пуль что бы создать новую игру
        aliens.empty()
        bullets.empty()
        # создание нового флота и размещение корабля в центре
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        pygame.mouse.set_visible(False)# скрывает мышу после начала игры



def update_screen(score_board,settings ,screen, ship, aliens,stats,  bullets , play_button): # и здесь settings, screen, ship , bullets (для синхронности)
    screen.fill(settings. bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #вывод счета
    score_board.show_score()
    if  stats.game_active == False: # рисует кнопку ИГРАТЬ , если игра не начата
        play_button.draw_button()

    pygame.display.flip() # переключение на новый экран


def update_bullets( settings ,screen, stats, score_board, ship, aliens, bullets):
    for bullet in bullets:
        bullet.update_bullet()  # необходимо , чтобы пули двигались
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # удаляет пули за экраном
    check_bullet_alien_collusion( settings ,screen, ship ,stats, score_board, bullets, aliens)
    bullets.update()


def check_bullet_alien_collusion( settings ,screen, ship ,stats, score_board, bullets, aliens):
    ''' Проверяет попадание в пришельцев. При обнаружении попадания удаляет пулю и пришельца'''
    collisions = pygame.sprite.groupcollide(bullets , aliens , True, True)
    ''' Два True означают, что надо удалять и пулю и пришельца из словаря столкнувшихся'''
    ''' РЕКУРСИЯ'''
    ''' Если все пришельцы уничтожены, то функция вызывает саму себя и создается новый флот'''
    if len(aliens) == 0:
        bullets.empty() # очищает группу пуль
        settings.increase_speed()
        create_fleet(settings , screen, ship , aliens)
        stats.level += 1 # увеличивает уровень
        score_board.prep_level()
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            score_board.prep_score()
            score_board.prep_high_score()
            check_high_score(stats, score_board)


def fire_bullet(settings , screen , ship , bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)



''' Вычисляет количество пришельцев в ряду'''
def get_number_aliens_x(settings , alien_width):
    available_space_x = settings.width - 2 * alien_width
    number_of_aliens = int(available_space_x / ( 2 * alien_width))
    return number_of_aliens



''' Создает пришельца и размещает его  в ряду'''
def create_alien(settings , screen, aliens, alien_number ,row_number):
    alien = Alien(settings , screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


''' Создает флот пришельцев'''
def create_fleet(settings , screen , ship , aliens):
    alien = Alien(settings, screen)
    number_of_aliens = get_number_aliens_x(settings , alien.rect.width)
    number_of_rows =  get_number_of_rows(settings, ship.rect.height , alien.rect.height)
    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings , screen , aliens , alien_number , row_number)


''' Считает количество рядов'''
def get_number_of_rows(settings , ship_height, alien_height):
    available_space_y = settings.height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows


''' Обновляет всех пришельцев'''
def update_aliens(stats, screen, bullets,score_board, settings, aliens, ship):
    check_fleet_edges(settings, aliens)
    for alien in aliens:
        alien.update_alien()
    if pygame.sprite.spritecollideany(ship , aliens):
        ship_hit(stats, screen, bullets,score_board, settings, aliens, ship)
    check_aliens_bottom(stats, screen, bullets,score_board, settings, aliens, ship)




'''Проверят нахождение флоат  относительно краев'''
def check_fleet_edges(settings , aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings , aliens)
            break


''' Меняет направление флота'''
def change_fleet_direction(settings , aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


''' Обрабатывает столкновение корабля с пришельцем'''
def ship_hit(stats, screen, bullets,score_board, settings, aliens, ship):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        score_board.prep_ships()
        #очистка списка пришельцев и пуль
        aliens.empty()
        bullets.empty()
        # создание нового флота и размщене корабля по центру нижней стороны экрана
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # делает мышу видимой после окончания игры


''' Проверяет столкновение пришельцев с нижней частью экрана'''
def check_aliens_bottom(stats, screen, bullets,score_board, settings, aliens, ship):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats, screen, bullets,score_board, settings, aliens, ship)
            break

def check_high_score(stats, score_board):
    #проверяет был ли новый рекорд
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()

