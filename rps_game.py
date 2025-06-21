import random # This line imports the 'random' module, which we'll use to make the computer's choice.
import time   # This line imports the 'time' module, which allows us to add pauses.

# --- Game Rules Definition (for different modes) ---
# Standard Rock-Paper-Scissors rules
RPS_RULES = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}

# Custom Game: The Rock, Wrapping Paper, Shark Tooth Scissors
# Define how each new custom choice beats another
CUSTOM_RULES = {
    "the rock": ["shark tooth scissors"],
    "wrapping paper (colorful)": ["the rock"],
    "shark tooth scissors": ["wrapping paper (colorful)"]
}

# --- Function to get user's choice ---
def get_user_choice(valid_choices):
    """
    Prompts the user to enter their choice (from valid_choices)
    and validates the input. Also allows 'quit' to exit the game.
    """
    while True:
        # Construct the prompt string clearly showing all options
        # Handle cases where valid_choices might have only one or two items
        if len(valid_choices) == 1:
            choice_prompt = valid_choices[0]
        elif len(valid_choices) == 2:
            choice_prompt = f"{valid_choices[0]} or {valid_choices[1]}"
        else:
            choice_prompt = ", ".join(valid_choices[:-1]) + ", or " + valid_choices[-1]

        user_input = input(f"Enter your choice ({choice_prompt}, or 'quit' to exit): ").lower()
        if user_input in valid_choices or user_input == "quit":
            return user_input
        else:
            print(f"Invalid choice. Please enter one of {choice_prompt} or 'quit'.")

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
    elif computer_choice in rules[user_choice]: # If user_choice beats computer_choice
        return "You win!", "user"
    elif user_choice in rules[computer_choice]: # If computer_choice beats user_choice
        return "Computer wins!", "computer"
    else:
        # This else should ideally not be reached with correct rules and valid inputs
        return "Something went wrong!", "tie" # Fallback, should indicate an error in logic

# --- Main game logic ---
if __name__ == "__main__":
    print("--- Welcome to Rock, Paper, Scissors! ---")
    print("Let's play a best-of-3 series against the computer!")
    time.sleep(1) # Pause for 1 second

    # Initialize overall series scores
    total_series_player_wins = 0
    total_series_computer_wins = 0
    total_series_ties = 0

    # Outer loop for playing multiple series
    while True:
        # --- Game Mode Selection ---
        print("\n--- Choose your game mode ---")
        game_mode_choice = ""
        while game_mode_choice not in ["1", "2", "3"]:
            game_mode_choice = input(
                "Enter '1' for Classic Rock-Paper-Scissors (RPS)\n"
                "      '2' for The Rock, Wrapping Paper, Shark Tooth Scissors (Custom Fun)\n"
                "      '3' to Create Your Own Rock-Paper-Scissors Names: "
            ).strip()
            if game_mode_choice not in ["1", "2", "3"]:
                print("Invalid choice. Please enter '1', '2', or '3'.")

        if game_mode_choice == "1":
            current_choices = list(RPS_RULES.keys())
            current_rules = RPS_RULES
            mode_name = "Classic Rock-Paper-Scissors"
        elif game_mode_choice == "2": # Now maps to Custom Fun
            current_choices = list(CUSTOM_RULES.keys())
            current_rules = CUSTOM_RULES
            mode_name = "The Rock, Wrapping Paper, Shark Tooth Scissors (Custom Fun)"
        else: # game_mode_choice == "3" - Create Your Own Names
            print("\n--- Create Your Own Game ---")
            # Loop until unique names are provided
            while True:
                name_rock = input("Enter a name for 'Rock': ").lower().strip()
                name_paper = input("Enter a name for 'Paper': ").lower().strip()
                name_scissors = input("Enter a name for 'Scissors': ").lower().strip()

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
            mode_name = f"Custom Game: {name_rock}, {name_paper}, {name_scissors}"

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
        print(f"  Ties: {ties}")
        time.sleep(1)

        # Display overall game record
        print("\n--- Overall Game Record ---")
        print(f"Total Series Won by {player_name}: {total_series_player_wins}")
        print(f"Total Series Won by Computer: {total_series_computer_wins}")
        print(f"Total Series Tied: {total_series_ties}") # If you wanted to track series ties
        time.sleep(1.5)


        # Ask if the user wants to play another series
        play_another_series = input("Do you want to play another best-of-3 series? (yes/no): ").lower()
        if play_another_series != "yes":
            break # Exit the outer loop if the user doesn't want to play another series

    print("\n--- Goodbye! Thanks for playing Rock, Paper, Scissors! ---")
    print("Final Overall Game Record:")
    print(f"  Your Total Series Wins: {total_series_player_wins}")
    print(f"  Computer Total Series Wins: {total_series_computer_wins}")
    print(f"  Total Series Tied: {total_series_ties}")
