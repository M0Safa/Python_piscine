def mage_counter() -> callable:
    count = 0

    def counting_stars() -> int:
        nonlocal count
        count += 1
        return count

    return counting_stars


def spell_accumulator(initial_power: int) -> callable:
    count = initial_power

    def counting_power(power: int) -> int:
        nonlocal count
        count += power
        return count

    return counting_power


def enchantment_factory(enchantment_type: str) -> callable:
    type = enchantment_type

    def enchant_item(item: str) -> str:
        return (f"{type} {item}")

    return enchant_item


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: any) -> None:
        vault[key] = value

    def recall(key: str) -> any:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("\nTesting mage counter...")

    count = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {count()}")

    print("\nTesting Spell accumulator...")

    final_power = spell_accumulator(10)
    print(f"Start power: {final_power(10)}")
    for i in range(3):
        print(f"Current power: {final_power(5)}",
              "(5 added)")

    print(f"Final power : {final_power(0)}")

    print("\nTesting enchantment_factory...")

    enchantments = {
        "type": "Warrior",
        "weapon": "Sword, shield",
        "rarity": "Legendary",
        "cost": "25 coins",
        "health": "200"
    }
    for enchantment, item in enchantments.items():
        enchant = enchantment_factory(enchantment)
        print(enchant(item))

    print("\nTesting memory vault...")

    vault = memory_vault()
    vault["store"]("damage", 50)
    print("Recalling stored memory...")
    print(f"Damage: {vault['recall']('damage')}\n")
    print("Recalling no stored memory...")
    print(f"Cost: {vault['recall']('Cost')}")
