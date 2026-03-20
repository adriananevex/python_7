from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity:str, attack: int, health: int, mana_power: int):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health
        self.mana_power = mana_power

    def play(self, game_state: dict) -> Dict:

        return {
            "card_played": self.name,
            "effect": "Elite card enters battlefield"
        }

    def attack(self, target: str) -> Dict:

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, damage: int) -> Dict:
        self.health -= damage

        return {
            "defender": self.name,
            "damage_taken": damage,
            "remainig_health": self.health
        }

    def cast_spell(self, target: str) -> Dict:

        return {
            "caster": self.name,
            "target": target,
            "spell_power":  self.mana_power
        }

    def channel_mana(self) -> Dict:

        return {
            "card": self.name,
            "mana_generated": self.mana_power
        }