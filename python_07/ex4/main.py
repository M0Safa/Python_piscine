from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()
    card1 = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Epic",
        attack=8,
        defense=4,
        health=10,
        rating=1200
    )
    card2 = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack=6,
        defense=3,
        health=8,
        rating=1150
    )
    for card in [card1, card2]:
        platform.register_card(card)
        print(f"{card.name} (ID: {card.card_id}):")
        card_stats = card.get_rank_info()
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card_stats['rating']}")
        print(f"- Record: {card_stats['record']}\n")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    rank = 1
    for entry in leaderboard:
        print(f"{rank}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")
        rank += 1
    print()
    report = platform.generate_tournament_report()
    print("Platform Report:")
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
