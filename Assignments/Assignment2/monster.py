import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__(random.randint(1, 6), random.randint(1, 20))

    def __del__(self):
        super().__del__("Monster")
    
    # Monster's Attack Function
    def monster_attacks(self, hero):
        ascii_image2 = """                                                                 
            @@@@ @                           
        (     @*&@  ,                         
        @               %                       
        &#(@(@%@@@@@*   /                      
        @@@@@.                                
                @       /                    
                    %         @                 
                ,(@(*/           %              
                @ (  .@#                 @   
                            @           .@@. @
                    @         ,              
                        @       @ .@          
                                @              
                            *(*  *      
                """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(self.combat_strength) + ") ---> Player (" + str(hero.health_points) + ")")
        if self.combat_strength >= hero.health_points:
            # Monster was strong enough to kill player in one blow
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            hero.health_points -= self.combat_strength
            print("    |    The monster has reduced Player's health to: " + str(hero.health_points))