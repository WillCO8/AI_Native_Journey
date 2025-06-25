Rock Paper Scissors
About This Project
This is a customizable Rock-Paper-Scissors game developed as a command-line interface (CLI) application. It allows players to enjoy the classic game, a "Custom Fun" mode with unique choices, or even create their own custom game rules. The project includes persistent data storage to track overall series wins and save user-defined custom game configurations across sessions. This mini-project was developed as part of an AI Native Journey, demonstrating foundational Python programming, iterative AI-driven refinement, and practical quality assurance.

Features
Multiple Game Modes: Play Classic Rock-Paper-Scissors, a fun "Custom Fun" variant with unique choices, or create and save your own custom game rules.

Best-of-3 Series: Engage in competitive series against the computer, tracking scores until a winner is determined.

Persistent Data: Overall player and computer wins, as well as custom game definitions, are saved to a game_data.json file, allowing progress to carry over between sessions.

User-Friendly Interface: Clear prompts and highly specific error messages ensure a smooth and intuitive gameplay experience.

How It Works (Core AI-Generated Logic)
The core logic and structure of this game were iteratively developed and refined with significant assistance from an AI. The AI played a crucial role by providing initial code structures, suggesting efficient ways to manage game flow and data, and critically, refining the user experience.

Specifically, the AI contributed to:

Core Game Mechanics: Generating the fundamental functions for getting user and computer choices, implementing the game rules to determine a winner, and managing the best-of-3 series structure.

Data Persistence: Assisting in setting up the JSON-based data saving and loading mechanisms for overall scores and custom game rules, allowing game progress to be stored between play sessions.

User Experience (UX) Enhancements: Collaborating with me to refine user prompts and error messages. Notably, the AI helped in crafting clear instructions for input and in implementing a highly specific error message that incorporates the user's exact invalid input (e.g., 'lizard' is not a valid option), making the game more intuitive and less frustrating.

Modular Design: Guiding the organization of the code into logical functions (get_user_choice, get_computer_choice, determine_winner, load_game_data, save_game_data) to ensure readability and maintainability.

The game leverages Python's built-in random module for computer choices and the json module for persistent data storage. It utilizes fundamental data structures like lists for valid choices and dictionaries for game rules, alongside conditional logic (if/elif/else) for decision-making.

How to Run It
To run this Rock Paper Scissors game, follow these steps:

Save the file: Ensure you have the rps_game.py file saved on your local machine.

Open your terminal or command prompt: Navigate to the directory where you saved rps_game.py.

Run the script: Execute the Python script using the command:

python3 rps_game.py

Follow the prompts: The game will start in your terminal, and you can follow the on-screen instructions to choose a game mode, enter your name, and make your choices.

Game Data: A file named game_data.json will be created in the same directory to store your overall game record and any custom game rules you create.

Future Plans / Roadmap
The immediate plan for this project is to expand beyond Rock Paper Scissors to include other simple games. This will likely involve:

Introducing new game logics and rulesets.

Potentially redesigning the main game selection interface.

Renaming the overall project to reflect the broader collection of games.

Enjoy playing Rock Paper Scissors!