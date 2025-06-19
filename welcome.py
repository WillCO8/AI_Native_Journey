# This script asks the user for their name and age,
# then prints a personalized welcome message using variables.

def greet_user_with_age(name, age):
    """
    Generates a personalized welcome message including name and age.

    Args:
        name (str): The name of the user.
        age (int): The age of the user.

    Returns:
        str: The personalized welcome message.
    """
    return f"Hello, {name}! Welcome to your Python journey. You are {age} years old."

# --- Main part of the script ---
if __name__ == "__main__":
    # 1. Ask the user for their name and store it in the 'user_name' variable
    user_name = input("Please enter your name: ")

    # --- Bug Fix: Handle Empty Name Input ---
    # Add a check to ensure the user actually entered a name.
    if not user_name.strip(): # .strip() removes leading/trailing whitespace
        print("You didn't enter a name. Please try again with a valid name.")
    else:
        # --- Existing Conditional Logic for Personalized Greeting ---
        # We're adding an 'if/else' statement to check the user's name.
        # Replace "William" below with YOUR actual name (e.g., "Sarah", "John")
        if user_name.lower() == "william": # .lower() makes the comparison case-insensitive
            print(f"Hey, it's the awesome AI Director, {user_name}! Welcome back to your Python journey.")
        else:
            # 2. Ask the user for their age and store it in the 'user_age' variable
            # We use int() to convert the input (which is text) into a whole number
            try:
                user_age = int(input("Please enter your age: "))
            except ValueError:
                user_age = "an unknown number of" # Handle cases where age isn't a valid number
                print("Invalid age entered. Using 'an unknown number of' for age.")

            # 3. Generate the personalized welcome message using both variables
            welcome_message = greet_user_with_age(user_name, user_age)

            # 4. Print the welcome message
            print(welcome_message)

    # --- Polishing Improvement: Script Completion Message ---
    print("\nScript execution completed. Goodbye!")
