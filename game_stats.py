''' Хранит статистику игры'''
class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats() # можно функцию из класса вызывать в самом классе
        self.game_active = False
        #рекорд не должен сбрасываться
        self.high_score = 0


    def reset_stats(self):
        self.ship_left = 3# проверяет сколько осталось кораблей
        #вводим счет
        self.score = 0
        # счет уровней
        self.level = 1

