from random import randint

import pygame 
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ss_game):
        """Инициализирует пришельца и задает его начальную позицию.""" 
        super().__init__() 
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()


        # Start each new alien at a random position on the right side
        #   of the screen.
        self.rect.left = self.screen.get_rect().right

        # The farthest down the screen we'll place the alien is the height
        #   of the screen, minus the height of the alien.
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)


        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

 

    def update(self):
        """Перемещает пришельца влево или вправо."""
        self.x -= self.settings.alien_speed 
        self.rect.x = self.x


