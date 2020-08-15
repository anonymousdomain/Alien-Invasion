class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.fleet_dropdown_speed = 1
        # fleet direction 1 to the right -1 to the left
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = 4.0
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50
        self.bullet_allowed = 3

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_allowed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
