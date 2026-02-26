from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.card_id in self.cards:
            print(f"Card {card.card_id} already registered.")
        else:
            self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            print("One or both cards are not registered!")
            return {}

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1
        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1
        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> List:
        sorted_cards = []
        Cards_c = list(self.cards.values())
        while Cards_c:
            tmp = Cards_c[0]
            for card in Cards_c:
                if card.calculate_rating() > tmp.calculate_rating():
                    tmp = card
            Cards_c.remove(tmp)
            sorted_cards.append(tmp)
        return [c.get_rank_info() for c in sorted_cards]

    def generate_tournament_report(self) -> Dict:
        total_cards = len(self.cards)
        avg_rating = (
            sum(card.calculate_rating() for card in self.cards.values())
            / total_cards
            if total_cards > 0 else 0
        )
        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': int(avg_rating),
            'platform_status': 'active' if total_cards > 0 else 'inactive'
        }
