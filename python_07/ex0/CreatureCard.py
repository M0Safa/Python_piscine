from ex0.Card import Card


class CreatureCard (Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if game_state['available_mana'] < self.cost:
            print("MANA: too low mana!")
            return {}
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
            }
        )
        return info
