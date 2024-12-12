# MMmmm.... ipormt

import random

# Value returning function.

def get_habitat(plant):
    if plant.lower() in ["rockweed", "red algae", "phytoplankton", "sugar kelp", "pickle weed"]:
        return "ocean"
    if plant.lower() in ["agave", "saguro cactus", "prickly pear", "yucca", "aloe"]:
        return "desert"
    if plant.lower() in ["philodendron", "bromeliad", "rubber tree", "cacao", "orchid"]:
        return "jungle"

# Defining another function.

def get_another(habitat, grab_amount):
    taken = []
    if habitat == "ocean":
        ocean_list = ["rockweed", "red algae", "phytoplankton", "sugar kelp", "pickle weed"]
        #Loop runs grab_amount times.
        for i in range(grab_amount):
            # Snatch a random plant from the ocean list to the taken list.
            taken.append(random.choice(ocean_list))
        return taken
    
    if habitat == "desert":
        desert_list = ["agave", "saguro cactus", "prickly pear", "yucca", "aloe"]
        #Loop runs grab_amount times.
        for i in range(grab_amount):
            # Snatch a random plant from the desert list to the taken list.
            taken.append(random.choice(desert_list))
        return taken

    if habitat == "jungle":
        jungle_list = ["philodendron", "bromeliad", "rubber tree", "cacao", "orchid"]
        #Loop runs grab_amount times.
        for i in range(grab_amount):
            # Snatch a random plant from the jungle list to the taken list.
            taken.append(random.choice(jungle_list))
        return taken
        
# Define the main.

def main():
    keep_goin = "hell yeah"
    while keep_goin.lower() != "exit":
        print()
        print("😋😍😏😛")
        plant = input("Enter a plant that grows in the wild: ")
        habitat = get_habitat(plant)
        if habitat == None:
            print("I ONLY KNOW 15 PLANTS OK 😭😭😭")
            continue
        print(f"I grabbed a {plant}, it was living in the {habitat}.")
        print()
        grab_amount = int(input(f"How many MORE {habitat} plants should I grab? "))
        # Call that tasty functi wuncti
        theft = get_another(habitat, grab_amount)
        print("\nOk here: ")
        # LOOP...
        for i in theft:
            print(f"{i}")
        print()
        keep_goin = input("Press ENTER to tell me another plant to grab, or type 'exit' to close. ")

# Call the main...
if __name__ == "__main__":
    main()
