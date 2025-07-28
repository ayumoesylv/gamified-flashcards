import random

# CLASSES
class Person:
    """creates a person object that can engage in battle"""
    def __init__(self, name = "default_char", health = 100, level = 0):
        self.name = name
        self.health = health
        self.level = level
    
    def __str__(self):
        return self.name
    
    def die(self):
        return


class Deck:
    """creates a deck with flashcards to review"""
    def __init__(self, name):
        self.card_list = []
        self.name = name
    
    def __str__(self):
        return self.name
    
    def add_cards():
        return
    
    

# MAIN FUNCTION
class Game:
    
    menu = {'q': 'quit game', 
            'cd': 'create new deck', 
            'sm': 'show menu', 
            'b': 'start battle', 
            'uc': "update character"}

    deck_folder = []

    def __init__(self, mc):
        self.mc = mc
    
    def get_prompt(self):
        request = input("> Command: ")
        return request
    
    def create_deck(self):
        name = input("> Enter name: ")
        new_deck = Deck(name)
        Game.deck_folder.append(new_deck)
        return
    
    def show_menu(self):
        for key in Game.menu: 
            padding = 7 - len(key)
            print(key, ("." * padding), Game.menu[key], sep='')
    
    def battle(self, team1, team2):
        """prepares for battle
        
        params
            team1 (Person object): Player
            team2 (Person object): Opponent
        """
        k = 0
        print("I'm %s, ready for battle!" % team1, "\n")
        print("I'm %s, ready for battle too!" % team2)

        while True:
            b_request = input("> Battle Command: ")
            char_sequence = [team1, team2]
            k = k % 2
            turn = char_sequence[k]
            k += 1

            if turn.health <= 0:
                turn.die()
                break

            if b_request == 'q':
                print("Retreating... \nSuccess!")
                break
        

    def update_character(self):
        self.mc.name = input("> Enter new name: ")
        print("Thanks, my new name is %s!" % self.mc.name)
    
    def run(self):
        while True:
            request = self.get_prompt()
            
            if request == 'q':
                print('Saving progress... Successfully quit game!')
                break

            if request == 'cd':
                self.create_deck()

            if request == 'sm':
                self.show_menu()

            if request == 'b':
                opp = Person("%s's opponent" % self.mc.name)
                self.battle(self.mc, opp)
            
            if request == 'uc':
                self.update_character()
            


# MAIN GAME LOOP
you = Person()
game_1 = Game(you)
game_1.run()