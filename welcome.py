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
