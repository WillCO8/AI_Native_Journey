def get_user_words():
    """
    Asks the user for a noun, a verb, and an adjective,
    and returns these three words as a tuple.
    """
    print("\n--- Let's get some words! ---")
    noun = input("Please enter a noun: ").strip()
    verb = input("Please enter a verb: ").strip()
    adjective = input("Please enter an adjective: ").strip()
    
    print("Thanks! Got your words.")
    return (noun, verb, adjective)

# Example of how you might use this function if it were in a script:
if __name__ == "__main__":
    my_noun, my_verb, my_adjective = get_user_words()
    print(f"You entered: Noun='{my_noun}', Verb='{my_verb}', Adjective='{my_adjective}'")

