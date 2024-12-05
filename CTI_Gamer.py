# Elijah Dixon
# 12/5/2024
# Using python functions to create a text based game where you battle pickled vegetables to the death.

import random
    
def create_character():
    name = input("Enter characater name: ")
    health = int(20)
    inventory = []
    equipment = []
    strength = int(3)
    defense = int(0)
    cool = int(10)

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Equipment": equipment,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return character


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

            
def create_villain():
    name = "Dastardly Horseradish"
    health = float(50)
    inventory = ["horseradish", "horse", "radish"]
    equipment = ["mason jar"]
    strength = int(5)
    defense = int(0)
    cool = int(20)

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Equipment": equipment,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return character

'''
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
        attack = attacker{}
        
        
        print(f"{characters} are duking it out?!")
        print(f"{attacker} attacks!")
        print(f"{defender} takes {damage} damage...")
'''        
def show_stats(character):
    # Character is a dictionary
    print()
    print(f"{character['Name']}'s Stats...")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")
    print(f"Equipment: {character['Equipment']}")
    print(f"Items: {character['Items']}")
    print()



def main():
    print("Welcome!")
    print("Game is starting...")
    create_enemy()
    

# Calling the main
if __name__ == "__main__":
    main()
