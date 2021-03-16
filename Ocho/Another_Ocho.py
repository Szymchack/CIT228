# import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from Ocho.game_stats import GameStats
from Ocho.scoreboard import Scoreboard
from Ocho.button import Button
from Ocho.frog import Frog
from Ocho.game_functions import game_functions as gf


def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ocho's Adventures")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a frog, a group of bullets, and a group of aliens.
    frog = Frog(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, frog, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, frog, aliens,
                        bullets)

        if stats.game_active:
            frog.update()
            gf.update_bullets(ai_settings, screen, stats, sb, frog, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, frog, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, frog, aliens, bullets,
                         play_button)
