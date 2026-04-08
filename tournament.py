from ex4.Match import Match


class Tournament:

    def __init__(self):

        self.players = []

    def register_player(self, player):

        self.players.append(player)

    def start(self):

        results = []

        for i in range(0, len(self.players), 2):

            player1 = self.players[i]
            player2 = self.players[i + 1]

            match = Match(player1, player2)

            result = match.play()

            results.append(result)

        return results

    def leaderboard(self):

        ranking = sorted(self.players, key=lambda p: p.wins, reverse=True)

        return [p.get_stats() for p in ranking]
