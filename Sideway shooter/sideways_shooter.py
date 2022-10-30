import sys
from random import random

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

from scoreboard import Scoreboard

class SidewaysShooter:
    """Класс для управления ресурсами и поведением игры."""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) 
        # self.settings.screen_width = self.screen.get_rect().width 
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideway Shooter")

        # Создание экземпляра для хранения игровой статистики. 
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Создание кнопки Play. 
        self.play_button = Button(self, "Play")
        


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                # Consider creating a new alien.
                self._create_alien()

                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

    def _check_events(self):
        """Реагирует на нажатие клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() 
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play.""" 
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) 
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        # Сброс игровых настроек.
        self.settings.initialize_dynamic_settings()

        # Сброс игровой статистики.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_ships()

        # Очистка списков пришельцев и снарядов. 
        self.aliens.empty() 
        self.bullets.empty()

        # Создание нового флота и размещение корабля в центре. 
        self._create_alien() 
        self.ship.center_ship()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                # print(len(self.bullets))

        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами.""" 
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        # Проверка попаданий в пришельцев.
        # При обнаружении попадания удалить снаряд и пришельца. 
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)


        if collisions:
            for aliens in collisions.values():
                self.stats.num_hits += self.settings.alien_points * len(aliens)
            # Update stats, and see if game should speed up.
            # self.stats.num_hits +=  1
            if self.stats.num_hits % self.settings.levelup_hits == 0:
                self.settings.increase_speed()
                self.sb.prep_score()
                self.sb.check_high_score()


    def _create_alien(self):
        """Create an alien, if conditions are right."""
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)

            # print(len(self.aliens))

    def _update_aliens(self):
        """Update alien positions, and look for collisions with ship."""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens that have hit the left edge of the screen.
        self._check_aliens_left_edge()

    def _check_aliens_left_edge(self):
        """Respond to aliens that have hit left edge of the screen.
        Treat this the same as the ship getting hit.
        """

        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to an alien hitting the ship."""
        if self.stats.ships_left > 0:
            # Decrement ships left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Center the ship.
            self.ship.center_ship()
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран.""" 
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Вывод информации о счете. 
        self.sb.show_score()

        # Кнопка Play отображается в том случае, если игра неактивна. 
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ss_game = SidewaysShooter()
    ss_game.run_game()
