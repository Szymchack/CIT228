import pygame
from pygame.sprite import Sprite


class Frog(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the frog and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the frog image and get its rect.
        self.image = pygame.image.load_basic('images/Ocho.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Start each new frog at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the frog's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the frog's position based on the movement flags."""
        # Update the frog's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the frog at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the frog on the screen."""
        self.center = self.screen_rect.centerx