import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__(random.randint(1, 6), random.randint(1, 20))

    def __del__(self):
        super().__del__("Hero")
