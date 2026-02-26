from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy
from typing import List, Dict


def ft_sort(hand: List, key: str) -> List:
    sorted_hand: List[Card] = []
    hand_c = hand[:]
    while True:
        if not hand_c:
            return sorted_hand
        tmp = hand_c[0]
        for card in hand_c:
            if card.cost < tmp.cost and key == "cost":
                tmp = card
            if isinstance(card, CreatureCard):
                if card.health > tmp.health and key == "health":
                    tmp = card
        hand_c.remove(tmp)
        sorted_hand.append(tmp)


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> Dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = []
        available_mana = 20
        enemies = battlefield[:]
        sorted_hand = ft_sort(hand, "cost")
        for card in sorted_hand:
            if card.cost > available_mana:
                print("You Do Not Have Enough Mana")
                return
            cards_played.append(card)
            mana_used += card.cost
            available_mana -= card.cost
            if isinstance(card, CreatureCard):
                if enemies:
                    target = enemies[0]
                    result = card.attack_target(target)
                    damage_dealt += result.get("damage_dealt", 0)
                    targets_attacked.append(target.name)
                else:
                    print("No enemies to attack.")
            else:
                continue
        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return ft_sort(available_targets, "health")
