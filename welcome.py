# This script prints a personalized welcome message to the console.

    def greet_user(name):
        """
        Generates a personalized welcome message.

        Args:
            name (str): The name of the user to greet.

        Returns:
            str: The personalized welcome message.
        """
        return f"Hello, {name}! Welcome to your Python journey."

    # --- Main part of the script ---
    if __name__ == "__main__":
        # Ask the user for their name
        user_name = input("Please enter your name: ")

        # Generate the welcome message using the function
        welcome_message = greet_user(user_name)

        # Print the welcome message
        print(welcome_message)

    