class Character:
    def __init__(self, strength, hp):
        self.__combat_strength = strength
        self.__health_points = hp

    def __del__(self, type):
        print(f"The {type} object is being destroyed by the garbage collector.")

    @property
    def combat_strength(self):
        return self.__combat_strength
    
    @combat_strength.setter
    def combat_strength(self, strength):
        self.__combat_strength = strength

    @property
    def health_points(self):
        return self.__health_points
    
    @health_points.setter
    def health_points(self, hp):
        self.__health_points = hp