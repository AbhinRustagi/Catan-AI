from Board import Board


class Game:
    def __init__(self, no_of_players):
        self.board = Board()
        self.no_of_players = no_of_players
        self.current_player = 0

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.no_of_players)