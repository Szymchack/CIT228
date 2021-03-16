import sys
from time import sleep

import pygame
from Ocho.bullet import Bullet
from Ocho.flies import flies


def check_play_button(ai_settings, screen, stats, sb, play_button, frog,
                      flies, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        start_game(ai_settings, screen, stats, sb, frog, flies, bullets)


def check_events(ai_settings, screen, stats, sb, play_button, frog, flies,
                 bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, frog,
                                 flies, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, frog)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              frog, flies, bullets, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, screen, stats, sb, frog, flies,
                         bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        frog.moving_right = True
    elif event.key == pygame.K_LEFT:
        frog.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, frog)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, frog, flies, bullets)


def fire_bullet(ai_settings, bullets, screen, frog):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, frog)
        bullets.add(new_bullet)