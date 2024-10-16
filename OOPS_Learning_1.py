# https://dev.to/jesseilc123/oop-python-for-dummies-9oa

# Programming paradigms: are different ways or styles in which a given program or programming language can be organized.

# A popular paradigm is Object Oriented Programming or OOP for short. OOP is the ability to organize code, enhance reusability, and imporve maintainability.

# In basic terms, OOP is a programming pattern that is built areound objects or entities so it's called object-orineted programming.


class VideoGames:
    # class attributes, are used for storing values
    games_list = []
    
    # class constants, constant values and doesn't change.
    SYSTEMS_LIST = ["Xbox", "Playstation", "Switch"]
    
    # __init__ constructor: intantiates objects of our class.
    def __init__(self, game, system): # game and system are parameters need to be passed witht he class.
        if self.check_system(system):
            # instance attributes
            self.game = game
            self.system = system
            VideoGames.games_list.append(self)
        
    # __repr__ function , translates the objects into readable
    def __repr__(self):
        return f"Game(game={self.game}, " +\
                f"system={self.system})"
    
    
    
    # Instance methods open_game and close_game
    def open_game(self):
        return f"Booting {self.game} on the {self.system}"
        
    def close_game(self):
        return f"Closing {self.game} on the {self.system}"
        
    
    # class method: referes to the class not the instance object.
    @classmethod
    def check_system(cls, system):
        return system in cls.SYSTEMS_LIST
    
    
    

game1 = VideoGames("Cricket", "Xbox")

print(game1)
print(game1.game)
print(game1.system)
print(game1.games_list)
game2 = VideoGames("MH World", "Playstation")
game3 = VideoGames("Metal Gear Rising", "PC")
print(VideoGames.games_list)
