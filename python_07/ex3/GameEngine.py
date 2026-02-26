from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import List, Dict


class GameEngine:
    turns_simulated: int = 0

    def __init__(self):
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.cards_created: int = 0
        self.total_damage: int = 0

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            print("Engine not configured")
            return {}
        deck = self.factory.create_themed_deck(3)
        hand: List[Card] = (
            deck["creatures"]
            + deck["spells"]
            + deck["artifacts"]
        )
        battlefield: List[CreatureCard] = [
             self.factory.create_creature("Goblin")
        ]
        result = self.strategy.execute_turn(hand, battlefield)
        self.cards_created = len(hand)
        self.total_damage = result['damage_dealt']
        GameEngine.turns_simulated += 1
        return result

    def get_engine_status(self) -> Dict:
        return {
             'turns_simulated': GameEngine.turns_simulated,
             'strategy_used': self.strategy.get_strategy_name(),
             'total_damage': self.total_damage,
             'cards_created': self.cards_created,
        }
