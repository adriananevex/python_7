import random

class Match:

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

    def play(self):

        winner = random.choice([self.player1, self.player2])

        winner.add_win()

        return {
            "player1": self.player1.name,
            "player2": self.player2.name,
            "winner": winner.name
        }
