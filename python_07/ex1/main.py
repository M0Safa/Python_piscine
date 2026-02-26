from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()
    game_State = {
        'available_mana': 20,
        'battlefield': []
    }
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common",
                            "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 5,
                               "+1 mana per turn"))
    print("Building deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())
    deck.shuffle()
    print("\nDrawing and playing cards:")
    while True:
        card = deck.draw_card()
        if not card:
            break
        print(f"\nDrew: {card.name} ({card.get_card_info()['type']})")
        print("Play result:", card.play(game_State))
    print("\nPolymorphism in action: Same interface,",
          "different card behaviors!")


if __name__ == "__main__":
    main()
