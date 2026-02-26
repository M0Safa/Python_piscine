from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 defense: int, attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = attack
        self.defense = defense
        self.health = health
        self.type = "EliteCard"
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        if game_state['available_mana'] < self.cost:
            print("This Card is not playable")
            return {}
        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Elite Card summoned to battlefield"
        }

    def attack(self, target) -> dict:
        if self.damage <= 0:
            print("Error: You can't deal damage")
            return {}
        elif self.health <= 0:
            print("Error: Already Dead!")
            return {}
        if not isinstance(target, Combatable):
            print("Error: The card must be a Combatable card")
            return {}
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.damage,
            'combat_type': 'melee'
            }

    def defend(self, incoming_damage: int) -> dict:
        if self.health <= 0:
            print("Error: Your Card is already dead")
            return {}
        if incoming_damage <= 0:
            print("Error: Invalid incoming damage provided")
            return {}
        damage_taken = max(0, incoming_damage - self.defense)
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': self.health > 0
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not targets:
            print("Error: There are no to targets !")
            return {}
        if self.health <= 0:
            print("Error: You Card is already Dead")
            return {}
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self.mana + amount,
            }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.damage,
            'defense': self.defense,
            'current_health': self.health,
            'combat_style': 'melee'
        }

    def get_magic_stats(self) -> dict:
        return {
            'can_cast_spells': True,
            'mana_channeling': True,
            'magic_type': 'elite'
        }
