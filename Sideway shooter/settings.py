class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        # Настройки корабля 
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 6 
        self.bullet_width = 15 
        self.bullet_height = 3 
        self.bullet_color = (60, 60, 60)

        # Ограничение количества снарядов
        self.bullets_allowed = 9

        # Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #  Higher values -> more frequent aliens. Max = 1.0.
        self.alien_frequency = 0.008


        # Темп ускорения игры 
        self.speedup_scale = 1.1

        # After every levelup_hits, level up the difficulty.
        self.levelup_hits = 1       

        # Темп роста стоимости пришельцев 
        self.score_scale = 1.5

        self.initialize_dynamic_settings()




    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры.""" 
        self.ship_speed = 1.5 
        self.bullet_speed = 3.0 
        self.alien_speed = 1.0


        # Подсчет очков 
        self.alien_points = 10

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев.""" 
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale 
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)