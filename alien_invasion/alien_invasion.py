import sys
import pygame
from alien_invasion import alien_settings
from alien_invasion import images
from ship import ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create Game resources"""
        pygame.init()
        self.settings = alien_settings()
        self.screen = pygame .display.set_mode((0 ,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()

        #Background color
        self.bg_color=(0,51,77)

    def run_game(self):
        """Start main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.update_bullets()
            self._update_screen()
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet positions.
        self.bullets.update()
            #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        self._update_screen()


    def _check_events(self):        
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.key == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Creat a new bullet and add it to the bullets group"""
        if len(self, bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        #Update images and flip
        self.screen.fill(self.alien_settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
            #make most recent drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run game.
    ai = AlienInvasion()
    ai.run_game()