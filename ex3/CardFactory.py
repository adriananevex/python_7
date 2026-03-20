from abc import ABC, abstractmethod
from ex0.Card import Card

class CardFactory(ABC):

    @abstractmethod
    def create_card(self, card_type: str) -> Card:
        pass