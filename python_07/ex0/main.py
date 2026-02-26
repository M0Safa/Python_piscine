from ex0.CreatureCard import CreatureCard


def main():
    game_state = {
        "available_mana": 30,
        "battlefield": []
    }
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(6))
    print("Play result:", fire_dragon.play(game_state))
    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
