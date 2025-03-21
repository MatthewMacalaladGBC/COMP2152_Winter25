# Import the random library to use for the dice later
import random
import os
import platform

# Put all the functions into another file and import them
from hero import Hero
from monster import Monster
import functions

print("Operating System: ", os.name)
print("Python Version: ", platform.python_version())

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

hero = Hero()
monster = Monster()
print("    |    The hero's base combat strength is " + str(hero.combat_strength))
print("    |    The hero's base health points are " + str(hero.health_points))
print("    |    The monster's base combat strength is " + str(monster.combat_strength))
print("    |    The monster's base health points are " + str(monster.health_points))

# Roll for weapon
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")
ascii_image5 = """
            , %               .           
*      @./  #         @  &.(         
@        /@   (      ,    @       # @ 
@        ..@#% @     @&*#@(         % 
&   (  @    (   / /   *    @  .   /  
    @ % #         /   .       @ ( @    
                %   .@*                
            #         .              
            /     # @   *              
                ,     %                
        @&@           @&@
        """
print(ascii_image5)
weapon_roll = random.choice(small_dice_options)

print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

# Limit the combat strength to 6
hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))

functions.adjust_combat_strength(hero, monster)

# Weapon Roll Analysis
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

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

print("You're updated combat strength is " + str(hero.combat_strength))

# Collect Loot
print("    ------------------------------------------------------------------")
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (enter)")

# Collect Loot First time
loot_options, belt = functions.collect_loot(loot_options, belt)
print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Roll for second item (Press enter)")

# Collect Loot Second time
loot_options, belt = functions.collect_loot(loot_options, belt)

print("    |    You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("    |    Your belt: ", belt)

# Use Loot
belt, hero.health_points = functions.use_loot(belt, hero.health_points)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))

# Check the Player's overall strength and health
print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

# Roll for the monster's power
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
ascii_image4 = """
            @%   @                      
        @     @                        
            &                          
    @      .                          

    @       @                    @     
            @                  @      
    @         @              @  @     
    @            ,@@@@@@@     @      
        @                     @        
        @               @           
                @@@@@@@                

                                    """
print(ascii_image4)
power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

# Increase the monster’s combat strength by its power
monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
print("    |    The monster's combat strength is now " + str(
    monster.combat_strength) + " using the " + power_roll + " magic power")

num_dream_lvls = -1 # Initialize the number of dream levels
while (num_dream_lvls < 0 or num_dream_lvls > 3 or num_dream_lvls >= hero.health_points):
    # Call Recursive function
    try:
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? The deeper you go, the more strength you gain, and the more hp you lose... (Enter a number 0-3)")
        # If the value entered was not an integer, set the number of dream levels to -1 and loop again 
    except ValueError:
        print("Number entered must be a whole number between 0-3 inclusive, and lower than your current hp. Try again")

    health_points -= num_dream_lvls
    crazy_level = functions.inception_dream(num_dream_lvls)
    combat_strength += crazy_level
    
    if num_dream_lvls > 0:
        print("num_dream_lvls: ", num_dream_lvls)
        print("Your combat strength increased to " + str(combat_strength))
        print("Your health points decreased to " + str(health_points))

# Fight Sequence
# Loop while the monster and the player are alive. Call fight sequence functions
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")
while monster.health_points > 0 and hero.health_points > 0:
    # Fight Sequence
    print("    |", end="    ")

    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        print("    |", end="    ")
        input("You strike (Press enter)")
        hero.hero_attacks(monster)
        if monster.health_points == 0:
            num_stars = 3
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("    |    The monster strikes (Press enter)!!!")
            monster.monster_attacks(hero)
            if health_points == 0:
                num_stars = 1
            else:
                num_stars = 2
    else:
        print("    |", end="    ")
        input("The Monster strikes (Press enter)")
        monster.monster_attacks(hero)
        if hero.health_points == 0:
            num_stars = 1
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("The hero strikes!! (Press enter)")
            hero.hero_attacks(monster)
            if monster.health_points == 0:
                num_stars = 3
            else:
                num_stars = 2

if(monster.health_points <= 0):
    winner = "Hero"
else:
    winner = "Monster"

# Final Score Display
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

    functions.save_game(winner, hero_name=short_name, num_stars=num_stars)       


