from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature):
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature):
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        return [
            creature.transform(),
            creature.attack(),
            creature.revert()
        ]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )

        return [
            creature.attack(),
            creature.heal()
        ]
