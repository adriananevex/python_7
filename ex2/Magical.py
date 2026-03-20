from abc import ABC, abstractmethod
from typing import Dict


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, target: str) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self) -> Dict:
        pass