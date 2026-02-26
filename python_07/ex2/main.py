from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical:['cast_spell', 'channel_mana', 'get_magic_stats']")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    arcane_warrior = EliteCard("Arcane Warrior", 10, "Legendary", 5, 5, 10, 4)
    enemy = EliteCard("Enemy", 7, "rare", 7, 3, 10, 4)
    available_mana_1 = 20
    battlefield = []
    game_state = {
            'available_mana': available_mana_1,
            'battlefield': battlefield
            }
    arcane_warrior.play(game_state)
    available_mana_2 = 15
    game_state = {
            'available_mana': available_mana_2,
            'battlefield': battlefield
            }
    enemy.play(game_state)
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(enemy.damage)}")

    enemy1 = CreatureCard("Enemy1", 4, "Common", 2, 2)
    enemy2 = CreatureCard("Enemy2", 3, "rare", 3, 3)

    print("\nMagic phase:")
    print(
        "Spell cast: "
        f"{arcane_warrior.cast_spell('Fireball', [enemy1.name, enemy2.name])}"
        )
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
