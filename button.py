''' Создание клавиши '''
import pygame.font # позволяет выводить текст
class Button():

    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #назначение размеров и свойств кнопки
        self.width, self.height = 200 , 50
        self.button_color = (0, 255, 0)

        self.text_color = (255, 255 , 255)
        self.font = pygame.font.SysFont('arial', 48)

        #построение прямоугольника и выравнивание по центру
        self.rect = pygame.Rect(20, 20, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #сообщение на кнопке создается только один раз
        self.prep_msg(msg)

    ''' Преобразует msg  в прямоугольник и выравнивает по центру'''
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg , True, self.text_color, self.button_color)
        # render преобразует текст в изображение
        # True означает сглаживание текста
        # у текста такой же фон как и у кнопки
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    ''' Рисует кнопку'''
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
