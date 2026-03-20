class Player:

    def __init__(self, name: str):

        self.name = name
        self.wins = 0

    def add_win(self):

        self.wins += 1

    def get_stats(self):

        return {
            "name": self.name,
            "wins": self.wins
        }
