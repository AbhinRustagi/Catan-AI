class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
        self.settlements = []
        self.cities = []
        self.roads = []

    def build_settlement(self, location):
        # Logic to build a settlement
        pass
    
    def build_road(self, location):
        # Logic to build a road
        pass