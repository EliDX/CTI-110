# Elijah Dixon
# 12/5/2024
# Using functions in python to make a text based game where you battle pickled vegetables.

import random

# First I determine the stats for my character.
# Health is how much damage you can take before getting knocked out.
# Sadly there is no inventory. I couldn't think of a way to add one in.
# Strength is used to determine how much damage you can deal with an attack.
# The m_strength/defense stats
# Defense reduced the damage taken by whatever value it is.
# Coolness measures how cool you are. It isnt displayed to the player, but changing its value can have various effects.

def create_character():
    name = input("What is your character's name? ")
    health = int(30)
    m_health = int(30)
    m_strength = int(3)
    strength = int(3)
    m_defense = int(0)
    defense = int(0)
    cool = int(20)

    player_character = {
        "Name": name,
        "Max Health": m_health,
        "Health": health,
        "Base Strength": m_strength,
        "Strength": strength,
        "Base Defense": m_defense,
        "Defense": defense,
        "Coolness": cool,
        }
    return player_character


# This function will create the enemy we will encounter. I want it to be random which enemies we encounter for each battle.
# I stored each enemy directly into a dictionary for later use.
# The max health value is used to reset each enemies hp after every battle, so we can fight the same 'type' more than once.
# I did not balance these stats too well... 

def summon_enemy(amount):
    templates = [
        {
            "Name": "Evil Pickle",
            "Max Health": 15,
            "Health": 15,
            "Strength": 2,
            "Defense": 0,
            "Coolness": 5,
        },
        {
            "Name": "Malicious Beetroot",
            "Max Health": 10,
            "Health": 10,
            "Strength": 1,
            "Defense": 2,
            "Coolness": 5,
        },
        {
            "Name": "Violent Kimchi",
            "Max Health": 5,
            "Health": 5,
            "Strength": 2,
            "Defense": 0,
            "Coolness": 70,
        },
        {
            "Name": "Suspicious Sauerkraut",
            "Max Health": 8,
            "Health": 8,
            "Strength": 3,
            "Defense": 0,
            "Coolness": 10,
        },
    ]
    return [random.choice(templates) for enemy in range(amount)]
    # It is returning a random selection of enemies from the templates according to the amount specified.

# I want to handle the villain sepreately from the regular enemies. 
def create_villain():
    name = "Dastardly Horseradish"
    health = float(30)
    strength = int(5)
    defense = int(1)
    cool = int(40)

    villain = {
        "Name": name,
        "Health": health,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return villain


# We need t calculate the damage based on a characters strength.
def attack(attacker, defender):
# Calculate attack damage dealt to the enemy.
    damage = max(1, attacker["Strength"] - defender["Defense"])
# Using the Coolness stat to determine critical hits.
    if random.randrange(1,101) <= attacker["Coolness"]:
        damage = damage + (attacker["Strength"]//2)
        print(f"{attacker['Name']} landed a critical!")
    defender["Health"] -= damage
    print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage!")
    if defender["Health"] <= 0:
        print(f"{defender['Name']} got knocked out!")
        defeats = defeats + 1


# These are regular battles with the regular enemeies. there can be more than one.ChatGPT helped me a bit with this.
def battle(player, opponents):
    print()
    print("The pickled army approaches!")
    while player["Health"] > 0 and any(opponent["Health"] > 0 for opponent in opponents):
        print()
        print(f"\n{player['Name']} - Health: {player['Health']}")
        for i, opponent in enumerate(opponents):
            if opponent["Health"] > 0:
                print(f"{i + 1}. {opponent['Name']} - Health: {opponent['Health']}")
                
        action = input("\nActions:\n(1)Attack\n(2)Check enemies stats.\n(3)Check your stats.\n")
        print()
        
        if action == "1":
            # The player chooses which opponent to attack.
            try:
                target_index = int(input("Choose your target (number): ")) - 1
                if 0 <= target_index < len(opponents) and opponents[target_index]["Health"] > 0:
                    attack(player, opponents[target_index])
                else:
                    print("Invalid target. Choose a valid opponent.")
            except ValueError:
                print("Numbers only, please!")
              
            
            # Live opponents will fight back. If your g
            for opponent in opponents:
                if opponent["Health"] > 0:
                    attack(opponent, player)
                    if player["Health"] <= 0:
                        break
        elif action == "2":
            print()
            for enemy in opponents:
                print(f"{enemy['Name']}\n(Health: {enemy['Health']}, Strength: {enemy['Strength']}, Defense: {enemy['Defense']})\n")
         
        elif action == "3":
            print()
            show_battle_stats(player)
                   
        else:
            print("Invalid action.\nActions:\n(1)Attack\n(2)Check enemies stats.\n(3)Check your stats.")
    
    if player["Health"] <= 0:
        print(f"{player['Name']} has been defeated. Game Over!")
        Game_Over = True
        
    elif all(opponent["Health"] <= 0 for opponent in opponents):
        print(f"{player['Name']} obliterated the opposition.")
        for enemy in opponents:
            enemy["Health"] = enemy["Max Health"] 
        
    

 # This function lets you see a characters full stats during battle. I couldve made this variable shorter.
def show_battle_stats(character):
    # Character is a dictionary, we call each item from the dictionary to get the stats needed for player view.
        print()
        print(f"{character['Name']}'s Stats...")
        print(f"Health: {character['Health']}")
        print(f"Strength: {character['Strength']}")
        print(f"Defense: {character['Defense']}")
        print(f"Coolness: {character['Coolness']}")
        print()


# This is the main game program.
def main():
    
    global keep_running
    keep_goin = True

    global defeats
    defeats = int(0)
    
    while keep_goin == True:
        print("Game is starting...")
        print("Controls: Use the numbers 1-5 to make choices when prompted.")
        print()
        print()
        char1 = create_character()
        show_battle_stats(char1)
        print()
        print(f"Ok, so basically, {char1['Name']} was like um, chilling? Or something, and the Dastardly Horseradish and his army of pickled vegetables find you.")
        print("They pickled all of your food, and you seek vengeance for their crimes...")
        print("You must defeat the 3 elite teams he sent after you to get to him.")
        print()
        input("Press ENTER to continue.")
        print()
        group1 = summon_enemy(2)
        print("Enemies appeared!!!!")
        print()
        battle(char1,group1)

    
        

# Calling the main.
if __name__ == "__main__":
    main()
