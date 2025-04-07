# monster.py
from character import Character
import random

class Monster(Character):
    def __init__(self):
        """
        Constructor for the Monster class.
        Calls the parent's constructor and initializes monster-specific properties.
        Chooses a random monster type.
        """
        self.monster_types = {
            "Goblin": {"health_multiplier": 0.8, "strength_multiplier": 0.7, "level": 1, "special_ability": None},
            "Orc": {"health_multiplier": 1.2, "strength_multiplier": 1.1, "level": 2, "special_ability": "Smash"},
            "Troll": {"health_multiplier": 1.5, "strength_multiplier": 0.9, "level": 3, "special_ability": "Regenerate"},
            "Spider": {"health_multiplier": 0.6, "strength_multiplier": 1.3, "level": 1, "special_ability": "Poison"}
        }
        self.monster_name, self.monster_stats = random.choice(list(self.monster_types.items()))

        super().__init__()
        self._m_combat_strength = int(self.combat_strength * self.monster_stats["strength_multiplier"])
        self._m_health_points = int(self.health_points * self.monster_stats["health_multiplier"])
        self._special_ability_name = self.monster_stats["special_ability"]
        self.level = self.monster_stats["level"] # Set the level for experience calculation

        print(f"    |    A wild {self.monster_name} appears!")
        print(f"    |    Monster Type: {self.monster_name}")
        print(f"    |    Monster Level: {self.level}")
        print(f"    |    Initial Monster Combat Strength: {self._m_combat_strength}")
        print(f"    |    Initial Monster Health Points: {self._m_health_points}")
        if self._special_ability_name:
            print(f"    |    Special Ability: {self._special_ability_name}")

    def __del__(self):
        """
        Destructor for the Monster class.
        Prints a Monster-specific message and calls the parent's destructor.
        """
        print("    |    The Monster object is being destroyed.")
        super().__del__()

    @property
    def m_combat_strength(self):
        """Getter for m_combat_strength."""
        return self._m_combat_strength

    @m_combat_strength.setter
    def m_combat_strength(self, value):
        """Setter for m_combat_strength."""
        if isinstance(value, int) and value > 0:
            self._m_combat_strength = value
        else:
            print("    |    Invalid monster combat strength value.")

    @property
    def m_health_points(self):
        """Getter for m_health_points."""
        return self.health_points # Use inherited property

    @m_health_points.setter
    def m_health_points(self, value):
        """Setter for m_health_points."""
        self.health_points = value # Use inherited property setter

    def use_special_ability(self, hero):
        """Uses the monster's special ability."""
        if self._special_ability_name == "Smash":
            damage = int(self.m_combat_strength * 1.5)
            print(f"    |    {self.monster_name} uses Smash, dealing {damage} damage!")
            hero.health_points -= damage
        elif self._special_ability_name == "Regenerate":
            heal = random.randint(5, 10)
            self.health_points += heal
            print(f"    |    {self.monster_name} uses Regenerate, healing {heal} health!")
        elif self._special_ability_name == "Poison":
            print(f"    |    {self.monster_name} uses Poison! Hero takes 3 damage.")
            hero.health_points -= 3
        elif self._special_ability_name is not None:
            print(f"    |    {self.monster_name} tries to use {self._special_ability_name}!")
        return hero.health_points

    def monster_attacks(self, hero):
        """
        Simulates the monster attacking the hero.
        Includes a chance for a critical hit and using a special ability.
        """
        use_special = self._special_ability_name and random.randint(1, 3) == 1 # 33% chance to use special
        if use_special:
            self.use_special_ability(hero)
        else:
            critical_hit = random.randint(1, 10) == 1  # 10% chance of critical hit
            damage = self.m_combat_strength
            if critical_hit:
                damage *= 2
                print("    |    Monster lands a critical hit!")

            print(f"    |    {self.monster_name} attacks with strength {self.m_combat_strength}, dealing {damage} damage.")
            hero.health_points -= damage
            print(f"    |    Hero health: {hero.health_points}")
        return hero.health_points