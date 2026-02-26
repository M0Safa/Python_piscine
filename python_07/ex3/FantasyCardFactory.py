from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, List
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_templates = ["Dragon", "Goblin"]
        self.spell_templates = ["Fireball", "Ice", "Lightning Bolt"]
        self.artifact_templates = ["Rings", "Staffs", "Crystals"]

    def create_creature(self, name_or_power) -> Card:
        creature_stats = {
            "Dragon": {"cost": 5,
                       "rarity": "Legendary",
                       "attack": 7,
                       "health": 5},

            "Goblin": {"cost": 2,
                       "rarity": "Common",
                       "attack": 5,
                       "health": 2}
        }
        if isinstance(name_or_power, str):
            if name_or_power not in self.creature_templates:
                return None
            stats = creature_stats[name_or_power]
            return (CreatureCard(name_or_power,
                                 stats['cost'],
                                 stats['rarity'],
                                 stats['attack'],
                                 stats['health']))

        if isinstance(name_or_power, int):
            if name_or_power >= 7:
                name = "Dragon"
            else:
                name = "Goblin"
            stats = creature_stats[name]
            return (CreatureCard(name,
                                 stats['cost'],
                                 stats['rarity'],
                                 stats['attack'],
                                 stats['health']))
        return None

    def create_spell(self, name_or_power) -> Card:
        spell_stats = {
            "Fireball": {"cost": 4,
                         "rarity": "Common",
                         "effect_type": "Deal 4 damage"},

            "Ice": {"cost": 2,
                    "rarity": "Common",
                    "effect_type": "Freeze target"},

            "Lightning Bolt": {"cost": 3,
                               "rarity": "Rare",
                               "effect_type": "Deal 3 damage"}
        }
        if isinstance(name_or_power, str):
            if name_or_power not in self.spell_templates:
                return None
            stats = spell_stats[name_or_power]
            return (SpellCard(name_or_power,
                              stats['cost'],
                              stats['rarity'],
                              stats['effect_type']))
        if isinstance(name_or_power, int):
            if name_or_power >= 4:
                name = "Fireball"
            elif name_or_power == 3:
                name = "Lightning Bolt"
            else:
                name = "Ice"
            stats = spell_stats[name]
            return (SpellCard(name,
                              stats['cost'],
                              stats['rarity'],
                              stats['effect_type']))
        return None

    def create_artifact(self, name_or_power) -> Card:
        artifact_stats = {
            "Rings": {"cost": 1,
                      "rarity": "Rare",
                      "durability": 5,
                      "effect": "+1 mana per turn"},

            "Staffs": {"cost": 3,
                       "rarity": "Legendary",
                       "durability": 3,
                       "effect": "Boost spell damage"},

            "Crystals": {"cost": 2,
                         "rarity": "Rare",
                         "durability": 4,
                         "effect": "Draw extra card"}
        }
        if isinstance(name_or_power, str):
            if name_or_power not in self.artifact_templates:
                return None
            stats = artifact_stats[name_or_power]
            return (ArtifactCard(name_or_power,
                                 stats['cost'],
                                 stats['rarity'],
                                 stats['durability'],
                                 stats['effect']))

        if isinstance(name_or_power, int):
            if name_or_power >= 3:
                name = "Staffs"
            elif name_or_power == 2:
                name = "Crystals"
            else:
                name = "Rings"
            stats = artifact_stats[name]
            return (ArtifactCard(name,
                                 stats['cost'],
                                 stats['rarity'],
                                 stats['durability'],
                                 stats['effect']))
        return None

    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }

        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                name = random.choice(self.creature_templates)
                deck["creatures"].append(self.create_creature(name))
            elif card_type == "spell":
                name = random.choice(self.spell_templates)
                deck["spells"].append(self.create_spell(name))
            else:
                name = random.choice(self.artifact_templates)
                deck["artifacts"].append(self.create_artifact(name))
        return deck

    def get_supported_types(self) -> Dict:
        return {
                'creatures': self.creature_templates,
                'spells': self.spell_templates,
                'artifacts': self.artifact_templates,
        }
