from abc import ABC, abstractmethod
from ex0.creature import Creature

class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass

class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass

class Sproutling(Creature, HealCapability):
    def __init__(self):
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self):
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount"

class Shiftling(Creature, TransformCapability):
    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self):
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self):
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return "Morphagon stabilizes its form."
