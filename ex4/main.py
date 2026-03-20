from ex4.Player import Player
from ex4.Tournament import Tournament


def main():

    print("=== DataDeck Tournament Platform ===\n")

    tournament = Tournament()

    players = [
        Player("Alice"),
        Player("Bob"),
        Player("Charlie"),
        Player("Diana")
    ]

    for player in players:
        tournament.register_player(player)

    print("Starting tournament...\n")

    results = tournament.start()

    for match in results:
        print(match)

    print("\nLeaderboard:\n")

    ranking = tournament.leaderboard()

    for player in ranking:
        print(player)


if __name__ == "__main__":
    main()