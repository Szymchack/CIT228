class Settings:
    """A class to store all settings for Another_Ocho."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (0, 240, 170)

        # frog settings
        # self.frog_speed_factor = 1.5
        self.frog_limit = 3

        # Bullet settings
        # self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # flies settings
        # self.flies_speed_factor = 1
        self.fleet_drop_speed = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the flies point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.frog_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.flies_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.flies_points = 50

    def increase_speed(self):
        """Increase speed settings and flies point values."""
        self.frog_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.flies_speed_factor *= self.speedup_scale

        self.flies_points = int(self.flies_points * self.score_scale)