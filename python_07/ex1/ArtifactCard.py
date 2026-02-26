from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if game_state['available_mana'] < self.cost:
            print("MANA: too low mana!")
            return {}
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Artifact exhausted"
            }
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_left": self.durability
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": "Artifact",
                "effect": self.effect,
                "durability_left": self.durability
            }
        )
        return info
