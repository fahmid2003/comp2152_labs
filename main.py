# main.py

# Import the platform library
import platform
print(f"    |    Python Version: {platform.python_version()}")

import os
print(f"    |    Operating System: {os.name}")

import random
import functions_lab06_solution
from hero import Hero
from monster import Monster

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion +10", "Poison Potion -5", "Strength Elixir +2", "Minor Heal", "Weakening Poison"]
belt = []

monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

num_stars = 0

hero = Hero()

# Load game data
functions_lab06_solution.load_game(hero)

monster = Monster()

i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    hero_combat_input = input(f"Enter your Hero's initial Combat Strength (currently {hero.combat_strength}, 1-6): ")
    print("    |", end="    ")
    monster_combat_input = input(f"Enter the Monster's initial Combat Strength (currently {monster.m_combat_strength}, 1-6): ")

    if (not hero_combat_input.isnumeric()) or (not monster_combat_input.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue
    elif (int(hero_combat_input) not in range(1, 7)) or (int(monster_combat_input) not in range(1, 7)):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue
    else:
        hero.combat_strength = int(hero_combat_input)
        monster.m_combat_strength = int(monster_combat_input)
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False

    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
                  , %
        * @./  #       @ &.(
      @       /@  (     ,   @     # @
      @       ..@#% @   @&*#@(       %
        &   ( @   ( / /   * @ . /
          @ % #     /   .     @ ( @
                % .@*
              #     .
            /   # @ *
              ,   %
          @&@     @&@
          """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)
    hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    functions_lab06_solution.adjust_combat_strength(hero.combat_strength, monster.m_combat_strength)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    hero.health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(hero.health_points) + " health points")

    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    monster.health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(monster.health_points) + " health points for the monster")

    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")
    loot_options, belt = functions_lab06_solution.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")
    loot_options, belt = functions_lab06_solution.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    belt, hero.health_points, hero.combat_strength = functions_lab06_solution.use_loot(belt, hero.health_points, hero.combat_strength)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.m_combat_strength))
    print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                  @%  @
              @   @
                  &
            @   .

          @   @         @
              @       @
            @   @     @ @
              @   @@@@@@@   @
                @         @
                  @     @
                    @@@@@@@

          """
    print(ascii_image4)
    power_roll = random.choice(list(monster_powers.keys()))
    monster.m_combat_strength = min(6, monster.m_combat_strength + monster_powers[power_roll])
    print(f"    |    The monster's combat strength is now {monster.m_combat_strength} using {power_roll} magic power")

    num_dream_lvls = -1
    while (num_dream_lvls < 0 or num_dream_lvls > 3):
        print("    |", end="    ")
        dream_level_input = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        try:
            num_dream_lvls = int(dream_level_input)
            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                print("    |    Number entered must be a whole number between 0-3 inclusive, try again")
                num_dream_lvls = -1
            elif (not num_dream_lvls == 0):
                hero.health_points -= 1
                crazy_level = functions_lab06_solution.inception_dream(num_dream_lvls)
                hero.combat_strength += crazy_level
                print("combat strength: " + str(hero.combat_strength))
                print("health points: " + str(hero.health_points))
        except ValueError:
            print("    |    Invalid input. Please enter a whole number between 0-3 inclusive.")
            num_dream_lvls = -1
        print("num_dream_lvls: ", num_dream_lvls)

    # Fight Sequence (moved earlier)
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while monster.health_points > 0 and hero.health_points > 0:
        print("    ------------------------------------------------------------------")
        print(f"    |    Hero Level: {hero.level}, Health: {hero.health_points}, Strength: {hero.combat_strength}")
        print(f"    |    Monster: {monster.monster_name}, Health: {monster.health_points}, Strength: {monster.m_combat_strength}")
        action = input("    |    Choose your action: (attack/special/run): ").lower()

        if action == "attack":
            print("    |", end="    ")
            input("You attack (Press enter)")
            monster.health_points = hero.hero_attacks(monster)
            if monster.health_points > 0:
                print("    |", end="    ")
                input("The monster attacks (Press enter)")
                hero.health_points = monster.monster_attacks(hero)
        elif action == "special":
            monster.health_points = hero.use_special_ability(monster)
            if monster.health_points > 0:
                print("    |", end="    ")
                input("The monster attacks (Press enter)")
                hero.health_points = monster.monster_attacks(hero)
        elif action == "run":
            run_success = random.randint(1, 4) > 1  # 75% chance to run
            if run_success:
                print("    |    You successfully ran away!")
                break  # Exit the combat loop
            else:
                print("    |    You failed to run away!")
                print("    |", end="    ")
                input("The monster attacks (Press enter)")
                hero.health_points = monster.monster_attacks(hero)
        else:
            print("    |    Invalid action.")

        if monster.health_points <= 0:
            print(f"    |    You defeated the {monster.monster_name}!")
            hero.experience += monster.level * 50  # Gain experience based on monster level
            num_stars = 3
            break
        elif hero.health_points <= 0:
            print("    |    You have been defeated!")
            num_stars = 1
            break

    if(monster.health_points <= 0):
        winner = "Hero"
    else:
        winner = "Monster"

    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
        functions_lab06_solution.save_game(winner, hero, hero_name=short_name, num_stars=num_stars)