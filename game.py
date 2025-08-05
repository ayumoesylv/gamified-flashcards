import random
import dbm
import pickle

# CLASSES
class Person:
    """creates a person object that can engage in battle"""
    def __init__(self, name = "default_char", health = 70, level = 1):
        self.name = name
        self.health = health
        self.level = level
        self.inventory = {}
        self.equipped = {}
    
    def __str__(self):
        return self.name

    def attack(self, other, scale):
        amt = self.level * (7 + scale)
        other.health -= amt
        print("%s took %d damage! %d health remains!" % (other.name, amt, other.health))

    def give_in(self):
        print("I yield!")
    
    def give_item(self, item):
        return
    
    def receive_item(self, item):
        self.inventory[item] += self.inventory.get(item, 0)
        return
    
    def equip_item(self):
        return
    
    def unequip_item(self):
        return
    



class Opponent(Person): 
    """creates an opponent object, which inherits from person, that the player does not control in battle"""

class Item:
    def __init__(self, name = "junk", level = 1, hp = 0, is_perishable = False):
        self.name = name
        self.level = level
        self.hp = hp
        self.is_perishable = is_perishable
    
    def use():
        return
    
    def __eq__(self, other):
        return self.name == other.name and self.level == other.level
    
    def __hash__(self):
        return hash((self.name, self.level))

class Deck:
    """creates a deck with flashcards to review"""
    def __init__(self, name):
        self.card_list = {}
        self.name = name
    
    def __str__(self):
        # return self.name
        return self.card_list
    
    def add_cards(self):
        front = input("> Enter front: ")
        back = input("\n> Enter back: ")
        print("Card successfully added.")
        self.card_list[front] = back
    
    def delete_cards(self):
        """deletes a card a user specifies by key name"""
        key = input("> Specify card: ")
        try:
            self.card_list.pop(key)
        except KeyError:
            print("Card not in %s. Try command prompt list deck cards to see all cards in %s" % (self.name, self.name))
    
    def pull_card(self):
        key = random.choice(list(self.card_list.keys()))
        print("-------\nENTERING CARD...ANSWER TO ATTACK: \n")
        answer = input("> Type the correct value to this card: %s\n> " % key)
        print("The correct answer is: %s. Your answer was %s." % (self.card_list[key], answer))
    
    def rate_card(self):
        rating = input("> How did you do? \n0 = fail, \n1 = hard, \n2 = okay, \n3 = easy\n> ")
        return int(rating)
    
    

# MAIN FUNCTION
class Game:
    
    menu = {'q': 'quit game', 
            'cd': 'create new deck', 
            'sm': 'show menu', 
            'b': 'start battle', 
            'uc': "update character",
            'ud': 'update deck',
            's': 'save data'}

    deck_folder = []

    def __init__(self, mc, db):
        # self.mc = mc
        # self.deck = self.create_deck()
        self.mc = pickle.loads(db["main character"]) if b"main character" in db else mc
        Game.deck_folder = pickle.loads(db["decks"]) if b"decks" in db else []
        self.deck = Game.deck_folder[0] if len(Game.deck_folder) >= 1 else self.create_deck()
    
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

    def update_deck(self):
        action = input("> Type a to add a card and d to delete a card: ")
        if action == 'a':
            self.deck.add_cards()
        elif action == 'd':
            self.deck.delete_cards()
    
    def update_character(self):
        self.mc.name = input("> Enter new name: ")
        print("Thanks, my new name is %s!" % self.mc.name)
    
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
                scale = self.deck.rate_card()
                team1.attack(team2, scale)

            scale = random.randint(0, 3)
            team2.attack(team1, scale)

    def save_data(self):
        db = dbm.open("savefile1.txt", "c")
        decks = pickle.dumps(self.deck_folder)
        mc = pickle.dumps(self.mc)
        db["decks"] = decks
        db["main character"] = mc
        print("Saving file... Success!")
        db.close()

    
    
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
            
            if request == 'ud':
                self.update_deck()
            
            if request == 'uc':
                self.update_character()

            if request == 'b':
                opp = Opponent("%s's opponent" % self.mc.name)
                self.battle(self.mc, opp)
            
            if request == 's':
                self.save_data()
            
            
            
            


# MAIN GAME LOOP
you = Person()
db = dbm.open("savefile1.txt", "c")
# decks = pickle.dumps([0, 1, 2])
# mc = pickle.dumps([3, 4, 5, 6, 7])
# db["decks"] = decks
# db["main character"] = mc

# for keys in db.keys():
#     print(keys, type(keys))

game_1 = Game(you, db)
db.close()
game_1.run()
