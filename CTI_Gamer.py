# Health is how much damage you can take before getting knocked out.
# Sadly there is no inventory. I couldn't think of a way to add one in.
# Strength is used to determine how much damage you can deal with an attack.
# Defense reduced the damage taken by whatever value it is.
# Coolness measures how cool you are. It isnt displayed to the player, but changing its value can have various effects.

def create_character():
    name = input("What is your character's name? ")
    health = int(30)
    strength = int(3)
    defense = int(0)
    cool = int(10)

    player_character = {
        "Name": name,
        "Health": health,
        "Strength": strength, 
        "Defense": defense,
        "Coolness": cool,
        }
    return player_character


# This function will create the enemy we will encounter. I want it to be random which enemy we encounter for each battle.
# I stored each enemy directly into a dictionary for later use.
# The max health value is used to reset each enemies hp after every battle.

def summon_enemy(amount):
    templates = [
        {
            "Name": "Evil Pickle",
            "Max Health": 15,
            "Health": 15,
            "Strength": 2,
            "Defense": 0,
            "Coolness": 0,
        },
        {
            "Name": "Malicious Beetroot",
            "Max Health": 10,
            "Health": 10,
            "Strength": 1,
            "Defense": 2,
            "Coolness": 0,
        },
        {
            "Name": "Violent Kimchi",
            "Max Health": 5,
            "Health": 5,
            "Strength": 2,
            "Defense": 0,
            "Coolness": 50,
        },
        {
            "Name": "Suspicious Sauerkraut",
            "Max Health": 8,
            "Health": 8,
            "Strength": 3,
            "Defense": 0,
            "Coolness": 0,
        },
    ]
    return [random.choice(templates) for enemy in range(amount)]
    
            
def create_villain():
    name = "Dastardly Horseradish"
    health = float(30)
    strength = int(5)
    defense = int(0)
    cool = int(20)

    villain = {
        "Name": name,
        "Health": health,
        "Strength": strength,
        "Defense": defense,
        "Coolness": cool,
        }
    return villain

'''
def regular_battle(char1, enemies):
    while char1['Health'] > 0 and enemy['Health'] > 0:
'''

'''
def final_battle(character, villain):
'''       

 # This function lets you see a characters full stats during battle.
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
    Game_Over = False
    print("Game is starting...")
    print("Controls: Use the numbers 1-5 to make choices when prompted.")
    print()
    print()
	char1 = create_character()
	print()
	print(f"Ok, so basically, {char1['Name']} was like um, chilling? Or something, and the Dastardly Horseradish and his army of pickled vegetables find you.")
	print("They pickled all of your food, and you seek vengeance for their crimes...")
	print("You must defeat the 3 elite teams he sent after you to get to him.")
	print()
	group1 = summon_enemy(2)
	for enemy in group1:
		print(f"{enemy['Name']}\n(Health: {enemy['Health']}, Strength: {enemy['Strength']}, Defense: {enemy['Defense']})\n")
	show_battle_stats(char1)

    group2 = summon_enemy(3)
	for enemy in group3:
		print(f"{enemy['Name']}\n(Health: {enemy['Health']}, Strength: {enemy['Strength']}, Defense: {enemy['Defense']})\n")
	show_battle_stats(char1)

    group3 = summon_enemy(4)
	for enemy in group4:
		print(f"{enemy['Name']}\n(Health: {enemy['Health']}, Strength: {enemy['Strength']}, Defense: {enemy['Defense']})\n")
	show_battle_stats(char1)



