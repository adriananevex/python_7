from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine

def main():

    print("=== DataDeck Game Engine ===\n")

    strategy = AggressiveStrategy()

    factory = FantasyCardFactory()

    engine = GameEngine(strategy, factory)

    print("Creating cards:\n")

    creature = engine.create_card("creature")
    spell = engine.create_card("spell")
    artifact = engine.create_card("artifact")

    print(creature.get_card_info())
    print(spell.get_card_info())
    print(artifact.get_card_info())

    print("\nPlaying turn:\n")

    result = engine.play_turn({"mana": 5})

    print(result)


if __name__ == "__main__":
    main()