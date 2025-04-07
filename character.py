# character.py
import random

class Character:
    def __init__(self):
        """
        Constructor for the Character class.
        Initializes private combat strength, health points, experience, and level.
        """
        small_dice_options = list(range(1, 7))
        big_dice_options = list(range(1, 21))
        self._combat_strength = random.choice(small_dice_options)
        self._health_points = random.choice(big_dice_options)
        self._experience = 0
        self._level = 1
        print("    |    A Character is created.")
        print(f"    |    Initial Combat Strength: {self._combat_strength}")
        print(f"    |    Initial Health Points: {self._health_points}")
        print(f"    |    Initial Level: {self._level}")
        print(f"    |    Initial Experience: {self._experience}")

    def __del__(self):
        """
        Destructor for the Character class.
        Prints a message when the Character object is being destroyed.
        """
        print("    |    The Character object is being destroyed.")

    @property
    def combat_strength(self):
        """Getter for combat_strength."""
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        """Setter for combat_strength."""
        if isinstance(value, int) and value > 0:
            self._combat_strength = value
        else:
            print("    |    Invalid combat strength value.")

    @property
    def health_points(self):
        """Getter for health_points."""
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        """Setter for health_points."""
        if isinstance(value, int) and value >= 0:
            self._health_points = value
        else:
            print("    |    Invalid health points value.")

    @property
    def experience(self):
        """Getter for experience."""
        return self._experience

    @experience.setter
    def experience(self, value):
        """Setter for experience."""
        if isinstance(value, int) and value >= 0:
            self._experience = value
            self._check_level_up()
        else:
            print("    |    Invalid experience value.")

    @property
    def level(self):
        """Getter for level."""
        return self._level

    @level.setter
    def level(self, value):
        """Setter for level."""
        if isinstance(value, int) and value > 0:
            self._level = value
        else:
            print("    |    Invalid level value.")

    def _check_level_up(self):
        """
        Checks if the character has enough experience to level up.
        This is a basic implementation; you can make it more complex.
        """
        level_up_threshold = self._level * 100
        if self._experience >= level_up_threshold:
            self._level += 1
            print(f"    |    {self.__class__.__name__} has leveled up to level {self._level}!")
            # You can add logic here to increase stats on level up
            self._combat_strength += random.randint(1, 3)
            self._health_points += random.randint(5, 10)
            print(f"    |    Combat Strength increased to {self._combat_strength}")
            print(f"    |    Health Points increased to {self._health_points}")