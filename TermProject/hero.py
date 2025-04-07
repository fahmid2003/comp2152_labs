# hero.py
from character import Character
import random

class Hero(Character):
    def __init__(self):
        """
        Constructor for the Hero class.
        Calls the parent's constructor and initializes Hero-specific properties.
        """
        super().__init__()
        self._special_ability_used = False
        self._special_ability_name = "Power Strike"
        self._special_ability_damage_multiplier = 2
        print("    |    A Hero is born with inherited properties and a special ability: Power Strike!")

    def __del__(self):
        """
        Destructor for the Hero class.
        Prints a Hero-specific message and calls the parent's destructor.
        """
        print("    |    The Hero object is being destroyed.")
        super().__del__()

    def use_special_ability(self, monster):
        """
        Uses the Hero's special ability: Power Strike.
        Can only be used once per game.
        """
        if not self._special_ability_used:
            print(f"    |    Hero uses {self._special_ability_name}!")
            damage = self.combat_strength * self._special_ability_damage_multiplier
            print(f"    |    Deals {damage} damage to the Monster!")
            monster.health_points -= damage
            self._special_ability_used = True
            return monster.health_points
        else:
            print("    |    Special ability has already been used!")
            return monster.health_points

    def hero_attacks(self, monster):
        """
        Simulates the Hero attacking a monster.
        Includes a chance for a critical hit.
        """
        critical_hit = random.randint(1, 10) == 1  # 10% chance of critical hit
        damage = self.combat_strength
        if critical_hit:
            damage *= 2
            print("    |    Critical hit!")

        print(f"    |    Hero attacks with strength {self.combat_strength}, dealing {damage} damage.")
        monster.health_points -= damage
        print(f"    |    Monster health: {monster.health_points}")
        return monster.health_points