# Elijah Dixon
# 12/5/2024
# Using python functions to create a text based game where you battle pickled vegetables to the death.

import random

# This function will create the player character.
# Health is how much damage you can taje before getting knocked out.
# The inventory has consumable items.
# The equipment area has things thta can be used more than once.
# Strength is used to determine how much damage you can deal with an attack.
# Defence reduced the damage taken by whatever value it is.
# Coolness measures how cool you are. It isnt displayed to the player, but changing its value can have various effects.

def create_character():
    name = input("What is your characaters name? ")
    health = int(30)
    inventory = []
    equipment = ["Fists"]
    strength = int(3)
    defense = int(0)
    cool = int(10)

    player_character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Equipment": equipment,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return player_character


# This function will create the enemy we will encounter. I want it to be random which enemy we encounter for each battle, so

def create_enemy():
    name_choices = ["Evil Pickle", "Malicious Beetroot", "Violent Kimchi", "Suspicious Sauerkraut"]
    random.shuffle(name_choices)
    name = name_choices[0]
    
    if name == "Evil Pickle":
        health = int(25)
        inventory = []
        equipment = []
        strength = int(2)
        defense = int(0)
        cool = int(5)

    elif name == "Malicious Beetroot":
        health = int(20)
        inventory = []
        equipment = []
        strength = int(3)
        defense = int(1)
        cool = int(10)
    
    elif name == "Violent Kimchi":
        health = int(20)
        inventory = []
        equipment = []
        strength = int(7)
        defense = int(0)
        cool = int(0)
        
    elif name == "Suspicious Sauerkraut":
        health = int(15)
        inventory = []
        equipment = []
        strength = int(3)
        defense = int(2)
        cool = int(60)

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Equipment": equipment,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    print(f"{name} appeared!?")
    show_stats(character)
    return character
    name_choices.remove(name)

            
def create_villain():
    name = "Dastardly Horseradish"
    health = float(50)
    inventory = ["horseradish", "horse", "radish"]
    equipment = ["mason jar"]
    strength = int(5)
    defense = int(0)
    cool = int(20)

    villain = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Equipment": equipment,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return villain

'''
def regular_battle(char1, enemy):
    while char1['Health'] > 0 and enemy['Health'] > 0:
'''
        
 
def show_stats(character):
    # Character is a dictionary, we call each item from the dictionary to get the stats needed for player view.
    print()
    print(f"{character['Name']}'s Stats...")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")
    print(f"Equipment: {character['Equipment']}")
    print(f"Items: {character['Items']}")
    print()



def main():
    print("Game is starting...")
    print("Controls: Use the numbers 1-5 to make choices when prompted.")
    print()
    print()
    char1 = create_character()
    print()
    print(f"Ok, so basically, {main_character_name}, was like, chilling, and the Dastardly Horseradish and his army of pickled vegetables find you.")
    print("They pickled all of your food, and you seek vengeance for their crimes...")
    print("You must defeat the 4 strongest members of his army to get to him.")
    print()
    create_enemy()
    

# Calling the main
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
