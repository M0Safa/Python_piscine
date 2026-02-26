from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 card_id: str,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 defense: int,
                 health: int,
                 rating: int
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.card_id: str = card_id
        self.attack_power: int = attack
        self.defense_power: int = defense
        self.health: int = health
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = rating

    def play(self, game_state: Dict) -> Dict:
        if game_state['available_mana'] < self.cost:
            print("MANA: too low mana!")
            return {}
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        }

    def attack(self, target) -> Dict:
        if self.attack_power <= 0:
            print("Error: You can't deal damage")
            return {}
        elif self.health <= 0:
            print("Error: Already Dead!")
            return {}
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack_power,
            'combat_resolved': True
            }

    def defend(self, incoming_damage: int) -> dict:
        if self.health <= 0:
            print("Error: Your Card is already dead")
            return {}
        if incoming_damage <= 0:
            print("Error: Invalid incoming damage provided")
            return {}
        damage_taken = max(0, incoming_damage - self.defense_power)
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense_power,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense_power,
            'current_health': self.health,
            'combat_style': 'melee'
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def get_tournament_stats(self) -> Dict:
        total_games = self.wins + self.losses
        return {
            'card_id': self.card_id,
            'name': self.name,
            'rarity': self.rarity,
            'wins': self.wins,
            'losses': self.losses,
            'total_matches': total_games,
            'rating': self.calculate_rating()
            }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
            }
