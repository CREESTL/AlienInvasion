class Settings():
    def __init__(self):
        #экран
        self.width = 1200
        self.height = 800
        self.bg_color = (130,230,230)
        # корабль
        self.speed = 3
        #self.ship_limit = 3
        # пуля

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60 ,60
        self.bullets_allowed = 4
        # пришельцы
        self.fleet_drop_speed = 10
        # темп ускорения игры
        self.speedup_scale = 1.4
        #темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 50 # столько очков дается за одного пришельца


    def increase_speed(self):
        ''' Увеличивет настройки скорости и стоимости пришельцев'''

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
