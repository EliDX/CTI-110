# In-class examples of dictionaries.

# Create a dictionary.

peace_lily = {"growth_habit":"bushy","flower_color":"white","avg_height":2,"nontoxic":False}

# Get value given the key.
print(f"The average height of a peace lily is {peace_lily['avg_height']} feet")
print()

# Get another value given the key.
print(f"Are peace lilies nontoxic? {peace_lily['nontoxic']}")
print()

# Get another value, without the f string.
print(peace_lily["flower_color"])
print()

# Add a key value pair.
peace_lily["sci_nm"] = "spathipyllum"

# Print the dictionary.
print(peace_lily)
print()

# Using update to add key value pairs.
peace_lily.update({"leaf_color":"dark green","sun":"bright indirect"})
print(peace_lily)
print()

# Deleting a key and value.
del peace_lily["sun"]
print(peace_lily)
print()
print()


#Printing only the keys.
print(peace_lily.keys())
print()

# Ask the user to give a key.
answer = input("Enter a key from the dictionary: ")
print()

# Give the value associated with the users answer.
print(f"The value for {answer} is {peace_lily[answer]}")
print()
