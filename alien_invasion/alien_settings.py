class Settings:
    """All settings for Alien Invasion"""

    def __init__(self):

        """Initialize the game settings"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,51,77)

        #ship settings
        self.ship_speed = 1.5

        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (204, 0, 102)
        self.bullets_allowed = 3