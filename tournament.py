from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def summarize_opponents(opponents):
    factory_labels = {
        "FlameFactory": "Flameling",
        "AquaFactory": "Aquabub",
        "HealingCreatureFactory": "Healing",
        "TransformCreatureFactory": "Transform",
    }
    pairs = []
    for factory, strategy in opponents:
        factory_name = factory.__class__.__name__
        factory_name = factory_labels.get(factory_name, factory_name)
        strategy_name = strategy.__class__.__name__
        if strategy_name.endswith("Strategy"):
            strategy_name = strategy_name[:-8]
        pairs.append(f"({factory_name}+{strategy_name})")
    return f"[ {', '.join(pairs)} ]"


def battle(opponents):
    print(summarize_opponents(opponents))
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):

                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                c1 = factory1.create_base()
                c2 = factory2.create_base()

                print()
                print("* Battle *")
                print(c1.describe())
                print(" vs.")
                print(c2.describe())
                print(" now fight!")

                # Estratégia 1
                for action in strategy1.act(c1):
                    print(action)

                # Estratégia 2
                for action in strategy2.act(c2):
                    print(action)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


print()
print("Tournament 0 (basic)")
t0 = [
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy())
]
battle(t0)

print()
print("Tournament 1 (error)")
t1 = [
    (FlameFactory(), AggressiveStrategy()),  # inválido
    (HealingCreatureFactory(), DefensiveStrategy())
]
battle(t1)

print()
print("Tournament 2 (multiple)")
t2 = [
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy())
]
battle(t2)
