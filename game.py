import random

# CLASSES
class Person:
    """creates a person object that can engage in battle"""
    def __init__(self, name = "default_char", health = 100, level = 1):
        self.name = name
        self.health = health
        self.level = level
    
    def __str__(self):
        return self.name
    
    def attack(self, other):
        amt = self.level * 10
        other.health -= amt
        print("%s took %d damage! %d health remains!" % (other.name, amt, other.health))

    def give_in(self):
        print("I yield!")


class Opponent(Person): 
    """creates an opponent object, which inherits from person, that the player does not control in battle"""
    def attack(self, other):
        scale = random.randint(7, 10)
        amt = self.level * scale
        other.health -= amt
        print("%s took %d damage! %d health remains!" % (other.name, amt, other.health))


class Deck:
    """creates a deck with flashcards to review"""
    def __init__(self, name):
        self.card_list = {}
        self.name = name
    
    def __str__(self):
        return self.name
    
    def add_cards(self):
        front = input("> Enter front: ")
        back = input("\n> Enter back: ")
        print("Card successfully added.")
        self.card_list[front] = back
    
    def pull_card(self):
        key = random.choice(list(self.card_list.keys()))
        print("-------\nENTERING CARD...ANSWER TO ATTACK: \n")
        answer = input("> Type the correct value to this card: %s\n> " % key)
        print("The correct answer is: %s. Your answer was %s." % (self.card_list[key], answer))
    
    

# MAIN FUNCTION
class Game:
    
    menu = {'q': 'quit game', 
            'cd': 'create new deck', 
            'sm': 'show menu', 
            'b': 'start battle', 
            'uc': "update character",
            'ad': 'add to deck'}

    deck_folder = []

    def __init__(self, mc):
        self.mc = mc
        self.deck = self.create_deck()
    
    def get_prompt(self):
        request = input("> Command: ")
        return request
    
    def show_menu(self):
        for key in Game.menu: 
            padding = 7 - len(key)
            print(key, ("." * padding), Game.menu[key], sep='')
    
    def create_deck(self):
        name = input("> Enter new deck name: ")
        new_deck = Deck(name)
        Game.deck_folder.append(new_deck)
        return Game.deck_folder[0]

    def add_to_deck(self):
        self.deck.add_cards()
    
    def battle(self, team1, team2):
        """prepares for battle
        
        params
            team1 (Person object): Player
            team2 (Person object): Opponent
        """
        # k = 0
        # char_sequence = [team1, team2]
        print("I'm %s, ready for battle!" % team1, "\n")
        print("I'm %s, ready for battle too!" % team2)

        while True:
            # turn based code
            # k = k % 2
            # current = char_sequence[k]
            # next = char_sequence[(k+1) % 2]
            # k += 1

            if team1.health <= 0:
                team1.give_in()
                break

            if team2.health <= 0:
                team2.give_in()
                break

            b_request = input("> Battle Command: ")

            if b_request == 'q':
                print("Retreating... \nSuccess!")
                break

            if b_request == 'a':
                print("Attacking %s!\n" % team2.name)
                self.deck.pull_card()
                team1.attack(team2)

            team2.attack(team1)

    def update_character(self):
        self.mc.name = input("> Enter new name: ")
        print("Thanks, my new name is %s!" % self.mc.name)
    
    
    
    def run(self):
        while True:
            request = self.get_prompt()
            
            if request == 'q':
                print('Saving progress... Successfully quit game!')
                break
            
            if request == 'sm':
                self.show_menu()
            
            if request == 'cd':
                self.create_deck()
            
            if request == 'ad':
                self.add_to_deck()

            if request == 'b':
                opp = Opponent("%s's opponent" % self.mc.name)
                self.battle(self.mc, opp)
            
            if request == 'uc':
                self.update_character()
            
            


# MAIN GAME LOOP
you = Person()
game_1 = Game(you)
game_1.run()