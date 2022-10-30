import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем."""

    def __init__(self, ss_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings
    
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # # Каждый новый корабль появляется у нижнего края экрана.
        # self.rect.midleft = self.screen_rect.midleft

        # Start each new ship at the center of the left side of the screen.
        self.center_ship()

        # # Сохранение вещественной координаты центра корабля. 
        # self.y = float(self.rect.y)

        # Флаги перемещения 
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        # Обновляется атрибут x объекта ship, не rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        # Обновление атрибута rect на основании self.y.
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the left side of the screen."""
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)
    
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

        