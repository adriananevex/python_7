from typing import Dict
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def decide_action(self, game_state: Dict) -> Dict:

        return {
            "action": "attack",
            "reason": "Aggressive strategy prioritizes attacking"
        }