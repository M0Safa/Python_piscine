from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.cards:
            if card_name == c.name:
                self.cards.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0) if self.cards else None

    def get_deck_stats(self) -> dict:
        avg_cost = sum(c.cost for c in self.cards) / len(self.cards)
        return {
            "total_cards": len(self.cards),
            "creatures": sum(isinstance(c, CreatureCard) for c in self.cards),
            "spells": sum(isinstance(c, SpellCard) for c in self.cards),
            "artifacts": sum(isinstance(c, ArtifactCard) for c in self.cards),
            "avg_cost": round(avg_cost, 2)
        }
