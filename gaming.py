# Elijah Dixon
# 11/2024
# Stupid dumb dumb stupid game

def create_character():
    name = input("Enter characater name: ")
    health = float(input(f"Enter {name}'s health: "))
    inventory = []
    weapons = ["bazooka"]
    strength = int(input(f"Enter [name]'s strength: "))

    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Weapons": weapons,
        "Strength": strength,
        }
    return character





def main():
    print("awaken, my child")
    print()
    # Call create character
    char1 = create_character()
    print()
    print(char1)


# Calling your moms house.
if __name__ == "__main__":
    main()
