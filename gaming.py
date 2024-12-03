# Elijah Dixon
# 11/2024
# Stupid dumb dumb stupid game

import random
def player_party():


    
def create_character():
    name = input("Enter characater name: ")
    health = float(input(f"Enter {name}'s health: "))
    inventory = []
    weapons = ["bazooka"]
    strength = int(input(f"Enter {name}'s strength: "))

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Weapons": weapons,
        "Strength": strength,
        }
    return character

def create_villain():
    name = "Dastardly Horseradish"
    health = float(8)
    inventory = ["horseradish", "horse", "radish"]
    weapons = ["mason jar"]
    strength = int(2)

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Weapons": weapons,
        "Strength": strength,
        }
    return character

def battle_test(char1, horseradish):
    while char1['Health'] > 0 and horseradish['Health'] > 0:
        # Define characters...
        characters = [char1, horseradish]

        # Randomly shuffle the characters
        random.shuffle(characters)

        # Assign attacker and victim
        attacker = characters[0]
        defender = characters[1]

        # Damage calculator...
        
        
        print(f"{characters} are duking it out?!")
        print(f"{attacker} attacks!")
        print(f"{defender} takes {damage} damage...")
        


def show_stats(character):
    # Character is a dictionary
    print()
    print(f"{character['Name']}'s Stats...")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")
    print(f"Weapons: {character['Weapons']}")
    print(f"Items: {character['Items']}")
    print()
