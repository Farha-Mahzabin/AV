class Settings():
    """Class to store all settings for the game"""
    def __init__(self):
        """initialize game's settings"""
        #screen settings
        self.width = 1280
        self.height = 720
        self.bg_color = (0, 0, 0) #background color

        #ship settings 
        self.ship_speed_factor = .5