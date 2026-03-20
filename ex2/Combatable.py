from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):

    @abstractmethod
    def attack(self, target: str) -> Dict:
        pass

    @abstractmethod
    def defend(self,damage: int) -> Dict:
        pass