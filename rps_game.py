import random # This line imports the 'random' module, which we'll use to make the computer's choice.
import time   # This line imports the 'time' module, which allows us to add pauses.
import json   # NEW: Import the 'json' module for saving and loading data

# --- File Paths ---
GAME_DATA_FILE = "game_data.json" # Define the file name for persistent storage

# --- Game Rules Definition (for different modes) ---
# Standard Rock-Paper-Scissors rules
RPS_RULES = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}

# Custom Game: The Rock, Wrapping Paper, Shark Tooth Scissors
# Define how each new custom choice beats another
CUSTOM_RULES_PRESET = { # Renamed to differentiate from user-defined custom rules
    "the rock": ["shark tooth scissors"],
    "wrapping paper (colorful)": ["the rock"],
    "shark tooth scissors": ["wrapping paper (colorful)"]
}

# --- Persistent Data Handling Functions ---
def load_game_data():
    """
    Loads game data (overall scores, custom rules) from a JSON file.
    Initializes with defaults if the file doesn't exist or is empty.
    """
    try:
        with open(GAME_DATA_FILE, 'r') as f:
            data = json.load(f)
            print(f"Loaded game data from {GAME_DATA_FILE}")
            return data
    except FileNotFoundError:
        print(f"No existing game data found. Creating new data file: {GAME_DATA_FILE}")
        return {
            "total_series_player_wins": 0,
            "total_series_computer_wins": 0,
            "total_series_ties": 0,
            "saved_custom_rules": {} # To store user-defined custom games
        }
    except json.JSONDecodeError:
        print(f"Error decoding {GAME_DATA_FILE}. Starting with new game data.")
        return {
            "total_series_player_wins": 0,
            "total_series_computer_wins": 0,
            "total_series_ties": 0,
            "saved_custom_rules": {}
        }

def save_game_data(data):
    """
    Saves the current game data to a JSON file.
    """
    try:
        with open(GAME_DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4) # Use indent for pretty-printing JSON
            print(f"Saved game data to {GAME_DATA_FILE}")
    except IOError as e:
        print(f"Error saving game data to {GAME_DATA_FILE}: {e}")

# --- Function to get user's choice ---
def get_user_choice(valid_choices):
    """
    Prompts the user to enter their choice (from valid_choices)
    and validates the input. Also allows 'quit' to exit the game.
    """
    # This block constructs a user-friendly string of valid choices.
    # For example, ["rock", "paper", "scissors"] becomes "rock, paper, or scissors".
    if len(valid_choices) == 1:
        choices_str = valid_choices[0]
    elif len(valid_choices) == 2:
        choices_str = f"{valid_choices[0]} or {valid_choices[1]}"
    else:
        choices_str = ", ".join(valid_choices[:-1]) + ", or " + valid_choices[-1]

    while True:
        # Improved prompt for clarity
        user_input = input(f"Enter your choice ({choices_str}), or type 'quit' to exit: ").lower().strip()
        
        if user_input in valid_choices or user_input == "quit":
            return user_input
        else:
            # Second refinement: Improved error message to include the user's invalid input
            print(f"'{user_input}' is not a valid option. Please choose from: {choices_str}, or type 'quit'.")

# --- Function to get computer's choice ---
def get_computer_choice(valid_choices):
    """
    Generates a random choice for the computer from the given valid_choices.
    """
    return random.choice(valid_choices) # random.choice() picks a random item from the list

# --- Function to determine the winner based on rules ---
def determine_winner(user_choice, computer_choice, rules):
    """
    Compares the user's and computer's choices and determines the winner
    based on the provided game rules.
    Returns a string indicating the result and a winner indicator ('user', 'computer', 'tie').
    """
    if user_choice == computer_choice:
        return "It's a tie!", "tie"
    elif computer_choice in rules.get(user_choice, []): # Use .get() with default for robustness
        return "You win!", "user"
    elif user_choice in rules.get(computer_choice, []): # Use .get() with default for robustness
        return "Computer wins!", "computer"
    else:
        # This else should ideally not be reached with correct rules and valid inputs
        return "Something went wrong!", "tie" # Fallback, should indicate an error in logic

# --- Main game logic ---
if __name__ == "__main__":
    print("--- Welcome to Rock, Paper, Scissors! ---")
    print("Let's play a best-of-3 series against the computer!")
    time.sleep(1) # Pause for 1 second

    # NEW: Load game data at the start
    game_data = load_game_data()
    total_series_player_wins = game_data["total_series_player_wins"]
    total_series_computer_wins = game_data["total_series_computer_wins"]
    total_series_ties = game_data["total_series_ties"]
    saved_custom_rules = game_data["saved_custom_rules"] # Load saved custom rules

    # Outer loop for playing multiple series
    while True:
        # --- Game Mode Selection ---
        print("\n--- Choose your game mode ---")
        game_mode_choice = ""
        # Offer option to load previously saved custom game
        custom_game_options = list(saved_custom_rules.keys())
        custom_game_prompt = ""
        if custom_game_options:
            custom_game_prompt = f"\n      '4' to Load a Saved Custom Game ({', '.join(custom_game_options)})"
        
        while game_mode_choice not in ["1", "2", "3", "4"] and (game_mode_choice != "4" or not custom_game_options):
            game_mode_choice = input(
                "Enter '1' for Classic Rock-Paper-Scissors (RPS)\n"
                "      '2' for The Rock, Wrapping Paper, Shark Tooth Scissors (Custom Fun)\n"
                "      '3' to Create New Custom Rock-Paper-Scissors Names"
                f"{custom_game_prompt}\n" # Include load option if available
                "Your choice: "
            ).strip()
            
            if game_mode_choice == "4" and not custom_game_options:
                print("No saved custom games to load. Please choose another option.")
                game_mode_choice = "" # Reset to re-prompt
            elif game_mode_choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please enter '1', '2', '3', or '4' (if available).")

        current_choices = []
        current_rules = {}
        mode_name = ""

        if game_mode_choice == "1":
            current_choices = list(RPS_RULES.keys())
            current_rules = RPS_RULES
            mode_name = "Classic Rock-Paper-Scissors"
        elif game_mode_choice == "2":
            current_choices = list(CUSTOM_RULES_PRESET.keys())
            current_rules = CUSTOM_RULES_PRESET
            mode_name = "The Rock, Wrapping Paper, Shark Tooth Scissors (Custom Fun)"
        elif game_mode_choice == "3": # Create New Custom Game
            print("\n--- Create Your Own Game ---")
            game_name = input("Give your custom game a name (e.g., 'My Animal RPS'): ").strip()
            if not game_name:
                print("Game name cannot be empty. Please try again.")
                continue # Restart outer loop

            # Loop until unique names are provided
            while True:
                name_rock = input(f"Enter a name for 'Rock' in '{game_name}': ").lower().strip()
                name_paper = input(f"Enter a name for 'Paper' in '{game_name}': ").lower().strip()
                name_scissors = input(f"Enter a name for 'Scissors' in '{game_name}': ").lower().strip()

                # Check for uniqueness and non-empty
                if not (name_rock and name_paper and name_scissors):
                    print("All names must be entered. Please try again.")
                elif len(set([name_rock, name_paper, name_scissors])) < 3:
                    print("Names must be unique. Please try again.")
                else:
                    break # All conditions met, exit inner loop

            # Dynamically create rules based on user input
            current_rules = {
                name_rock: [name_scissors],
                name_paper: [name_rock],
                name_scissors: [name_paper]
            }
            current_choices = [name_rock, name_paper, name_scissors]
            mode_name = f"Custom Game: {game_name}"
            # NEW: Save the newly created custom game rules
            saved_custom_rules[game_name] = current_rules
            game_data["saved_custom_rules"] = saved_custom_rules # Update game_data dict
            save_game_data(game_data) # Persist the new custom game
            
        elif game_mode_choice == "4": # Load Saved Custom Game
            if not custom_game_options:
                print("No custom games saved to load.")
                continue # Restart outer loop if no options
            
            while True:
                load_name = input(f"Enter the name of the custom game to load ({', '.join(custom_game_options)}): ").strip()
                if load_name in saved_custom_rules:
                    current_rules = saved_custom_rules[load_name]
                    current_choices = list(current_rules.keys())
                    mode_name = f"Loaded Custom Game: {load_name}"
                    break
                else:
                    print(f"'{load_name}' not found. Please enter a valid saved game name.")
            
        print(f"You've selected: {mode_name}!")
        time.sleep(1)

        # Initialize scores for each new series
        player_score = 0
        computer_score = 0
        ties = 0
        round_number = 0

        player_name = input("\nPlease enter your name for this series: ")
        if not player_name.strip():
            player_name = "Player" # Default name if empty input
        print(f"\n--- Starting a new Best-of-3 Series with {player_name} in {mode_name} mode! ---")
        time.sleep(1.5) # Pause for 1.5 seconds

        # Inner loop for playing rounds within a series until someone wins 2
        while player_score < 2 and computer_score < 2:
            round_number += 1
            print(f"\n--- Round {round_number} ---")
            time.sleep(0.5)

            # 1. Get user's choice (pass the current valid choices)
            player_choice = get_user_choice(current_choices)
            if player_choice == "quit":
                print("\nExiting current series...")
                break # Break from the inner loop
            print(f"{player_name} chose: {player_choice}")
            time.sleep(0.5)

            # 2. Get computer's choice (pass the current valid choices)
            ai_choice = get_computer_choice(current_choices)
            print(f"Computer chose: {ai_choice}")
            time.sleep(0.5)

            # 3. Determine and display the winner, and update scores (pass the current rules)
            round_result, winner_indicator = determine_winner(player_choice, ai_choice, current_rules)
            print(round_result)

            if winner_indicator == "user":
                player_score += 1
            elif winner_indicator == "computer":
                computer_score += 1
            else:
                ties += 1 # Ties still count for display, but not for winning a series

            # Display current scores for the series
            print(f"Series Score: {player_name} {player_score} - Computer {computer_score} - Ties {ties}")
            time.sleep(0.7)

        # Check if the inner loop was broken by a 'quit' command
        if player_choice == "quit":
            break # Exit the outer loop (end the entire game)

        # After the inner loop breaks, a series winner has been determined (unless quit)
        print("\n--- Series Over! ---")
        if player_score >= 2:
            print(f"Congratulations, {player_name}! You won this series!")
            total_series_player_wins += 1
        elif computer_score >= 2: # This means computer_score is 2 or more
            print("The Computer won this series. Better luck next time!")
            total_series_computer_wins += 1
        else: # This case is reached if player quits before a series winner is determined
            print("This series ended prematurely.")
            # We don't add to total series wins/losses if it was a mid-series quit
        time.sleep(1)

        print("\nFinal Series Scores:")
        print(f"  {player_name} Wins: {player_score}")
        print(f"  Computer Wins: {computer_score}")
        f"  Ties: {total_series_ties}"
