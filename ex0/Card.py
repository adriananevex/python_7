from abc import ABC, abstractmethod
from typing import Dict

class Card(ABC):
  def __init__(self, name: str, cost: int, rarity: str):
    self.name = name
    self.cost = cost
    self.rarity = rarity

  @absctractmethod
  def play(self, game_state: dict) -> Dict:
    pass

  def get_card_info(self) -> Dict:
    return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__
    }

  def is_playable(self, available_mana: int) -> bool:
    return available >= self.cost
