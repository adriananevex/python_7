from typing import Dict
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:

    def __init__(self, strategy: GameStrategy, factory: CardFactory):

        self.strategy = strategy
        self.factory = factory

    def create_card(self, card_type: str):

        return self.factory.create_card(card_type)

    def play_turn(self, game_state: Dict):

        decision = self.strategy.decide_action(game_state)

        return {
            "turn_result": decision,
        }