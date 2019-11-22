class Plant:
    """Domain model Plant"""
    def __init__(self, name, hex, season, red, green, blue):
        self.name = name
        self.hex = hex
        self.season = season
        self.rgb = {red, green, blue}