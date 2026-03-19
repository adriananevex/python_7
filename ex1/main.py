from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():

    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    lightning_bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")

    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 10, "+1 mana per turn")

    print("Building deck with different card types...\n")

    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    deck.shuffle()

    while True:

        try:

            card = deck.draw_card()

            print(f"Drew: {card.name} ({card.__class__.__name__})")

            result = card.play({})

            print("Play result:", result, "\n")

        except ValueError:
            break

if __name__ == "__main__":
    main()
