# Import the random library to use for the dice later
import random

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Recursion
# You can choose to go crazy, but it will reduce your health points by 1 per level
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


# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    total_kills = load_monster_kills()

    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    lines = [line for line in lines if "Total monsters killed" not in line]

    if winner == "Hero":
        total_kills += 1
        lines.append(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
    else:
        lines.append("Monster has killed the hero previously\n")

    lines.append(f"Total monsters killed: {total_kills}\n")

    with open("save.txt", "w") as file:
        file.writelines(lines)

def load_monster_kills():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip()
            if "Total monsters killed" in last_line:
                return int(last_line.split(": ")[-1])
    except FileNotFoundError:
        pass
    return 0

def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_result = lines[-2].strip() # Second last line, as last line is now always total monsters killed
                print(last_result)
                return last_result
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

# Lab 06 - Question 5b
def adjust_combat_strength(hero, monster):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                monster.combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            hero.combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


