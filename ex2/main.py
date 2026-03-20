from ex2.EliteCard import EliteCard

def main():

    print("=== DataDeck Ability System ===\n")

    archmage_knight = EliteCard(
        "Archmage Knight",
        6,
        "Legendary",
        8,
        10,
        5
    )

    print("Playing card:")
    print(archmage_knight.play({}))

    print("\nCombat test:")
    print(archmage_knight.attack("Orc Warrior"))

    print("\nDefense test:")
    print(archmage_knight.defend(3))

    print("\nSpell test:")
    print(archmage_knight.cast_spell("Dark Dragon"))

    print("\nMana channel:")
    print(archmage_knight.channel_mana())


if __name__ == "__main__":
    main()
