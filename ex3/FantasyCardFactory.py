from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_card(self, card_type: str):

        if card_type == "creature":
            return CreatureCard("Dragon Knight", 5, "Epic", 6, 6)

        elif card_type == "spell":
            return SpellCard("Fireball", 3, "Rare", "damage")
            
        elif card_type == "artifact":
            return ArtifactCard("Ancient Relic", 2, "Common", 10, "mana boost")

        else:
            raise ValueError("Unknown card type")
