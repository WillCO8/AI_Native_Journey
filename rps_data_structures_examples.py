# This file demonstrates different Python data structures useful for a
# Rock-Paper-Scissors game or similar projects.

# --- 1. Python List for Valid Choices ---
# A list is an ordered, changeable collection of items.
# It's perfect for when you just need a sequence of items.
# Analogy: A shopping list where each item is simply listed.

print("--- Example 1: Using a List for Valid Choices ---")
valid_choices = ["rock", "paper", "scissors"]

print(f"All valid choices for the game: {valid_choices}")

# You can check if an item is in the list
user_input = "rock"
if user_input in valid_choices:
    print(f"'{user_input}' is a valid choice.")
else:
    print(f"'{user_input}' is not a valid choice.")

# You can also access items by their position (index)
print(f"The first valid choice is: {valid_choices[0]}")
print("-" * 40)


# --- 2. Python Dictionary for Game Rules ---
# A dictionary is an unordered, changeable collection of key-value pairs.
# It's ideal for storing relationships, like "rock beats scissors".
# Analogy: A translation dictionary, where you look up a word (key)
#          to find its meaning (value).

print("\n--- Example 2: Using a Dictionary for Game Rules ---")
# This dictionary defines what each choice beats.
# Key: The choice
# Value: The choice that the key beats
game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

print(f"Game rules defined: {game_rules}")

# To find out what 'rock' beats:
print(f"Rock beats: {game_rules['rock']}")

# Example of using rules to determine a winner
player_choice = "rock"
computer_choice = "scissors"

if game_rules.get(player_choice) == computer_choice:
    print(f"Player chose '{player_choice}', Computer chose '{computer_choice}'. Player wins!")
elif game_rules.get(computer_choice) == player_choice:
    print(f"Player chose '{player_choice}', Computer chose '{computer_choice}'. Computer wins!")
else:
    print("It's a draw!")
print("-" * 40)


# --- 3. Python List of Dictionaries for Game History ---
# Combining lists and dictionaries allows for storing structured records
# of multiple items, like a history of game rounds.
# Analogy: A stack of index cards, where each card (dictionary) has
#          specific fields (key-value pairs) like 'player_choice', 'winner'.

print("\n--- Example 3: Using a List of Dictionaries for Game History ---")
game_history = [] # Initialize an empty list to store game rounds

# Create dictionaries for individual rounds
round_1_data = {
    "round_number": 1,
    "player_choice": "rock",
    "computer_choice": "scissors",
    "result": "player_win"
}
game_history.append(round_1_data) # Add the round dictionary to the list

round_2_data = {
    "round_number": 2,
    "player_choice": "paper",
    "computer_choice": "paper",
    "result": "draw"
}
game_history.append(round_2_data)

round_3_data = {
    "round_number": 3,
    "player_choice": "scissors",
    "computer_choice": "rock",
    "result": "computer_win"
}
game_history.append(round_3_data)

print("Full game history:")
for round_entry in game_history:
    print(f"  Round {round_entry['round_number']}: Player '{round_entry['player_choice']}', Computer '{round_entry['computer_choice']}', Result: {round_entry['result']}")

# You can access specific data from a round in the history
print(f"Result of Round 1: {game_history[0]['result']}")
print("-" * 40)
