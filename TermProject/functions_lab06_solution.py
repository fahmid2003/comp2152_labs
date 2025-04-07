# functions_lab06_solution.py
import random

def use_loot(belt, health_points, combat_strength):
    if not belt:
        print("    |    Your belt is empty.")
        return belt, health_points, combat_strength

    print("    |    !!You quickly use your first item:")
    first_item = belt.pop(0)
    print(f"    |    You used: {first_item}")

    if "Health Potion" in first_item:
        heal_amount = int(first_item.split()[-1])
        health_points = min(20, health_points + heal_amount)
        print(f"    |    Health increased by {heal_amount} to {health_points}")
    elif "Strength Elixir" in first_item:
        strength_boost = int(first_item.split()[-1])
        combat_strength += strength_boost
        print(f"    |    Combat Strength increased by {strength_boost} to {combat_strength}")
    elif "Weakening Poison" in first_item:
        # This will affect the next monster encountered (not implemented in this function directly)
        print("    |    You apply weakening poison (effect on next monster).")
    elif "Minor Heal" == first_item:
        health_points = min(20, health_points + 5)
        print(f"    |    Health increased by 5 to {health_points}")
    else:
        print("    |    That item had no immediate effect.")
    return belt, health_points, combat_strength

def collect_loot(loot_options, belt):
    ascii_image3 = """
                        @@@ @@
                     *# ,      @
                   @          @
                      @@@@@@@@
                     @   @ @% @*
                   @     @  ,   &@
                 @
                @
               @
               @
              @*
               @
                 @@@@@@@@@@@@
                 """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    You found: ", loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt

def save_game(winner, hero, hero_name="", num_stars=0):
    total_monsters_killed = 0
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                if "Total monsters killed" in line:
                    try:
                        total_monsters_killed = int(line.split(":")[1].strip())
                    except ValueError:
                        total_monsters_killed = 0
                    break
    except FileNotFoundError:
        pass

    with open("save.txt", "a") as file:
        file.write(f"--- Game Outcome ---\n")
        if winner == "Hero":
            file.write(f"Winner: Hero {hero_name}\n")
            file.write(f"Stars Earned: {num_stars}\n")
            total_monsters_killed += 1
        elif winner == "Monster":
            file.write("Winner: Monster\n")
        file.write(f"Hero Level: {hero.level}\n")
        file.write(f"Hero Experience: {hero.experience}\n")
        file.write(f"Hero Health: {hero.health_points}\n")
        file.write(f"Hero Strength: {hero.combat_strength}\n")
        file.write(f"Total monsters killed: {total_monsters_killed}\n")
        file.write("\n")

def load_game(hero):
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            saved_data = {}
            for line in lines:
                line = line.strip()
                if ":" in line:
                    key, value = line.split(":", 1)
                    saved_data[key.strip()] = value.strip()

            if "Hero Level" in saved_data:
                hero.level = int(saved_data["Hero Level"])
            if "Hero Experience" in saved_data:
                hero.experience = int(saved_data["Hero Experience"])
            if "Hero Health" in saved_data:
                hero.health_points = int(saved_data["Hero Health"])
            if "Hero Strength" in saved_data:
                hero.combat_strength = int(saved_data["Hero Strength"])
            if "Total monsters killed" in saved_data:
                print(f"    |    Total monsters killed in previous games: {saved_data['Total monsters killed']}")
            if "Winner" in saved_data:
                print(f"    |    Last game outcome: {saved_data['Winner']}")
            return True
    except FileNotFoundError:
        print("    |    No previous game found. Starting fresh.")
        return False
    except ValueError:
        print("    |    Error loading saved data. Starting fresh.")
        return False

def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game (we'll just read the last outcome for now)
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            last_game = None
            for line in reversed(lines):
                if "--- Game Outcome ---" in line:
                    break
                if "Winner:" in line:
                    last_game = line.split(":")[1].strip()
                    break

            if last_game:
                if last_game == "Hero":
                    # Increase monster strength if the hero
                    print("    |    ... Increasing the monster's combat strength since you won last time")
                    return combat_strength, m_combat_strength + 1
                elif last_game == "Monster":
                    # Increase hero strength if the monster won
                    print("    |    ... Increasing the hero's combat strength since you lost last time")
                    return combat_strength + 1, m_combat_strength
                else:
                    print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
                    return combat_strength, m_combat_strength
            else:
                print("    |    No previous game outcome found, no combat strength adjustment.")
                return combat_strength, m_combat_strength

    except FileNotFoundError:
        print("    |    No save file found, no combat strength adjustment.")
        return combat_strength, m_combat_strength

# Recursion
# You can choose to go crazy, but it will reduce your health points by 1
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))