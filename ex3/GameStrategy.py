from abc import ABC, abstractmethod
from typing import Dict

class GameStrategy(ABC):

    @abstractmethod
    def decide_action(self, game_state: Dict) -> Dict:
        pass